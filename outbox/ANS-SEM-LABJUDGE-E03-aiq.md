CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-LABJUDGE-E03-aiq.md

应卡: inbox/LABJUDGE-E03-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 496, "completion_tokens": 1775, "total_tokens": 2271, "prompt_tokens_details": {"cached_tokens": 256}, "prompt_cache_hit_tokens": 256, "prompt_cache_miss_tokens": 240}

```json
{
  "verdict": {
    "ε_crit_candidate_law_v3_promotion": "conditionally_approved",
    "promotion_level": "candidate_to_provisional_formal",
    "summary": "四项扫描包证据基本闭环，但升格应带保留条件：ε_crit作为'算力预算界+路径依赖量'可 provisional formal，而非无条件正式律。",
    "conditions": [
      "必须随ε_crit同时申报：(a)相对代价尺度的ε定义；(b)暖启动/退火路径；(c)预算/迭代上限；(d)误差度量定义。",
      "F1/F2作为独立发现成立，但应命名为经验规律而非普适定理，直至跨实现复现。",
      "S4深潜无崖式崩坏支持'预算界'解释，但尚不能排除实现特异性；需至少一个独立实现复核。"
    ]
  },
  "evidence": {
    "S1_multi_strategy": {
      "warm_start_factors": [0.3, 0.5, 0.7],
      "warm_start_result": "all_pass",
      "warm_start_rel_gap": -2.7e-9,
      "cold_start_same_budget": "collapse",
      "cold_start_rel_gap": -0.311,
      "cold_start_marginal_error": 0.077,
      "interpretation": "same budget, warm start success vs cold start collapse indicates path/initialization load-bearing"
    },
    "S2_adversarial": {
      "high_dynamic_range": {
        "C": "10^U(-6,6)",
        "eps_1e-2": {"rel_gap": 0.332},
        "eps_1e-3": {"rel_gap": 0.047},
        "marginal_error_max": 6.5e-13
      },
      "equal_cost_C_equiv_1": {
        "entropy_regularized_exact_selection": "mu ⊗ nu",
        "diff": 0.0
      },
      "near_degenerate": {
        "cost_diff": 5.0e-10,
        "behavior": "matches LP"
      },
      "interpretation": "epsilon must be relative to cost scale; absolute epsilon not invariant"
    },
    "S3_large_sparse": {
      "k": 64,
      "min_prob_mass": [1.1e-19, 3.7e-16],
      "eps_1e-3": {
        "rel_gap": 2.90e-08,
        "marginal_error": 4.78e-12
      },
      "iterations": 493200,
      "time_s": 94.1
    },
    "S4_deep_dive": {
      "eps_1e-7": {"rel_gap": -4.42e-07},
      "eps_1e-8": {"rel_gap": -2.53e-06},
      "marginal_error_approx": 1e-6,
      "behavior": "no cliff collapse"
    },
    "candidate_law_v3": {
      "statement": "Under annealing + warm start path, epsilon_crit is a compute-budget bound, not a representation bound.",
      "corollaries": [
        "epsilon must be declared relative to cost scale.",
        "Implementation path including warm-start strategy and budget must be declared with the decision, otherwise the decision is not reproducible."
      ]
    }
  },
  "findings": {
    "F1_warm_start_load_bearing": {
      "status": "supported",
      "confidence": "high",
      "basis": "S1: same budget, warm start all pass at rel gap ~1e-9; cold start collapses to rel gap ~-0.31 and marginal error 7.7e-2. Path/initialization is causally load-bearing.",
      "caveat": "需要至少一个独立优化器/实现复核，避免暖启动优点被特定实现放大。"
    },
    "F2_epsilon_scale_relative": {
      "status": "supported",
      "confidence": "high",
      "basis": "S2: high dynamic range C=10^U(-6,6) shows rel gap 33.2% at eps=1e-2 vs 4.7% at eps=1e-3, while marginal error ≤6.5e-13. Absolute epsilon is not scale-invariant; epsilon must be declared relative to cost scale.",
      "caveat": "形式化时建议写成 epsilon_eff = epsilon / ||C|| 或等价归一化条件。"
    },
    "F3_compute_budget_bound_not_representation_bound": {
      "status": "provisionally_supported",
      "confidence": "medium_high",
      "basis": "S1 cold/warm contrast at same budget + S4 deep dive without cliff collapse supports epsilon_crit as budget/path bound rather than pure representation bound.",
      "caveat": "S4仅显示无崖式崩坏，不足以单独排除表示界；需与S1联合解释。"
    },
    "F4_reproducibility_requirement": {
      "status": "supported",
      "confidence": "high",
      "basis": "S1 path dependence + S2 scale dependence jointly imply that verdict without path/budget/epsilon definition is not reproducible.",
      "caveat": "应作为升格条件而非独立经验发现。"
    }
  },
  "negative_results_and_dissent": {
    "registered_negative": [
      {
        "item": "cold_start_same_budget",
        "result": "collapse",
        "rel_gap": -0.311,
        "marginal_error": 0.077,
        "significance": "F1的关键反例，说明预算相同并不保证收敛。"
      }
    ],
    "dissent": [
      {
        "dissent_id": "D1",
        "target": "无条件正式律",
        "reason": "现有证据支持路径依赖+预算依赖的provisional formal律；若宣称无条件正式律，则缺少跨实现独立复现与表示界排除实验。",
        "testable_reason": "在至少一个独立实现中，固定epsilon相对代价尺度、固定预算，冷启动应复现崩溃；暖启动应复现通过。若冷启动在同等预算下稳定通过，则F1被否证。"
      },
      {
        "dissent_id": "D2",
        "target": "F2绝对epsilon不成立",
        "reason": "S2显示高动态范围下相对gap随epsilon变化显著；若存在尺度不变绝对阈值，应观察到跨尺度一致的rel gap。",
        "testable_reason": "取C=c*C0，c跨多个量级，固定绝对epsilon，观察rel gap是否不变。若不变，则F2被否证。"
      }
    ]
  },
  "answers": {
    "q1_promotion": "满足候选→provisional formal的升格条件，但不满足无条件正式律升格条件。建议判定为：候选律v3升格为provisional formal，附路径/预算/尺度申报条件。",
    "q2_independent_findings": "F1成立（高置信，需跨实现复核）；F2成立（高置信，建议形式化为相对代价尺度）。F3 provisional supported。",
    "q3_if_rejected": "若否决升格，可检验理由为：现有证据尚未排除表示界；且F1/F2未在独立实现中复现。具体检验：独立实现下同预算冷启动若稳定通过则F1否证；固定绝对epsilon跨代价尺度若rel gap不变则F2否证。"
  },
  "registration": {
    "negative_results_registered": true,
    "dissent_registered": true,
    "reproducibility_requirement": "判定必须随附：epsilon相对代价尺度定义、暖启动/退火路径、预算/迭代上限、误差度量。"
  }
}
```

——aiq SI1语义轨·20261008T051523Z
