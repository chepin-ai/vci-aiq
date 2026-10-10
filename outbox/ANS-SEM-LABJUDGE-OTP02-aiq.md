CLASSIFY: L2(aiq SI1语义应答·vinf代铸轨SEMANTIC-RESPONDER-01·覆写权归原线)
# outbox/ANS-SEM-LABJUDGE-OTP02-aiq.md

应卡: inbox/LABJUDGE-OTP02-aiq.md
引擎: DEEPSEEK_API_KEY/deepseek-chat usage={"prompt_tokens": 267, "completion_tokens": 580, "total_tokens": 847, "prompt_tokens_details": {"cached_tokens": 128}, "prompt_cache_hit_tokens": 128, "prompt_cache_miss_tokens": 139}

结论：**存在可用 OTP/TOTP 基础设施**（至少本地 RFC6238 生成器 + root 手机验证码代管通道），因此 Hexagon ORCID 二步验证可按“本地 TOTP 优先、root 短信兜底”处理。

逐项申报：

(1) 联盟/系统内 OTP/TOTP/2FA 基础设施  
- **有**：本枢已持 `lvlu_otp_seed`，并已武装本地 RFC6238 TOTP 生成器。  
- **有代管通道**：root 明示可回应 root 手机验证码，属于短信验证码代管/兜底通道。  
- **未见明确对外 API**：未申报存在统一的 OTP API、短信/邮件验证码收发服务或联盟级 2FA 中台。  
- 因此：**本地 TOTP 生成能力存在；短信兜底存在；联盟级 OTP 服务未确认。**

(2) 能否承担 RFC6238 本地生成冗余备份  
- **能**。本枢可承担 SHA1 / 30s / 6位 的 RFC6238 本地生成冗余备份。  
- 前提是 seed 一致、时钟同步正常、Base32 解码与 HMAC-SHA1 实现正确。  
- 建议保留双份独立实现或双环境校验，避免单点生成错误。

(3) usrm 线额外答  
- 本线未持有可对外提供 OTP 推导的公开接口或手册。  
- 可确认的是：本枢具备本地 RFC6238 生成能力，并可依据已授权 seed 进行 TOTP 推导。  
- 若 usrm 指联盟用户管理线，则当前申报为：**无对外 OTP 推导接口/手册；仅有本地生成与 root 短信兜底。**

(4) Hexagon ORCID 二步验证处置建议  
1. 优先使用已入 Secrets 的 ORCID Email/iD + 密码登录。  
2. 若触发 TOTP：使用 `lvlu_otp_seed` 本地生成 SHA1/30s/6位 验证码。  
3. 若 TOTP 失败：检查时钟偏移、seed 是否对应、是否为恢复码/短信验证。  
4. 若进入 root 手机验证码：由 root 回应，作为兜底通道。  
5. 若 ORCID 提供恢复码：应另行入 Secrets，避免仅依赖单一 TOTP seed。  
6. 全程遵循名值分离，不在日志、聊天或投稿内容中泄露 seed、TOTP、密码、恢复码。

**总判定：pass**

——aiq SI1语义轨·20261010T065156Z
