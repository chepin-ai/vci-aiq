CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-MONOTONE-01-aiq.md

应卡: inbox/WILDQ-MONOTONE-01-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 394, "completion_tokens": 1897, "total_tokens": 2291, "prompt_tokens_details": {"cached_tokens": 256}, "prompt_cache_hit_tokens": 256, "prompt_cache_miss_tokens": 138}

题面混了两层东西：**枢案 M 是“治理健康度/待闭环度”的全局量，不是“可升级刚性态”的充要判据**。因此我直接给两答。

---

## A) 线-local 单调量 \(M_{\text{line}}\)

对你们这种“线”结构，比全局 \(M(W)\) 更合适的是按**升级路径上的闭环义务**来取局部量。设一条线 \(\ell\) 在当前版本态 \(v\) 上有：

- \(U_\ell\)：本线尚未裁定的 undecided 项数
- \(F_\ell\)：fail-open 事件数
- \(O_\ell\)：未闭环 FINDING 数
- \(N_\ell\)：无 fp 卡件数
- \(A_\ell\)：非自包含 ask 数

则可定义

\[
M_\ell(v)
=
\alpha_\ell |U_\ell|
+\beta_\ell |F_\ell|
+\gamma_\ell |O_\ell|
+\delta_\ell |N_\ell|
+\varepsilon_\ell |A_\ell|
+\zeta_\ell |D_\ell|
\]

其中建议新增一项：

\[
D_\ell=\text{依赖未刚性上游线的数量}
\]

因为线-local 的“刚性能否升”不只取决于本线自清，还取决于所依赖上游是否已经可升。

### 沿什么参数单调？

沿**版本推进参数** \(t\) 单调：从 \(v1\text{-draft}\to v1\to v1.1\to\cdots\)。

若每轮满足：

1. undecided 只减不增；
2. fail-open 事件入册且不重开；
3. FINDING 一旦闭环不取消；
4. fp 卡件一旦补上不删；
5. ask 一旦自包含化不回退；
6. 依赖上游只从“未刚性”变为“刚性”，不逆向；

则

\[
M_\ell(t+1)\le M_\ell(t)
\]

即线-local 单调非增。这就是枢案 M1 的线-local 版本。

### 等号集

\[
M_\ell=0
\]

的含义是：

- 本线无 undecided；
- 无 fail-open 未处理；
- 无未闭环 FINDING；
- 无无 fp 卡件；
- 无非自包含 ask；
- 无未刚性上游依赖。

但注意：**\(M_\ell=0\) 只是刚性升级的必要条件候选，不是充分条件**。还要加同行评审双轮律、级名不滥闸门、以及可复现性/自包含证据。因此线-local 的刚性等号应写成：

\[
\text{Rigid}(\ell)
\iff
M_\ell=0
\;\wedge\;
\text{PeerReview2}(\ell)
\;\wedge\;
\text{NameGate}(\ell)
\;\wedge\;
\text{Repro}(\ell)
\]

若要把等号压成一个量，可定义

\[
M_{\ell,\text{rigid}}
=
M_\ell
+
\lambda\cdot \mathbf{1}[\neg \text{PeerReview2}]
+
\mu\cdot \mathbf{1}[\neg \text{NameGate}]
+
\nu\cdot \mathbf{1}[\neg \text{Repro}]
\]

则

\[
M_{\ell,\text{rigid}}=0 \iff \text{可升级刚性态}
\]

### 与枢案 M 的关系

- **子项关系**：全局 \(M(W)\) 可视为各线 \(M_\ell\) 的聚合，但还多出跨线耦合项，如依赖冲突、全局命名冲突、跨线 FINDING 未闭环。
- **独立关系**：线-local \(M_\ell\) 可以为零，而全局 \(M(W)>0\)，因为别的线未闭环。
- **反例关系**：全局 \(M(W)=0\) 不一定推出某线可升，因为该线可能缺同行评审或依赖上游未刚性；反过来，某线 \(M_\ell=0\) 也不保证全局 \(M=0\)。

所以关系应写成：

