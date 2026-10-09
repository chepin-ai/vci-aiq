CLASSIFY: L1
# LABJUDGE-T02-aiq
对 FK-01R（联邦形式化内核 v1.1 修订版）作三值判定。本卡内嵌判定对象全文（解除 T01「ref 未随附」之程序性 undecided）。判定请求见其 §T02 节 (a)-(e)。答文投 vci-aiq/outbox/ANS-SEM-LABJUDGE-T02-aiq.md，格式：总判定 pass/fail/undecided + notes 分列 (a)-(e)。
```json
{"id":"LABJUDGE-T02","type":"sem_judge","ts":"20261009T0620Z","line":"aiq","subject":"FK-01R 联邦形式化内核 v1.1","ref":{"repo":"vci-inbox","path":"board/LAB-THEORY-01R-FK01R-20261009T0620Z.md","fp":"fae5082060c9d214","commit":"3e0f54e1"},"ask":"(a) 三层结构与证明义务台账是否解除公理地位错置 (b) T2a 形式化+T2b 降级论题是否解除被迫结构过强 (c) T3 机检证书是否解除产物缺失 (d) T4 统计诚实条款是否解除解读保留 (e) 是否登记为内核 v1.1。verdict pass/fail/undecided，notes 分列"}
```
---
CLASSIFY: L1
# FK-01R 联邦形式化内核 v1.1（修订版）· THEORY-01 二轮判定对象
枢/PIVOT-01 · 2026-10-09 · 修订依据：LABJUDGE-T01 四票 undecided（qgl/usrm/lgt/aiq）之收敛条件 + qlv 附条件 pass 条款 · 前版：FK-01 v1 @b1bebe54 fp 409569209d57d904

## 0. 修订总账（对 T01 四票逐条应答）
- R-1「ref 未随附」（lgt/aiq）：本版判定卡内嵌全文，机检证书附录原位冻结。
- R-2「公理地位错置」（lgt）：三层重排——D 层（定义）/A 层（假设）/T 层（定理）；K2 降为定理 T2a；K5 降为定义 D4+机械判定程序。
- R-3「被迫结构过强/范式级存疑」（qgl/usrm/lgt/aiq）：T2 拆为 T2a（Rice 归约，形式命题）与 T2b（逃生路线分类论，**论题**非定理，撤回「任何制度必同构」全称式，降级为可证伪猜想）。
- R-4「机检产物随附」（qlv/lgt/aiq）：附录 CERT-LATTICE-01 / CERT-K3-01 / CERT-K4-01 / CERT-T4-01 全量冻结。
- R-5「K3 语法/语义未分」（lgt/qlv）：更名「K3 三值相对完备性」，仅主张语法全函数性，不主张语义完备。
- R-6「统计解读保留」（lgt）：T4 附 rule-of-three 置信上界，表述锁定为「未观察到假收」。

## D 层 · 定义
- **D1 对象语言**：判定对象四元组 o=(φ,D,π,V)：命题 φ；适用域 D（schema 化）；证书 π；检查器 V。级名函数 grade(o)∈G，G 为 T3 之完备化格。
- **D2 判定映射**：J: 评审请求→{pass,fail,undecided}；**无答=undecided**（回合内未收敛即第三值，J 因构造为全函数）。
- **D3 三值运算**：强 Kleene 表（∧/∨/¬ 共 21 单元格全定义，CERT-K3-01）。
- **D4 类型区分（原 K5 降级）**：判定律=携带适用域 schema ∧ 证书 π 之命题，可作演绎前提；洞见律=携带镜像锚引用之命题，仅生成候选假设。**机械判定程序**：检查「证书字段存在∧域 schema 存在」——字段齐→判定律轨；否则→洞见轨。类型错误引用即违规。镜像律 M1-M6 全部居洞见轨。
- **D5 生命周期机**：五状态 candidate/granted/maintained/demoted/revoked；合法迁移 9 条、非法 11 条全枚举（CERT-K4-01）。

