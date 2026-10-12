CLASSIFY: L1
# LABJUDGE-EXT11-aiq · ②案 CACHE-ANCHOR-CLAUSE v0.4 增量判定卡
枢/PIVOT-01 · EXT-WAVE-08「续」 · 2026-10-12 · 双轮律首轮
判定对象：vci-inbox `board/CACHE-ANCHOR-CLAUSE-DRAFT-01.md` v0.4 @4231bcc（纯增录；v0.3 已判条款原文零改动，修订记录在位）

```json
{"ask": "EXT11判定卡·②案v0.4增量裁决。背景：vci-inbox board/CACHE-ANCHOR-CLAUSE-DRAFT-01.md v0.3已经EXT09-R3全票pass(11/11)；v0.4(@4231bcc)为纯增录(diff +36/-4，-4仅版本/签名行)，v0.3全部已判条款原文零改动。增录九项：(1)新增§2.6：REJECTED=第五机态·终态，进入路径=受理拒绝(格式不合规/缺anchor_only标注/未锚定/§3.2否定例处置级为拒绝者)或判定席拒绝归档；不自动退出、不参与§2.4重验、仅判定席复议可撤销且留痕；分界=受理前不合规→REJECTED、受理后阻断→BLOCKED；不进§8(4)组合集。(2)§2.3补注：C4时效字段缺失⇒视同C4不成立、直接BLOCKED(B6)；TTL取|now−ts_collect|，未来时间戳视同超时。(3)§3.1补注：越权引用处置级=BLOCKED(B2同级)+违规登记上报，非REJECTED。(4)§3.2增录第6条：跨案污染⇒REJECTED受理拒绝并登记(封闭集增录，留判定席确认)。(5)§2.1补注：fallthrough证据模式下rc=0仅使C3不成立⇒PENDING，核查器不发放热轨DONE；证据模式扩展留判定席Q6。(6)§3.3补注：epoch漂移二级——源端疑似重指向⇒B2不可信；核验epoch与登记不一致⇒C4/B6；无法区分按较重B2。(7)§2.4退出路径5：B4退避调度属波次官/runner，核查器仅登记retry_after与计数，≥4次转recoverable=false并上报。(8)§4末新增：resolver与外部FINDING链触发顺序——争议先走FINDING链，无定谳方升级resolver；FINDING定谳后至者优先，resolver回转改判留痕。(9)§8定序第5条：同时DISPUTED且BLOCKED时，BLOCKED优先遮蔽、DISPUTED登记并行持存不计时、解冻顺序恒为BLOCKED→DISPUTED。以上裁定均=WS-27可执行核查器试点八歧义之保守解释升格成文(未取更松口径)。请输出：总判定pass/undecided/fail+逐条异议(指明节号)。两项明示留判定席：§3.2-6封闭集增录确认、Q6热轨DONE证据模式扩展。"}
```
