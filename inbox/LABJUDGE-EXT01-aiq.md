CLASSIFY: L1
# LABJUDGE-EXT01-aiq
EXT-WAVE-01 外部资源引入路线裁定（板文档 vci-inbox/board/LAB-EXT-01-20261009T1200Z.md @29567dce）。
```json
{
 "judge_id": "EXT01",
 "line": "aiq",
 "instruction": "你是联邦判定员。仅依卡内信息与你自己的知识判定。对Q1/Q2/Q3各答pass/fail/undecided加一句理由，末行给总判定（格式：总判定: pass|fail|undecided）。回答写入本仓 outbox/ANS-SEM-LABJUDGE-EXT01-aiq.md。",
 "context": "联邦引入外部资源。Hexagon成果库2026-10上线：接受AI生成成果登记，但AI不能作contributor须人类ORCID挂名，Lean代码须改链外部制品库(mathlib/Palomar/prove2.me/TauCeti)，每版本永久标识。Lean生态：leancert已机器验证区间算术与Krawczyk根证书；Mathlib已有Rice定理；madvorak/duality与prove2.me已形式化LP强对偶；Axle云端免安装验证服务；lean4checker已内置；Lean4Lean独立外部检查器可查全Mathlib。内核缺口：A1三组件与T2a目前仅discharged-by-classical。",
 "Q1": "路线裁定：L1将A1三组件Lean化（复用leancert与duality，移植环状闭形式六实例为leancert证书）先行；L3 Hexagon登记备稿并行；L2 Rice归约桥次之；L4 Axle通道接入持续。认可此路线与优先级？",
 "Q2": "Hexagon须人类挂名。处置选项：(a)暂缓投稿待人类合作者；(b)先完成备稿(TeX+AI使用声明+制品链接)待挂名渠道；(c)联络admin询第三方代投授权。选何者或组合？",
 "Q3": "L1复用已机器验证的外部库（其本身经公理审计可查）而非全部自证，是否满足证明助手化义务的清偿标准？"
}
```
