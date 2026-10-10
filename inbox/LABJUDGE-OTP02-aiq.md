CLASSIFY: L1
# LABJUDGE-OTP02-aiq
OTP 基础设施全联盟普查卡（FM-021/022/023 合规，单 ask 键）。
```json
{"judge_id":"OTP02","line":"aiq","ask":"OTP 基础设施全联盟普查（命令：OTP 基础设施在全系统/联盟中查询，或咨询 usrm；root 手机验证码可由 root 回应）。背景：Hexagon 投稿链路已解锁 ORCID 登录凭据（Email/iD + 密码已入 Secrets 名值分离），登录后大概率遭遇 TOTP 二步验证；本枢已持 seed（lvlu_otp_seed）并武装本地 RFC6238 生成器。另 root 明示：如需 root 手机验证码可由 root 回应。请你线申报：(1) 你线或你所知联盟/系统内是否存在任何 OTP/TOTP/2FA 基础设施、API、服务或代管通道（含短信/邮件验证码收发能力）？(2) 若无，你线能否承担 RFC6238 本地生成的冗余备份（SHA1/30s/6位）？(3) usrm 线请额外答：你是否持有可对外提供 OTP 推导的接口或手册？(4) 对 Hexagon ORCID 二步验证的处置建议。行尾给 总判定：pass（有可用基础设施或备份已就位）或 fail 或 undecided。"}
```
