LABJUDGE-EXT15 判定请求（WS-63 ζ 包 OBL-EXT11-a 关闭·v1.1.0 重签）
提交：vci-inbox main @6601e53e1a61d59db3a75f351a268f365dbc5d4d
变更（v1.0.1→v1.1.0 外科手术式重签，SUP-01 先例）：
1) ci/witness_zeta_verify.py fef03b8ef9ace07c：枢线修补#17——Backlund 门锚点 t=0（arg ζ(2)=0 实正）+结点紧区间 Δarg（CVZ 直评 ~1e-85）+弧盒扇形张角分支认证（≤1.2<π ⇒主值回卷唯一）；±1e-9 浮点容忍移除（只增强）。
2) ci/witness_zeta_gen.py 4e6d0bf75c641ce1：镜像披露。
3) 证书×3：iso100 0921f449554b3aca（+anchor/+darg_method/note/disclosure 附录，数学零变更）；iso1000 b8aca692db9a32f5/trunc 4a995647032ff536 仅 generator.sha256+witness_sha256；trunc zero_source.sha256 交叉引用同步新 iso1000。
关闭条件逐字：「张角余量纳入后 N_B 区间落入唯一整数窗；不得以放宽区间宽度绕过」。
证据：T=100 N_B∈[28.99999999999999999586, 29.00000000000000000442] 宽 8.6e-18，233 结点全 cvz_pt，462 盒，m_re=0；T=20 对照 N_B=1 宽 1.5e-11；zetazero N(100)=29 独立确认。
门禁：双跑字节一致 PASS；fast pins 22/22；gen 交叉核对字节一致（3.12.12）；pytest 44/44 PASS。
披露（逐字）：有限高度 T=100/1000 截断；区间见证层 PASS、kernel 层未证、非 RH 证据；隔离区间内区间见证 PASS、非全域声明。iso1000 完备性仍 BLOCKED(B1-TB)。
问：此关闭是否满足逐字条件、门禁是否充分、披露是否合规？请答 PASS 或 REVISE+理由。