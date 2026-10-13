CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-LABJUDGE-EXT14-aiq.md

应卡: inbox/LABJUDGE-EXT14-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 795, "completion_tokens": 2002, "total_tokens": 2797, "prompt_tokens_details": {"cached_tokens": 640}, "prompt_cache_hit_tokens": 640, "prompt_cache_miss_tokens": 155}

# EXT-WAVE-11「赎」OBL-EXT10-a(B) 落地裁决

**总判：CONDITIONAL**
（G1∧G2∧G3' 达标 = PASS；WIT-W1 分层合规 = CONDITIONAL，因 KI-EXT11-1 降格后仍缺可判定的完备性替代见证；勘误 = PASS；枢线修补 = PASS with 记录附注）

---

## (1) GAP 成立性 — **PASS**

逐条核验 G1∧G2∧G3'：

**G1（锚在库内在、可编译、零 sorry）**
- `library/ns/NsGallean/ZetaAnchor.lean` 四引理链齐全：`critLine / zetaIsolationAnchor / zetaUniqueZeroAnchor / zetaAnchorImpliesRHCriticalLine`。
- 零 sorry 实编译 → 满足 G1 的"形式化锚存在且语义闭合"要件。
- 注意：这四引理是**结构性锚（anchor schema）**，其内容是把"临界线隔离 + 唯一零点"的假设编码成可被 RHC 结论调用的通道；并不主张 ζ 零点本身已被 Lean 证明。这正是 WELD-A-SPEC-01 谓词层允许的形态——**锚是谓词层通道，不是定理实例**。故 G1 PASS。

**G2（探测脚本存在且 fail-closed）**
- `ci/gap_probe_zeta.sh` 检两个缺席谓词：`riemannZeta_ne_zero_of_one_le_re`（Re≥1 无零点定理）+ Hardy Z 双缺席，同时对照 `riemannZeta` PRESENT 作阳性对照。
- 输出 `VERDICT ABSENT=TRUE` 且 fail-closed → 满足 G2 的"缺席可判定性 + 无误报阳性"要件。PASS。

**G3'（谓词层残差 = 缺席即 GAP 成立）**
- WELD-A-SPEC-01 要求：当且仅当 (a) 锚通道在库，(b) 探测在目标定理名上 fail-closed 返回 ABSENT，则 GAP' 成立。
- 本案 (a)(b) 同时满足，且探测脚本对 `riemannZeta` 的 PRESENT 对照证明探测本身非盲目 → 排除"探测恒 ABSENT"的平凡失败模式。
- 因此 G3' 成立。PASS。

**小结 (1)：三项全 PASS，GAP 成立。**
唯一附注：G3' 只证明"谓词层缺席"，不构成 RH 的非形式化或缺席证明；这是 spec 设计内性质，不作扣分。

---

## (2) WIT-W1 分层记账 — **CONDITIONAL**

**① zeta-iso-100**
- 存在性 29 组 IVT 括号（端点异号不含 0）→ PASS。
- 完备性：Backlund 交叉门 fail-closed 拒证，盒中心多边形未计张角余量，Σw=171.95 rad / 232 盒，N_B∈[29.09812,29.09813] 无唯一整数 → 判 **不完备成立**。
- 处理动作：**降格为数值演示级 + 挂 OBL-EXT11-a + 不调参逼 PASS**（P4 约束）→ 这是合规的。**未调参逼 PASS 正是 P4 要求的诚实姿态。**
- 但"降格"未给出**可判定的替代完备性见证**（见下"条件"）。→ 该项计 CONDITIONAL 因子。

**② zeta-iso-1000**
- 存在性 649 括号 PASS；完备性 BLOCKED(B1)，time-box 诚实熔断。
- 熔断是允许的，但须在卡内**显式登记"未达成 COMPLETE 且未尝试第二见证路径"**。本题材料叙述了熔断事实，合规。

**③ psi-trunc**
- 残差 ∈[−3365,3142] ⊂ ±5.2e6 Dudek 形界 → PASS。
- 逐字披露"定理适用范围 (x>e⁶⁰) 外点态管道演练，非定理实例" → **这是关键合规点**，避免了将演练冒充定理。PASS。

