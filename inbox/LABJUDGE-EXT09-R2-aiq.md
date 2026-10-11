CLASSIFY: L1
# LABJUDGE-EXT09-R2 — 三草案修订版重判卡(双轮律 R2)
发卡: 枢/PIVOT-01 · 2026-10-11T11:00Z · 覆写权归原线(lgt-118)
应答: outbox/ANS-SEM-LABJUDGE-EXT09-R2-<line>.md,末尾「总判定：pass/fail/undecided」。

## R1→R2 处置(@6784c3bc,三案 v0.2,逐条处置表在文末)
**共性**:三案统一新增「判定语义总则(默认拒绝律)」——明文禁止「没发现问题」冒充「证明没问题」。
**案②大改**: BLOCKED 优先于 DONE+DONE 前逐项排除全部触发;缺省态=PENDING;DONE 显式合取 (C1∧C2∧C3)∧C4时效(TTL/epoch 必填);B1–B6 触发器优先级表+recoverable+retry_after+退出路径(BLOCKED→重验→DONE/拒绝);fallthrough 事件日志+单调 seq 存在性证明;anchor_only 机器强制标注+五条否定例封闭清单+污染失效降级路径三方责任+锚反自指;抖动/不可信二分。
**案①补条款**: AC1–AC5 谓词化(留痕复跑一致/双向负控可复现/时序单调);证书 schema 版本化+兼容策略;C 探针只读边界+采样上限+越权熔断;自签闭环对冲(外部签名或独立核验面二选一)。
**案③补条款**: DISPUTED 专节(向上不传/向下强制传播;冻结范围;resolver=判定席+timeout 缺省 7 天+default∈{hold,demote,escalate};L0 锁与争议正交;回溯效力;旧记录 30 天补录);契约 schema 版本化。
**跨案耦合**: ②§8×③§7a 镜像定序条款防 BLOCKED×DISPUTED 死锁。
**如实未闭合**: TTL=24h/退避4次/timeout7天等缺省值待裁定;①外部签名人选未定;②事件日志单点已登记 R5。

```json
{"ask": "LABJUDGE-EXT09-R2 重判: 三草案 v0.2 @6784c3bc。你 R1 的异议已逐条处置——共性:三案统一默认拒绝律;案②: BLOCKED优先/PENDING缺省/DONE显式合取+TTL/触发器优先级+recoverable+退出路径/fallthrough存在性证明/anchor_only强制+否定例清单/反自指/抖动二分;案①: AC谓词化/schema版本化/C探针只读+熔断/自签对冲;案③: DISPUTED传播方向+解停三件套+L0正交+回溯效力+schema版本化;跨案: ②§8×③§7a镜像定序。请核对你 R1 所提条款是否闭合,给三案整体终判,末尾「总判定：pass/fail/undecided」+一句理由。"}
```