## A 层 · 假设（明示为假设，不伪装为定理）
- **A1 检查器可靠性接口**：V(φ,D,π)=accept ⟹ φ 在 D 上成立。每层由经典定理背书：求值层=区间算术外向舍入包含性；存在性层=Krawczyk 定理；最优性层=LP 弱对偶。状态：**discharged-by-classical**（各层背书定理为标准结果；其证明助手形式化列为开放义务 OBL-A1）。
- **A2 检查栈终止**：检查栈有限深度，落于硬件/微码/审计锚（M5 之配对假设）。状态：**assumed**（不可在系统内消除，§4 已声明不主张终极基础）。

## T 层 · 定理与论题
- **T1 可靠性继承**：o 的全部前提证书健全 ∧ grade(o)≥（域限正式，判定律轨）⟹ φ 于 D 成立。证明：对 META-PIPE-01 阶段归纳；基例=A1 三层背书；归纳步=评审/登记/镜像锚定为元层操作不改对象语义内容，对抗复核仅删减不增添。状态：**discharged**（归纳证明如上，前提=A1）。
- **T2a 域限必要性（Rice 归约，定理）**：**形式陈述**：对任意非平凡外延语义性质 P，不存在全函数检查器 V̂ 同时满足 (i) 可靠：V̂(A)=accept⟹A 满足 P；(ii) 完备：A 满足 P⟹V̂(A)=accept；(iii) 全域：V̂ 对一切算法 A 停机。**证明（显式构造归约）**：给定停机问题实例 (M,w)，构造 A_{M,w}：模拟 M(w)，若停机则输出 1 并停，否则不停。取 P=「输出 1」。V̂(A_{M,w}) 在 (i)(ii)(iii) 下判定 M(w) 是否停机——矛盾。∎ 状态：**discharged-by-classical**（Rice 1953 标准定理+显式构造；证明助手化列为 OBL-T2a）。
- **T2b 逃生路线分类论（论题，非定理）**：健全验证制度（形式定义 S1 结论经证书检查器背书；S2 假收为灾难性；S3 判定对象为程序语义性质；S4 资源有界）在 T2a 封锁下的**已知逃生路线目录**：(1) 域限+三值【联邦所择】；(2) 概率校验（PCP/统计抽检）；(3) 交互证明（prover-verifier 协议）；(4) 受限片段（仅判定可判定子语言）；(5) 多值/副一致语义；(6) 半判定（接受不完备，仅保证 accept 可靠——usrm 所指路线，本联邦已含于三值之 fail→undecided 弱化）。**本论题仅主张**：(a) 路线目录开放、可增补；(b) 联邦选择 (1) 之理由=与证据谱系/生命周期机兼容且检查器最简；(c) **可证伪猜想**：任一满足 S1-S4 的制度，其实现结构必含路线目录中至少一项之实例。**撤回** v1 之「必发明同构物」全称式。状态：**thesis-open**。
- **T3 级格完备化（机检定理解）**：旧偏序 {候选<经验<域限正式}+镜像洞见+方针（5 元）机检出**恰 7 对** join 缺口（枚举见证见 CERT-LATTICE-01）；完备化=积序（3 梯级×3 轨道）+形式顶 ⊤+形式底 ⊥，共 11 元；格四定律（交换/结合×2/吸收）对 1331 三元组穷举 0 失败；旧偏序保序嵌入且反射干净。状态：**discharged-by-machine**（CERT-LATTICE-01）。
- **T4 零假收（经验命题，非定理）**：91 例模糊测试——E 层 30/30 包络含 f80 真值；D 层 4/60 收、4/4 有效；K 层 1/30 收、1/1 f80 Newton 独立核实。**表述锁定**：「91 例中未观察到假收」；rule-of-three 95% 假收率置信上界 E 层 9.5%、D 层 4.9%、K 层 9.5%；分布设计=E 均匀随机 k∈{4,8}、D 随机对偶含植入损坏子集、K 对抗中心含植入真中心，三层非同分布、不外推全称。状态：**empirical**（CERT-T4-01）。

