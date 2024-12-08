import smtplib,ssl
import Important

def send_mail(receiver,message):
    host = "smtp.gmail.com"
    port = 465

    user_name = Important.get_mail()

    app_password = Important.get_pass()

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(user_name,app_password)
        server.sendmail(user_name,receiver,message)
