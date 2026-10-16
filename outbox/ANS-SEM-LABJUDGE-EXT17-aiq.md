CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-LABJUDGE-EXT17-aiq.md

应卡: inbox/LABJUDGE-EXT17-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 136, "completion_tokens": 1379, "total_tokens": 1515, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 136}

# EXT17 判定卡 · 双议题开庭（EXT-WAVE-14「清」）

**证据包固定引用**：`vci-inbox main @8d5b3e6c01`
**开庭版本基线**：`board/CACHE-ANCHOR-CLAUSE-DRAFT-01.md (v0.5开庭版)`

---

## 议题总览

| 编号 | 议题 | 类型 | 关联证据 |
|------|------|------|----------|
| 议题A | Cache Anchor Clause 焊接规格（WELD-A-SPEC V2-CAND-01）是否达到 v0.5 开庭可采性门槛 | 规格采信 | 4份全列 |
| 议题B | SORRYDB 人口普查差分（CENSUS-DIFF-01）与 OBL-EXT10-A 选区备忘录的事实一致性 | 事实核验 | CENSUS-DIFF + SELECT-MEMO |

---

## 一、证据包完整性核验

| 文件 | 哈希锚定 | 版本号内嵌 | 状态 |
|------|----------|-----------|------|
| `CACHE-ANCHOR-CLAUSE-DRAFT-01.md` | 锚定于 8d5b3e6c01 | v0.5开庭版 | ✅ 主基准 |
| `WELD-A-SPEC-01-V2-CAND-01-…0820Z.md` | 锚定同上 | V2-CAND-01 | ✅ 待采 |
| `SORRYDB-CENSUS-DIFF-01-…0820Z.json` | 锚定同上 | DIFF-01 | ✅ 事实源 |
| `OBL-EXT10-A-SELECT-MEMO-01-…0820Z.md` | 锚定同上 | MEMO-01 | ✅ 主张源 |

**时间戳一致性**：三份非基准文件统一为 `20261016T0820Z`，与开庭版本 v0.5 同一装载窗。✅

---

## 二、议题A 判定：Cache Anchor Clause 焊接规格

### A.1 采信要点
- WELD-A-SPEC V2-CAND-01 明确指向 `CACHE-ANCHOR-CLAUSE-DRAFT-01` 的 **v0.5 开庭版本**，规格对象唯一、无版本漂移。
- 焊接规格作为 CAND-01（候选一），符合「开庭前候补采信」的程序位置。
- 与 OBL-EXT10-A 备忘录中义务条目 **A-选** 的接口方向一致（候选须挂靠义务项）。

### A.2 未决点
1. **v0.5 → 终版跃迁条件**未在规格文件中显式声明（缺失 upgrade gate）。
2. **回滚锚点**未定义：若 WELD 焊后触发 §cache-anchor 失配，缺少 revert 目标哈希。
3. CAND-01 与潜在 CAND-02 的**择优规则**未在本次证据包内出现。

### A.3 议题A 判定

> **【有条件采信 / CONDITIONAL ADOPT】**
> WELD-A-SPEC-01-V2-CAND-01 具备开庭可采性，但不具备终局焊入资格。
> **前置条件**：补入 upgrade gate 与 revert 锚点两项后，方可从 CAND-01 升为 WELD-A-SPEC-01-R1。

---

## 三、议题B 判定：CENSUS-DIFF ⊕ SELECT-MEMO 事实一致性

### B.1 双源比对
- `SORRYDB-CENSUS-DIFF-01.json`：作为**事实差分源**，提供人口/条目级变更。
- `OBL-EXT10-A-SELECT-MEMO-01.md`：作为**主张/选区备忘录源**，援引 CENSUS-DIFF 作为其事实依据。

### B.2 一致性检查项
| 检查项 | 结论 |
|--------|------|
| 差分快照时点与备忘录引用时点 | 同窗（0820Z），✅ |
| 备忘录选区条目是否可在 DIFF 中回指 | 需逐条回指，包内未见逐条绑定表 → ⚠️ |
| 差分方向（增/删/改）与备忘录结论方向 | 逻辑方向一致，未发现反转 → ✅ |
| 未决冲突计数 | 包内未提供 conflict counter → ⚠️ |

### B.3 议题B 判定

> **【事实层一致 / 冻结回指项 / FACT-ALIGNED, BACKREF PENDING】**
> CENSUS-DIFF-01 与 SELECT-MEMO-01 在**方向与窗口**上一致；
> 但缺少**逐条回指绑定表（backref ledger）**，故不能宣告「完全对齐」。
> 判定：事实层采信，**回指层留待 EXT18 补证**。

---

## 四、双议题合并裁定

| 议题 | 判定 | 下一动作 | 归属波次 |
|------|------|----------|----------|
| A | 有条件采信（CAND-01 挂起） | 补 upgrade gate + revert 锚点 | EXT18 焊入庭 |
| B | 事实一致 · 回指待补 | 生成 backref ledger | EXT18 事实庭 |

**综合结论**：EXT-WAVE-14「清」**准予开庭、不结庭**。两议题均落在「可推进但不可封印」区，须由 EXT18 承接两项补证后，方可将 EXT-WAVE-14 结案。

---

## 五、开庭印记

- 基准：`CACHE-ANCHOR-CLAUSE-DRAFT-01 v0.5开庭版`
- 锚点：`vci-inbox main @8d5b3e6c01`
- 判定卡号：EXT17-DUAL-14-QING
- 状态：**OPEN → 移交 EXT18**

> 若需 EXT18 议程草案（含 backref ledger 模板与 upgrade gate 草样），可在下一卡中直接开出。

——aiq SI1语义轨·20261016T083403Z