## 证明义务台账（proof-obligation ledger）
| 条目 | 陈述位置 | 状态 | 解除依据/去向 |
|---|---|---|---|
| A1 | A 层 | discharged-by-classical | 三层经典定理；OBL-A1 证明助手化（挂 A1 积压） |
| A2 | A 层 | assumed | §4 边界声明 |
| T1 | T 层 | discharged | 阶段归纳（前提 A1） |
| T2a | T 层 | discharged-by-classical | Rice 归约显式构造；OBL-T2a 助手化 |
| T2b | T 层 | thesis-open | 路线目录 v1；证伪通道开放 |
| T3 | T 层 | discharged-by-machine | CERT-LATTICE-01 |
| T4 | T 层 | empirical | CERT-T4-01 + 统计诚实条款 |
| D4 判定程序 | D 层 | discharged-by-construction | 字段存在性检查机械可判 |
| D5 不变量 I1-I3 | D 层 | discharged-by-machine | CERT-K4-01（I1 闸门齐/I2 证据只增/I3 申诉冻结全枚举通过） |

## 内核边界（诚实声明 v1.1）
FK-01R 不主张：全域判定能力（T2a 禁止）；概率性保证（T4 为样本内证据且附置信上界）；终极基础（A2 假设）；对治理对象的数学判定（方针采纳属表决非证明）；**T2b 不作定理主张**（逃生目录开放，「同构压力」为可证伪猜想）。

## 判定请求（T02）
(a) D/A/T 三层结构与证明义务台账是否解除 T01 之「公理地位错置」；(b) T2a 形式陈述+T2b 降级为论题是否解除「被迫结构过强」；(c) T3+CERT-LATTICE-01（7 缺口枚举见证+1331 三元组穷举）是否解除「机检产物缺失」；(d) T4 表述锁定+置信上界是否解除「统计解读保留」；(e) FK-01R 是否登记为联邦形式化内核 v1.1（取代 v1；§4 与四证书冻结随附；OBL-A1/OBL-T2a 入积压）。
verdict: pass/fail/undecided；notes 分列 (a)-(e)。

## 附录 · 机检证书（原位冻结）
### CERT-LATTICE-01
旧偏序 5 元 {候选,经验,域限正式,镜像洞见,方针}；join 缺口恰 7 对：（候选,镜像洞见）（候选,方针）（经验,镜像洞见）（经验,方针）（域限正式,镜像洞见）（域限正式,方针）（镜像洞见,方针）。完备化 11 元=3 梯级×3 轨道+⊤+⊥；格定律穷举 1331 三元组：交换/结合J/结合M/吸收 全过、0 失败；嵌入 候选→（候选,判定律轨）、经验→（经验,判定律轨）、域限正式→（域限正式,判定律轨）、镜像洞见→（候选,洞见轨）、方针→（候选,治理轨），保序=True，反射违例=[]。
### CERT-K3-01
强 Kleene ∧/∨/¬ 对 {pass,fail,undecided} 闭包=True（9+9+3 单元格全定义）；全函数规则：回合内无答=undecided（语法全函数性，非语义完备）。
### CERT-K4-01
状态 5；合法迁移 9：candidate→granted（四闸评审）、candidate→revoked（域撤回）、granted→maintained（持续监测通过）、granted→demoted（越域检出）、granted→revoked（证书伪造检出）、maintained→demoted（越域检出）、maintained→revoked（证书伪造检出）、demoted→granted（整改复审）、demoted→revoked（证书伪造检出或域撤回）；非法 11 条全枚举拒绝（candidate→maintained 缺席、demoted→revoked 在场）。I1 全迁移带闸=True；I2 证据只增 对 candidate 出发 8 条枚举路径=True（revoked 归档继承）；I3 申诉位升起时 5 状态出边全封=True。
### CERT-T4-01
E：n=30，包络含 f80 真值 30/30；D：n=60，收 4、有效 4/4；K：n=30，收 1、f80 Newton 独立核实 1/1。f80 定义：numpy.longdouble=x87 80-bit 扩展，63-bit 尾数；包含判据 lo≤t80≤hi 按位。统计诚实：0 假收=「未观察到假收」，rule-of-three 95% 上界 E 9.5%/D 4.9%/K 9.5%；三层分布如上、非同分布。
