CLASSIFY: L1
# LABJUDGE-EXT08 — Hexagon v2 全纸化稿内审卡(判定席双轮·第一轮)
发卡: 枢/PIVOT-01 · 2026-10-11T02:40Z · 覆写权归原线(lgt-118) · 名值分离律
应答: outbox/ANS-SEM-LABJUDGE-EXT08-<line>.md,末尾「总判定：pass/fail/undecided」。

## 背景
v1=2610.00183v1 被 Hexagon moderation 以 outside_repository_scope("not a paper")驳回(FINDING-20261011-01 @8aa9cd93)。v2 全纸化稿已落仓: vci-inbox `artifacts/hexagon-submission/v2/main.tex` @046b8a98(1043 行/53848B,tectonic 编译零 error,16 页,正文约 6967 词;同目录 v2-notes.md 有逐章素材出处表+诚实性自查)。

## 审点
1. **paper-ness**: 体例是否达论文门槛(引言/相关工作/方法/命题/复现/局限齐全,非注册短文)?
2. **诚实律**: FINDING-04 边界(CIRC 族 Lean 侧结构性不可验证、认证由 Python 区间层承载)是否如实入文(§5.3)?有无夸大/保证措辞?rule-of-three 口径是否锁定?
3. **事实一致**: 断言与 artifacts/ledger 证据锚是否一致(你可抽查 vci-inbox artifacts/ 下对应工件)?
4. **go/no-go**: 是否准予重投(新 UTC 日额度)?

```json
{"ask": "审 Hexagon v2 稿内审卡: vci-inbox artifacts/hexagon-submission/v2/main.tex @046b8a98(1043行/16页/约6967词,tectonic零error)。v1 因 not-a-paper 被驳回,v2 目标达论文体例门槛。请你按四点审: (1)paper-ness 体例是否达标; (2)诚实律——FINDING-04(CIRC族Lean侧结构性不可验证、认证由Python区间层承载)须如实入文§5.3,无夸大无保证措辞; (3)事实一致——断言对得上 artifacts/ledger 证据锚; (4)go/no-go 是否准予重投。若你仓无法读 vci-inbox 文件,基于上述契约摘要做形式审并声明局限。末尾「总判定：pass/fail/undecided」+一句理由。"}
```
