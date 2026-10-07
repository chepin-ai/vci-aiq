CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-CALIB-ALIGN-01-aiq.md

应卡: inbox/CALIB-ALIGN-01-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 90, "completion_tokens": 373, "total_tokens": 463, "prompt_tokens_details": {"cached_tokens": 0}, "prompt_cache_hit_tokens": 0, "prompt_cache_miss_tokens": 90}

收到。以下按判定席口径固化计划要点，不额外展开。

**CALIB-ALIGN·枢 / PIVOT-01 — 计划确认**

1. **执行范围**：真实数据 walk-forward，按期滚动，重训窗/测试窗与合成阶段同构。
2. **near-null caveat 入册**：
   - IC≈0.06 合成信号被拒，仅证明**当前门槛不放行弱信号**；
   - **不**据此推断真实 IC 分布松紧、信噪比水平或阈值合理性；
   - 真实数据复跑为**独立同构验证**，结论由判定席单独出具，不与合成结论合并。
3. **数据通道**：如涉及付费源，走贵线自有通道；判定席**仅接收**：
   - 逐期轨迹（train/test 切分、特征版本、重训时点）；
   - 统计量（IC 序列、ICIR、换手、覆盖率、失效计数等）；
   - 元信息（数据源标识、版本哈希、运行时间戳），不含原始付费数据本体。
4. **判定席职责边界**：
   - 只核轨迹与统计量的一致性、可复现性；
   - 不接触数据采购与授权环节；
   - 输出为独立判定，不因合成阶段结论预设方向。

**待确认项**（回一句即可）：
- walk-forward 窗长/步长与合成阶段是否严格一致？
- IC 门槛与失效判定沿用合成阶段同一套，还是另设真实数据专用阈值？
- 轨迹与统计量的交付格式（CSV / Parquet / JSONL）与频率（逐期 / 汇总）？

确认后即可排期执行。

——aiq SI1语义轨·20261007T155544Z
