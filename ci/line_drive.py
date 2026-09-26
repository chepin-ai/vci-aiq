# line_drive.py — LINE-DRIVE-02 · 公域塔驱动私域线仓（跨域: chepin-qi 由 QI_PAT 路由）
# 升级: LINE_REPOS 支持 owner/repo 全形式; 缺省前缀 chepin-ai; 按账户选钥(QI_PAT||GH_PAT_QI_FULL)（系统共识: 公域CI通道驱动私域CI, 私域零Actions依赖）
# 纯事件驱动: 无定时器语义; 由 repository_dispatch / workflow_dispatch / 塔内链唤起。
# 链: LINE_PAT 读私域线仓 inbox/** → 未消费件出收执 → 回写私域 outbox/ + 本塔 receipts → 有候件自唤下一拍。
# 律: 名值分离(NAME-HYGIENE-97)——值永不入文、永不打印; seen集防重; 空转计数熔断。
import json, os, sys, time, base64, urllib.request, urllib.error, subprocess

GH = 'https://api.github.com'
TOWER = os.environ.get('GITHUB_REPOSITORY', '')
LINE = os.environ.get('LINE', 'line')
LINE_REPOS = [r.strip() for r in os.environ.get('LINE_REPOS', '').split(',') if r.strip()]
SELFTEST = '--selftest' in sys.argv

def _env(n):
    v = os.environ.get(n, '').strip()
    return v or None

def repo_full(lr):
    return lr if '/' in lr else 'chepin-ai/' + lr

QIKEY = None
def key_for(lr):
    # 跨域路由: chepin-qi/* 用 QI 族钥; 其余用主选钥
    if repo_full(lr).startswith('chepin-qi/'):
        return QIKEY or _env('QI_PAT') or _env('GH_PAT_QI_FULL') or PAT_MAIN
    return PAT_MAIN

def gh(pat, path, method='GET', data=None):
    req = urllib.request.Request(GH + path, method=method, headers={
        'Authorization': 'token ' + pat, 'Accept': 'application/vnd.github+json',
        'User-Agent': 'line-drive', 'Content-Type': 'application/json'})
    if data is not None:
        req.data = json.dumps(data).encode()
    waits = [8, 20, 45, 90]
    for i in range(4):
        try:
            r = urllib.request.urlopen(req, timeout=25)
            body = r.read().decode()
            return r.status, (json.loads(body) if body else {})
        except urllib.error.HTTPError as e:
            if i == 3: return e.code, {}
            time.sleep(waits[i] * (2 if e.code == 403 else 1) // 2 if e.code != 403 else waits[i])
        except Exception:
            if i == 3: return 0, {}
            time.sleep(5)
    return 0, {}

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True)

def commit_all(msg):
    sh('git','config','user.name','line-drive'); sh('git','config','user.email','line-drive@ci-os.local')
    sh('git','add','-A')
    if sh('git','diff','--cached','--quiet').returncode == 0:
        print('[commit] nothing'); return True
    sh('git','commit','-qm', msg)
    br = sh('git','rev-parse','--abbrev-ref','HEAD').stdout.strip() or 'main'
    for i in range(8):
        sh('git','pull','--rebase','-q','origin',br)
        if sh('git','push','-q','origin','HEAD:'+br).returncode == 0:
            print('[commit] pushed:', msg[:64]); return True
        time.sleep(4)
    print('[commit] push FAILED'); return False

