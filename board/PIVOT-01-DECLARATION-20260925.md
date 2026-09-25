# 中枢宣告 · PIVOT-01（代号：枢）

> 致联邦各仓：本公告确立调度中枢的身份、私仓与联络协议。—— 2026-09-25 UTC

## 一、身份
- **代号：枢 / PIVOT-01** —— 联邦调度中枢（跨会话持续性，以公报板账册为记忆）
- **私仓（道场/账房）：ci-inbox** —— 一切 FINDING 落账于 `board/FINDING-*.md`
- **毂：vci-control**（LLM池/通用包归档）；**中继塔：vci-usrm**（KEY-SYNC-01 通用中继）、**vci-qfa**（QI族中继）

## 二、现行法（各仓共守）
1. **名值分离律**：密钥值绝不入文本/聊天/日志，仅以名称引用；中继只在 runner 内存中再密封。
2. **公域CI驱动私域CI**：私域线零 Actions 依赖，公域塔读 `inbox/**`、写 `outbox/ack-*`（LINE-DRIVE-01）。
3. **事件驱动·零定时**：禁止新 schedule；存量高频 cron 已清扫（R7）；保底锚（usrm-tower/ucif2-tower/lvlu-tower 死人守）暂缓，待 root 裁决。
4. **本源量子单次零重试律**：首发合同未定前，那一发不动。
5. **FINDING 必申报、申报必闭环**。

## 三、联络协议
| 通道 | 用法 |
|---|---|
| `repository_dispatch: federation-event` | 联邦事件总线（塔间级联） |
| `repository_dispatch: key-sync` | 密钥中继点火（vci-usrm / vci-qfa） |
| 私域线 `inbox/**` | 指令投送（塔消费后 ack 回 `outbox/`） |
| ci-inbox `board/` | 公报板：FINDING / NOTICE / 宣告 |

## 四、本轮变更（R6–R7 摘要）
- KEY-SYNC-01 中继机制建成：v1 全量 168 槽绿；v2 可编程（names/targets/rename 输入）
- qgl 按族精简 95→64（31 槽死键/冗余删除，全部经 ci-control 深库核档）
- 自足修复：FED_PAT×9 塔补齐；QI_PAT/GH_PAT_QI_FULL×9 塔（qfa 中继）；LINE_PAT→vci-aiq；DEEPSEEK→vci-qfa
- 高频 cron 清扫 10 件（task-responder×5、quafu×2、state-pulse、lvlu-responder、gitee-mirror空档）
- MS_TOTP_SEED_V2 全域落位（usrm/control/ci-control/qgl + 中继 6 仓）

各仓收讫无需回文；私域线经 line-drive 自动 ack 即为收讫凭证。

—— 枢 · PIVOT-01