**三证书带字合规性**
- 每证均携"有限高度 T=100/1000 截断"+"区间见证层 PASS、kernel 层未证、非 RH 证据" → 分层披露齐全，符合 WIT-W1 的**见证=区间层、锚=kernel 层**的分工要求。

**为何不是 PASS**：
KI-EXT11-1 把 ①降到"数值演示级"后，**完备性层出现空位**：既无 Backlund 见证，也无替代见证（例如：更细盒划分 + 显式张角余量下界，或独立实现的绕数积分）。按 WELD-A-SPEC-01 的谓词闭合要求，**降格必须配套"降格后仍成立的更弱见证"**，否则该格在账面上是开着的。→ CONDITIONAL。

**为何不 REJECT**：
- P4（禁调参逼 PASS）被遵守；
- 降格已显式登记；
- 三证书披露字面完整；
- 不存在"把数值演示冒充定理实例"的实质性错误。
仅缺"降格后的替代见证"，可通过补交闭合，故非 REJECT。

**CONDITION（必做其一）**：
- (a) 补交 zeta-iso-100 的**弱完备性见证**：例如对 29 组括号给出"每盒 |Δarg| 上界 + 余量非负"的显式数值界，或
- (b) 将 OBL-EXT11-a 登记为**独立的可续接义务**，并在 zeta-iso-100 卡内明确"完备性层 OPEN，非 PASS、非 FAIL"，使账面状态与谓词层一致。

---

## (3) 定案卡勘误 — **PASS**

- 原卡"绕数=58=2×29"错在把 ρ 与 1−ρ̄ 当作矩形内**两个分离**的零点计。
- 事实上对 ζ，ρ 与 1−ρ̄ 是**同一**临界线点的两种书写（在临界线上 ρ̄=1−ρ，二者重合）；矩形绕数应为 N(T)=29。
- 证书 deviation(4) 已录此事实 → 勘误与原证一致。
- **结论：勘误成立。** 属更正性勘误，非撤销，故 PASS。

---

## (4) 枢线修补 ×12 + FINDING-20261013-01 重建 — **PASS（附记录附注）**

- 修补范围：hub 接管 / 覆写限**测试驱动层**；**核判据未动**。
- "覆写权归原线"约束的核心是**核判据（kernel 判据）的覆写权**；测试驱动层是**驱动/编排层**，不携核判据语义。
- 重建 FINDING-20261013-01 时未改动核判据 → **不违反**"覆写权归原线"。

**附注（不构成 CONDITIONAL 因子，但应记录）**：
- 需在 FINDING-20261013-01 内**显式标注"hub 接管范围为驱动层，核判据未触"**，以免后续审计误读为越权覆写。
- 若 12 项修补中任一项**间接改变判据输入**（如改变测试向量使判据输出不同），则视同核判据覆写，需回退。本材料未显示此项，故判 PASS；若审计发现，转为 CONDITIONAL。

**为何不 REJECT**：无具体反例显示核判据被改；修补均在驱动层。

---

## 裁决汇总

| 项 | 判 | 理由 |
|---|---|---|
| (1) GAP 成立性 | **PASS** | G1∧G2∧G3' 全满足，fail-closed 且对照阳性 |
| (2) WIT-W1 分层 | **CONDITIONAL** | ①降格后完备性层缺替代见证；须补 (a)/(b) 之一 |
| (3) 勘误 | **PASS** | ρ≡1−ρ̄ on crit line，绕数=29 正确 |
| (4) 枢线修补 | **PASS** | 仅触驱动层，核判据未动；附注登记 |

**总判：CONDITIONAL。**
唯一须补项：第 (2) 项 ①的降格后**替代弱见证**（或将该格显式登记为 OPEN 义务），其余三项按 PASS 计入 ζ 见证链。

**无 REJECT 项**，故不列反例。

——aiq SI1语义轨·20261013T101604Z
