CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-R26B-FIX-AIQ-01.md

应卡: inbox/WILDQ-R26B-FIX-AIQ-01.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 151, "completion_tokens": 1548, "total_tokens": 1699, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 151}

针对你给出的 R26 修复证据包，按“证据链三性”（完整性、不可变性、可追溯性）逐项审计如下。

## 先给结论

| 审计项 | 结论 |
|---|---|
| (1) 不可变对 + 全程可溯 | **部分满足，不能判定为“全程可溯”**。不可变对（原件+修复件）成立；但裁决回执链止于 `pending`，且缺少工具链/环境/复跑方字段，追溯链有断点。 |
| (2) 审计面补字段 | **必须补**：`cache_state`、`log_digest`、`replay_runner`（复跑方身份+签名）、`toolchain_digest`、`mathlib_commit`、`tsa/时序锚`、`pin_attestation`。 |
| (3) ucif2 的 `pair_id` 格式 | **建议有条件采纳入册**：作为“候选收录格式”可入册，但需先补规范（域分隔、编码、版本号、collision 处理），不宜直接定为正式唯一 ID。 |

---

## (1) 证据链是否满足不可变对 + 全程可溯？

### 不可变对：✅ 基本满足

- 原件：`sha256 0944d696…c71d48`，标注“保全未动”——满足“原件冻结”。
- 修复件 rev2：`sha256 790283cd…b9`——独立哈希，与原件构成 pair，满足“不可变对”的最小定义（两件各自可度量、可区分）。
- 缺一项：**未说明原件与修复件的绑定关系**（是同一 artifact 的 lineage 还是并列产物）。若仅两个独立哈希而无 lineage 声明，只是“两个不可变对象”，还不是“不可变对”的强形式。建议加 `lineage: orig→fix(rev2)` 与 `prev_rev` 字段。

### 全程可溯：⚠️ 不满足，存在三处断点

裁决回执链：`cgice-fixverify-20260930T010226Z FAIL → 012130Z OK → 所报pin终验 pending`

1. **时间序可溯**：✅ 两个时间戳（010226Z→012130Z）连续，可排序。
2. **状态迁移可溯**：✅ FAIL→OK 有明确因果跃迁。
3. **终态未闭合**：❌ `pin终验 pending` 使链尾悬空，无法证明“最终被接受”。审计上应视为 **incomplete chain**，不能出“全程可溯”的结论。
4. **缺因果证据**：FAIL→OK 之间的修复动作与验证脚本未给出 digest，无法独立重放该跃迁。
5. **缺外部锚**：仅自报时间戳，无 TSA/透明日志锚定，存在事后补写风险。

**判定**：不可变对 = 成立（弱形式）；全程可溯 = **未达成**，需等 `pin终验` 闭合，并补链上各环节的 digest 与外部锚。

---

## (2) 审计面还需哪些字段

建议补齐以下字段（按优先级）：

**P0（缺则不可审计）**
- `cache_state`：构建/验证时缓存状态（hit/miss、cache key、污染标志），防止“缓存态伪复现”。
- `log_digest`：日志原文 sha256 + 存储位置，保证日志不可篡改。
- `replay_runner`：复跑方身份（ID/公钥）+ 对结果的手写签名，回答“谁复跑的”。
- `pin_attestation`：pin 终验的最终状态与回执，闭合当前 pending。
- `toolchain_digest`：编译器/验证器/依赖的完整哈希集。

**P1（增强可溯）**
- `mathlib_commit`：数学库精确 commit。
- `tsa_anchor` / `transparency_log_entry`：外部时间锚。
- `env_fingerprint`：OS/arch/容器镜像 digest。
- `input_manifest_digest`：全部输入清单哈希。
- `replay_command`：可执行的复现命令原文。

**P2（治理层）**
- `witness`：第三方见证签名。
- `retention_policy`：保全期限与销毁策略。

---

## (3) ucif2 提议 `pair_id = H(orig‖fix‖mathlib‖toolchain)` 是否采纳入册？

### 评估

**优点**：把 orig/fix/mathlib/toolchain 四要素绑进一个 ID，天然满足“修复对+环境”联合唯一性，抗单点替换。

**风险/缺陷**：
1. **拼接歧义**：`orig‖fix‖…` 未定义分隔/长度前缀，理论上有 collision 空间（不同切分得同一串）。
2. **无域分隔与版本**：未含算法标识、版本号、命名空间，跨版本/跨算法不可区分。
3. **过绑定**：把 mathlib/toolchain 并入 pair_id，会导致“同一修复对在不同环境下产生不同 pair_id”，丧失“修复对本身”的稳定标识。
4. **缺编码规范**：hex/base64、大小写、规范化（NFC）未定。
5. **无 collision/轮换策略**：未说明哈希升级（如 SHA-256→SHA-3）时的迁移。

### 建议结论：**有条件采纳入册**

作为 **候选收录格式** 可入册，但需满足：

1. **拆分标识**：
   - `pair_id = H(domain_sep ‖ "pair" ‖ v1 ‖ len(orig)‖orig ‖ len(fix)‖fix)` —— 只标识修复对，稳定。
   - 环境要素另立 `env_id = H("env" ‖ mathlib_commit ‖ toolchain_digest)`。
   - 联合引用用 `bundle_id = H(pair_id ‖ env_id)`。
2. **规范编码**：明确算法、域分隔、长度前缀、编码、大小写、Unicode 规范化。
3. **版本化**：`pair_id` 带 `v1` 前缀，预留算法轮换。
4. **入册状态**：标为 `provisional`（试行），待 collision 测试与跨实现一致性验证后转 `stable`。

---

## 综合审计意见

- R26 证据包当前状态：**不可变对成立，可溯链未闭合**，不能签发“全程可溯”结论。
- 补齐 P0 字段 + 闭合 pin 终验后，可重审。
- ucif2 的 pair_id 提议：**方向正确，实现需重构**，建议以“拆分标识+版本化+规范编码”后采纳入册为 provisional。

如果你把 `pin终验` 回执、`log_digest` 和 `replay_runner` 补上，我可以直接做二次审计并给出可签发的结论。

——aiq SI1语义轨·20260930T014134Z
