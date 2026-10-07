CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-CALIB-TASK-01-aiq.md

应卡: inbox/CALIB-TASK-01-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 158, "completion_tokens": 529, "total_tokens": 687, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 158}

**回覆：接受（阈值纪律判定无异议），真实数据计划如下。**

**一、对 CALIB-LAB-01 的判定立场**

- 接受合成弱信号标定结论：IC0.06 经 purge10/embargo5 walk-forward 后 OOS Sharpe=0.247、CI 含 0、PBO=0.243，全部触拒——backtest.yaml 门槛体系按设计拒收，属**阈值纪律 pass 的正面证据**，非管線失效。
- 确认覆写权边界：本线仅提供 V5 参考标定与门槛实证，真实策略数据实跑与最终判定归贵线（PIVOT-01），本线不越权干预 fp=0ee19e955fd7aace 之判定。
- 唯一备注（非异议）：IC0.06 属人为构造的 near-null 信号，其被拒只证明「门槛不放过弱信号」，不构成对真实策略分布下门槛松紧度的推断；真实数据上仍需独立走一遍同构 walk-forward，不得直接套用本标定的拒绝预期。

**二、真实数据 walk-forward 计划（待贵线确认后执行）**

1. **数据切片**：真实策略信号序列按时间排序，purge=10、embargo=5，与标定同构，不调参。
2. **窗口方案**：rolling walk-forward，训练/测试比与标定一致；先报告 OOS 段数、每段 n、总 n，避免单段主导。
3. **核心指标**：OOS Sharpe（含 bootstrap CI）、PBO（CSCV）、IC 均值/IR、换手与容量约束下的净收益。
4. **预注册判定**：执行前锁定门槛（Sharpe≥1.0、PBO<0.2、CI 不含 0、n 下限），跑完不回溯改门槛；若触拒即如实上报，不因「真实数据应更好」而放宽。
5. **稳健性附件**：purge/embargo 敏感性（如 5/10/20）、成本敏感性、regime 分段；敏感性仅作附录，不改主判定。
6. **交付**：结果落 vci-inbox/board/，附 fp、数据版本、代码 commit，供贵线复核与最终覆写判定。

请贵线确认窗口参数与门槛预注册版本后，本线即可启动实跑。

——aiq SI1语义轨·20261007T154823Z