\[
M(W)
=
\sum_\ell w_\ell M_\ell
+
C_{\text{cross}}
+
G_{\text{global}}
\]

其中 \(C_{\text{cross}}\) 是跨线未闭环耦合，\(G_{\text{global}}\) 是全局闸门项。

---

## B) 对枢案 M 的反例或修正

有。枢案 M 作为“待闭环度”是合理的，但作为“刚性升级判据”不够。

### 反例 1：\(M=0\) 但不可升级

构造：

- 所有 undecided = 0；
- fail-open = 0；
- 未闭环 FINDING = 0；
- 无 fp 卡件 = 0；
- 非自包含 ask = 0；

但：

- 同行评审只过了一轮，未满足双轮律；
- 或级名闸门未过；
- 或关键产物不可复现；
- 或依赖的上游线仍是 v1-draft。

此时

\[
M=0
\]

但不可升级。  
所以枢案 M 缺少**评审轮次项、级名闸门项、可复现项、上游刚性依赖项**。

### 反例 2：\(M>0\) 但已刚性

构造：

- 某线已通过双轮评审、级名闸门、可复现验证；
- 上游依赖也已刚性；
- 但存在一个历史 fail-open 事件，已处理、已入册、已闭环，只是计入 \(M\) 的“fail-open事件”项未区分“已闭环/未闭环”；
- 或存在一个无 fp 卡件的旧项，但该旧项已明确标记为不阻塞升级。

若 \(M\) 把“历史发生但已闭环”的 fail-open 仍计入正值，则会出现

\[
M>0
\]

但实际已刚性。

所以枢案 M 的项必须区分为：

- 未闭环 fail-open；
- 已闭环但留痕 fail-open；
- 阻塞性无 fp；
- 非阻塞性无 fp；
- 阻塞性 ask；
- 非阻塞性 ask。

否则 M 会把“审计痕迹”误算成“升级阻塞”。

### 修正建议

把枢案 M 改为：

\[
M(W)
=
\alpha |U|
+
\beta |F_{\text{open}}|
+
\gamma |O_{\text{open}}|
+
\delta |N_{\text{block}}|
+
\varepsilon |A_{\text{block}}|
+
\zeta |D_{\text{nonrigid}}|
+
\eta |R_{\text{missing}}|
+
\theta |G_{\text{name}}|
+
\iota |P_{\text{repro}}|
\]

其中：

- \(F_{\text{open}}\)：未闭环 fail-open；
- \(O_{\text{open}}\)：未闭环 FINDING；
- \(N_{\text{block}}\)：阻塞性无 fp；
- \(A_{\text{block}}\)：阻塞性非自包含 ask；
- \(D_{\text{nonrigid}}\)：未刚性上游依赖；
- \(R_{\text{missing}}\)：评审轮次不足；
- \(G_{\text{name}}\)：级名闸门未过；
- \(P_{\text{repro}}\)：可复现证据缺失。

然后定义刚性判据：

\[
\text{Rigid}(W)
\iff
M(W)=0
\;\wedge\;
\text{PeerReview2}
\;\wedge\;
\text{NameGate}
\;\wedge\;
\text{Repro}
\]

或者直接把后三项并入 \(M\)，使

\[
M_{\text{rigid}}(W)=0 \iff \text{可升级刚性态}
\]

### 结论

枢案 v0 的 \(M\) 可作为**波次单调的待闭环度**，M1/M2 在“只增不减闭环”条件下成立。  
但若要把 M2 写成“\(M_{\text{line}}=0 \iff\) 可升级刚性态”，必须补：

1. 评审双轮项；
2. 级名闸门项；
3. 可复现项；
4. 上游刚性依赖项；
5. 阻塞/非阻塞区分。

否则会出现：

- \(M=0\) 但不可升级；
- \(M>0\) 但已刚性。

修正后的单调量应叫：

\[
M_{\text{rigid}}
\]

而不是原枢案 \(M\)。原 \(M\) 保留为“未闭环度/健康度”，\(M_{\text{rigid}}\) 才承担刚性升级的充要判据。

——aiq SI1语义轨·20261007T153322Z
