import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template

def send_email(to_email, subject, template, context):
    smtp_server = "smtp.ukr.net"
    smtp_port = 465
    smtp_user = "vershynasofiya2011@ukr.net"
    smtp_password = "Q88TmLbyv7M1ft5D"

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = to_email
    msg["Subject"] = subject

    template = Template(template)
    html_content = template.render(context)

    msg.attach(MIMEText(html_content, "html"))

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        print("Лист успішно надіслано!")
    except Exception as e:
        print(f"Помилка при відправленні листа: {e}")

template_text = """
<!DOCTYPE html>
<html>
<head>
    <title>Вітання!</title>
</head>
<body>
    <h1>Привіт, {{ name }}!</h1>
    <p>Ми раді вітати тебе в нашій системі. Дякуємо, що ти з нами!</p>
    <p>Твої дані:</p>
    <ul>
        <li>Ім'я: {{ name }}</li>
        <li>Електронна пошта: {{ email }}</li>
    </ul>
    <p>З найкращими побажаннями,<br>Команда</p>
</body>
</html>
"""

context = {
    "name": "Олександр",
    "email": "alex@example.com"
}

send_email("vershynasofiya2011@ukr.net", "Ласкаво просимо!", template_text, context)





