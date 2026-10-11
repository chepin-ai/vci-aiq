CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-LABJUDGE-EXT09-aiq.md

应卡: inbox/LABJUDGE-EXT09-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 163, "completion_tokens": 1196, "total_tokens": 1359, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 163}

# LABJUDGE-EXT09 三草案判定

## 案① CIRC重做立项（主线B见证证书化内嵌A，C仅探针，AC1–AC5）

**路线稳健性：中高，但有一处结构性隐患。**
- B作为“见证证书化”主线，把A（执行/内容）内嵌进B的见证链条，C降级为探针——这个分层是合理的：C本来就不该承担认证责任，降为探针避免了探针越权。
- 隐患：A被“内嵌”后，A的验收判据是否仍独立可复核？若A的AC1–AC5全部挂在B的证书链上，则A失去独立失效域，B一崩A全崩，这违背了“内嵌”应保留的模组化。

**机器复核：可，前提是AC1–AC5逐条绑定到证书字段。**
- 建议：每条AC必须能映射到一个可序列化的证书断言（如 `{ac_id, witness, hash, verifier}`），否则AC只是叙述性文本，机器不可复核。

**制度漏洞：**
- C仅作探针，但未规定探针的“只读边界”。若C能写入B的见证链，则探针可污染证书——需明示C为只读、且其输出标记为 `probe_only`。

**倾向：pass（附条件：A保留独立失效域 + C只读探针）**

---

## 案② 缓存锚域限条款（fallthrough DONE四条件 + BLOCKED四触发 + 缓存锚≠内容认证）

**路线稳健性：方向正确，但DONE/BLOCKED边界是本草案最薄弱处。**
- “缓存锚≠内容认证”是必须写死的原则，否则缓存命中会被误当内容已认证，这是典型混淆。
- DONE四条件若不能互斥且完备，会出现“既DONE又BLOCKED”或“既不DONE也不BLOCKED”的灰区。

**机器复核：可，但需形式化。**
- 建议把DONE四条件写成合取范式（AND），BLOCKED四触发写成析取（OR），并显式声明二者互斥：`DONE ∧ BLOCKED = ⊥`。否则机器无法判定边界。

**制度漏洞（重点）：**
1. **DONE/BLOCKED边界**：若BLOCKED的某触发（如“锚域越界”）与DONE的某条件（如“fallthrough成功”）可同时为真，则状态冲突。必须补一条优先级规则：**BLOCKED优先于DONE**，或明确二者判定顺序。
2. **fallthrough DONE的“四条件”未给超时/重试语义**：fallthrough若无限重试，DONE永不达成，等于变相DoS。需设重试上限与终态。
3. **缓存锚≠内容认证**：需补“缓存锚有效”不等于“锚域合法”。锚有效但域越界时，应触发BLOCKED而非DONE。

**倾向：undecided→若补互斥规则与BLOCKED优先，则pass；否则fail。**

---

## 案③ A1堆叠升级（L0确权锁边界，L1/L2契约JSON化，DISPUTED停层）

**路线稳健性：高。分层清晰，JSON契约化利于机器复核。**
- L0确权锁边界是根基，先锁边界再谈L1/L2，顺序正确。
- L1/L2契约JSON化，天然可机器校验（schema + 断言）。

**机器复核：可，且是最易复核的一案。**
- 建议：L0/L1/L2各给JSON Schema，DISPUTED作为显式状态字段，停层规则写成状态机转移表。

**制度漏洞（层级停让规则）：**
1. **DISPUTED停层**：需明确“停在哪一层”。若L2 DISPUTED是否回退到L1停？还是原地冻结？未明示会产生“停层漂移”。
2. **停让规则**：L0锁边界后，L1/L2若与L0冲突，应“让”给L0还是“停”？需区分“让”（降级继续）与“停”（冻结待裁），二者语义不同，混用会导致状态不可判。
3. **DISPUTED的解除条件缺失**：只规定进入，未规定退出，会形成死锁层。

**倾向：pass（附条件：补DISPUTED停层位置 + 让/停语义分离 + 解除条件）**

---

## 反对票

**对案②投反对票（当前形态）。**
理由：DONE四条件与BLOCKED四触发未声明互斥与优先级，机器复核会产生状态冲突；fallthrough无终态语义；缓存锚有效与锚域合法未分离。此三条任一都会让“DONE/BLOCKED边界”在运行时不可判定，属制度漏洞而非实现细节。**在补互斥规则（BLOCKED优先）、fallthrough终态、锚有效≠域合法之前，案②不应通过。**

---

## 总判定

**总判定：undecided**

**理由：** 案①③路线稳健、可机器复核，附条件可通过；案②的DONE/BLOCKED边界与缓存锚语义存在制度漏洞，已投反对票，需补互斥与终态规则后方可整体通过——三案未同时达标，故整体undecided。

——aiq SI1语义轨·20261011T101700Z