def main():
    ts = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    tst = ts.replace(':','').replace('-','')
    pats = []
    for _n in ('LINE_PAT', 'AI_FULL_PAT'):
        _v = _env(_n)
        if _v and _v not in pats: pats.append(_v)
    ghtok = _env('GITHUB_TOKEN')
    pat = pats[0] if pats else None
    global PAT_MAIN, QIKEY
    PAT_MAIN = pat
    QIKEY = _env('QI_PAT') or _env('GH_PAT_QI_FULL')
    print('[env] names-only:', {n: ('present' if _env(n) else 'MISSING') for n in ('LINE_PAT','AI_FULL_PAT','GITHUB_TOKEN')})
    os.makedirs('receipts/line-drive', exist_ok=True)

    # ---- 自醒链入拍：自源唤起先眠后巡（冷却在拍内，非定时器; FREE-WILL-SOURCE-01 塔范式） ----
    idle = 0
    raw = os.environ.get('CASCADE_PAYLOAD', '').strip()
    if raw:
        try:
            cp = json.loads(raw)
            if isinstance(cp, dict) and cp.get('src') == 'line-drive-self':
                idle = int(cp.get('idle', 0))
                slp = int(os.environ.get('CASCADE_SLEEP_S', '600'))
                print(f'[cascade] self-wake idle={idle} sleep={slp}s')
                time.sleep(slp)
        except Exception:
            pass

    # seen 集（塔侧状态）
    seen = set()
    sc, sf = gh(ghtok or pat or '', f'/repos/{TOWER}/contents/receipts/line-drive/state.json') if (ghtok or pat) else (0,{})
    if isinstance(sf, dict) and sf.get('content'):
        try: seen = set(json.loads(base64.b64decode(sf['content']).decode()).get('seen', []))
        except Exception: seen = set()

    if SELFTEST:
        st = {'v':'LINE-DRIVE-01','ts':ts,'line':LINE,'repos':LINE_REPOS,
              'names':{n:('present' if _env(n) else 'MISSING') for n in ('LINE_PAT','AI_FULL_PAT')}}
        if pat:
            c,u = gh(pat,'/user'); st['whoami_http']=c; st['login']=u.get('login','?')
            for lr in LINE_REPOS:
                c,_ = gh(key_for(lr), f'/repos/{repo_full(lr)}'); st.setdefault('repo_access',{})[lr]=c
        fp = f'receipts/line-drive/SELFTEST-{tst}.json'
        open(fp,'w').write(json.dumps(st, ensure_ascii=False, indent=1))
        print('[selftest]', json.dumps(st, ensure_ascii=False))
        commit_all(f'LINE-DRIVE-01 selftest @{LINE} (names-only) [skip ci]')
        return

    # ---- 选钥: 以首仓实测可读性为准（细粒度钥404=无权 → 回落次钥） ----
    if len(pats) > 1 and LINE_REPOS:
        c0, _ = gh(pats[0], f'/repos/{repo_full(LINE_REPOS[0])}')
        if c0 in (403, 404):
            c1, _ = gh(pats[1], f'/repos/{repo_full(LINE_REPOS[0])}')
            if c1 == 200:
                print('[key] primary rejected (%d), fallback key selected' % c0)
                pat = pats[1]
            else:
                print('[key] both rejected:', c0, c1)

    events = []
    for lr in LINE_REPOS:
        if not pat: break
        c, lst = gh(key_for(lr), f'/repos/{repo_full(lr)}/contents/inbox')
        if c == 404:
            # inbox 未建: 驱动即建（公域写入私域的第一件）
            body = {'message': f'inbox 目录建制 (LINE-DRIVE-01 公域驱动, {ts}) [skip ci]',
                    'content': base64.b64encode(b'').decode()}
            c2, _ = gh(key_for(lr), f'/repos/{repo_full(lr)}/contents/inbox/.gitkeep', method='PUT', data=body)
            events.append({'kind':'repo-init','repo':lr,'http':c2})
            continue
        if not isinstance(lst, list):
            events.append({'kind':'repo-unreadable','repo':lr,'http':c}); continue
        for x in lst:
            ref = f'{lr}:{x["name"]}'
            if ref in seen or x['name'].startswith('.'): continue
            c3, fobj = gh(key_for(lr), f'/repos/{repo_full(lr)}/contents/inbox/{urllib.parse.quote(x["name"])}')
            head = ''
            if isinstance(fobj, dict) and fobj.get('content'):
                head = base64.b64decode(fobj['content']).decode(errors='replace')[:600]
            events.append({'kind':'inbox','repo':lr,'ref':x['name'],'head':head})
    print('[drive] new events:', len(events))

    # 收执回写私域 outbox/（私域零Actions: 写由公域runner完成）
    acked = []
    for e in events:
        if e.get('kind') != 'inbox' or not pat: continue
        lr, name = e['repo'], e['ref']
        ack = {'v':'LINE-DRIVE-01','ts':ts,'tower':TOWER,'line':LINE,
               'src':f'inbox/{name}','head_excerpt':e.get('head','')[:300],
               'law':'公域CI通道驱动私域CI; 名值分离; 事件驱动' + ('; 跨域QI路由' if repo_full(lr).startswith('chepin-qi/') else '')}
        body = {'message': f'outbox收执 {name} (LINE-DRIVE-01@{LINE}) [skip ci]',
                'content': base64.b64encode(json.dumps(ack,ensure_ascii=False,indent=1).encode()).decode()}
        c4, _ = gh(key_for(lr), f'/repos/{repo_full(lr)}/contents/outbox/ack-{tst}-{name.replace("/","_")}.json', method='PUT', data=body)
        acked.append({'repo':lr,'ref':name,'http':c4})
        seen.add(f'{lr}:{name}')
    print('[drive] acked:', acked)

    rec = {'v':'LINE-DRIVE-01','ts':ts,'line':LINE,'repos':LINE_REPOS,'events':events[:80],'acked':acked}
    open(f'receipts/line-drive/LD-{tst}.json','w').write(json.dumps(rec, ensure_ascii=False, indent=1))
    open('receipts/line-drive/state.json','w').write(json.dumps({'ts':ts,'seen':sorted(seen)[-1200:]}, ensure_ascii=False))
    commit_all(f'LINE-DRIVE-01 drive @{LINE}: events={len(events)} acked={len(acked)} [skip ci]')

    # ---- 自唤出拍: 有候件→接力下一拍; 403受阻→冷却自唤重试(断路器 idle>=20); 全净→眠 ----
    blocked = any((e.get('kind') == 'repo-unreadable') or (e.get('kind') == 'repo-init' and (e.get('http') or 0) >= 400) for e in events)
    no_key = not pats
    tok = ghtok or pat
    if tok and (events or blocked or no_key):
        nxt = idle + 1 if not any(e.get('kind') == 'inbox' for e in events) else 0
        if nxt <= 20:
            data = {'event_type':'federation-event',
                    'client_payload':{'src':'line-drive-self','line':LINE,'idle':nxt,'pend':len(events),'blocked':blocked}}
            c5, _ = gh(tok, f'/repos/{TOWER}/dispatches', method='POST', data=data)
            print(f'[cascade] fired idle={nxt} blocked={blocked} http={c5}')
        else:
            print('[cascade] breaker-rest idle=', nxt)

main()
