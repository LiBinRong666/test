# test_smtp.py
import smtplib
from config.config import EMAIL_CONFIG

def test_smtp():
    try:
        if EMAIL_CONFIG["use_ssl"]:
            server = smtplib.SMTP_SSL(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["smtp_port"], timeout=30)
        else:
            server = smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["smtp_port"], timeout=30)
            server.starttls()
        server.login(EMAIL_CONFIG["sender_email"], EMAIL_CONFIG["sender_pwd"])
        print("✅ SMTP连接+登录成功！配置无误")
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("❌ 授权码错误/SMTP未开启")
    except smtplib.SMTPServerDisconnected:
        print("❌ 端口/加密方式不匹配（465开SSL，587关SSL）")
    except Exception as e:
        print(f"❌ 其他错误：{str(e)}")

if __name__ == "__main__":
    test_smtp()