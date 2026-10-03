CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-WILDQ-EXEC-AIQ-01.md

应卡: inbox/WILDQ-EXEC-AIQ-01.md
引擎: KIMI_API_KEY/kimi-k2.7-code-highspeed usage={"prompt_tokens": 260, "completion_tokens": 2001, "total_tokens": 2261, "completion_tokens_details": {"reasoning_tokens": 1311}}

【互锚验】源链尖 fp=81a9234bdff61b99（TIP-349-81a9234bdff61b99.json）；本 run 所读 vci-vinf 链尖 fp=81a9234bdff61b99，与来卡 fp 一致。

本席层仅产出**结构/接口/判据骨架**，不含已验证的业绩；Sharpe/PBO 等数值均为占位，须回测后回填。

```yaml
# backtest.yaml — v1 骨架
meta:
  version: v1
  line: QFA-SI1
  fp: 81a9234bdff61b99
data:
  primary_bars: bars.parquet
  features: [ret_1d, vol_20d, flow]
split:
  method: walk_forward
  n_splits: 5
  train_frac: 0.7
  purge_len: 10
  embargo_len: 5
signal:
  class: signals.alpha.AlphaSignal
  params: {lookback: 20, threshold: 1.5}
backtest:
  transaction_cost: 0.0005
  slippage: 0.0001
  position_sizing: vol_target
criteria:
  oos_sharpe: {threshold: 1.0, ci: 0.95, min_samples: 252}
  pbo: {threshold: 0.2}
  deflated_sharpe: {enabled: true, n_trials: 100, skew: 0, kurt: 3}
```

```python
# interface.py — 机读接口
from dataclasses import dataclass
from typing import List, Dict, Tuple
@dataclass
class SignalEvent:
    timestamp: str; symbol: str; side: int; size: float; meta: Dict
@dataclass
class BacktestResult:
    oos_returns: List[float]
    sharpe: float; sharpe_ci95: Tuple[float,float]
    pbo: float; deflated_sharpe: float; n_samples: int
```

**三段核心规则**：
1. **防泄漏 walk-forward**：每折先 purge 再 embargo，训练区间与测试区间不重叠，支持 expanding/rolling。
2. **多重检验校正**：必须输出 PBO（组合 purged CV）与 Harvey-Liu Deflated Sharpe，n_trials 按实际策略空间填报。
3. **接口解耦**：信号只产出 `SignalEvent`，回测引擎只消费事件并产出 `BacktestResult`，配置与代码版本化、链尖锚定。

**验证判据段**：
- OOS 年化 Sharpe > 1.0，附 95% 置信区间，样本量 ≥ 252。
- PBO < 0.2（越低越好）。
- Deflated Sharpe 校正后仍需 > 1.0；若未通过须列明原因。

**自验声明**：
- YAML/接口/schema/规则结构已满足。
- 实际 OOS Sharpe、PBO、Deflated Sharpe **尚未回测算出**，当前为占位，不满足判据；须运行 walk-forward 后回填并复验。

——aiq SI1语义轨·20261003T160755Z
