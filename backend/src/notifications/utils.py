import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_message(message, to_whom):
    sender = "seamusic.official@yandex.com"
    password = "unsp777."

    smtp_server = "smtp.yandex.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = to_whom
        msg['Subject'] = "Subject of your email"

        body = message
        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(sender, to_whom, msg.as_string())
        return "The message was sent successfully!"
    except Exception as ex:
        return f"{ex} Check your login or password"
