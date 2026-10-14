CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-LABJUDGE-EXT15-R3-aiq.md

应卡: inbox/LABJUDGE-EXT15-R3-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 718, "completion_tokens": 796, "total_tokens": 1514, "prompt_tokens_details": {"cached_tokens": 512}, "prompt_cache_hit_tokens": 512, "prompt_cache_miss_tokens": 206}

PASS

**判定依据（EXT15-R3 终投，议题：WS-63 ζ 见证包 OBL-EXT11-a 关闭 / Backlund 门严格化）**

一、证书层（zeta-iso-100 v1.1.1）
- N_B 区间 [28.9999999999999999958558652436, 29.000000000000000004418444223] 宽 8.56258e-18，ceil(lo)=floor(hi)=29，唯一整数窗成立，Backlund 门（N_B 必须恰为 29）被严格闭合。
- completeness.backlund 必填字段 nB_interval / width_budget / branch_exclusion_28_30 已按 qfa R2 修订项③逐字落实。
- 宽度预算闭包 w_NB=(w_θ+w_Δarg+w_wrap)/π=(2.69001e-17+8.96721e-84+0)/π=8.56258e-18，与证书区间宽度精确相等；各项 w_θ/w_Δarg/w_wrap/w_round 及传递公式在册，无隐藏加项。

二、枢线层（ci 修补 #18/#19）
- verify 双查 backlund_cert_nB_interval_match / width_budget_match，fail-closed，缺字段即拒证，杜绝“字段缺席即默认通过”的软通道。
- gen 同款复算 + 诚实门，与 verify 对称；test 第 45 项 test_backlund_cert_fields 覆盖该门。
- resign_v111 双跑字节一致；gen --emit-raw 全量与三证逐字节相同；pytest 45/45（3338.17s），无 flaky 迹象。证据链可复现。

三、独立复算层（SUP-01 / SUP-02）
- SUP-01：769 结点均匀网格复算得同区间；232 段张角 max 0.876<π 余量≥2.265；锚点辐角宽 3.77e-153，数值裕度充足。
- SUP-02：EM 独立腿（Euler-Maclaurin N=1000 dps=80，算法独立于 CVZ 主路）输出 N_B∈[28.9999999999999999877574324241, 29.0000000000000000124773520971] 宽 2.47e-17，唯一 29，且与 CVZ 区间相交（修订项①落实）。
- 共享假设已申报（仅 θ 解析余项 + iv 内核），非共享部分独立；两条路径给出同一整数窗，交叉印证成立（修订项②落实）。

四、纪律与边界
- 有限高度 T=100/1000 截断明示；区间见证层 PASS、kernel 层未证；隔离区间内区间见证 PASS，非全域声明；非 RH 证据。所有限定语与 qfa R1/R2 要求逐字一致，未见越界声明。

五、缺口核查
- 无未闭合的必填字段；无 fail-open 分支；无区间宽度预算不匹配；无独立腿与主路区间不相交的反例；无字节漂移或测试缺口。R1 十卡 PASS / qfa REVISE → SUP-01 → qfa R2 REVISE → SUP-02 → v1.1.1 证据包链路中三项修订（独立腿、宽度预算闭包、必填字段）均已逐字落实，无遗留项。

结论：OBL-EXT11-a 关闭判定 **PASS**。

——aiq SI1语义轨·20261014T064214Z
