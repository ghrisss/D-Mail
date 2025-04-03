from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from datetime import datetime
from configs import EMAIL_PASSWORD, DEBUG


def send_email(email_to, name_to, today: datetime, store, file_to_attach):
    msg = MIMEMultipart()
    msg["Subject"] = f"OnePage Dia {today.day}/{today.month} - Loja {store}"
    msg["From"] = "seuemail@gmail.com"
    msg["To"] = f"{email_to}"

    # link_imagem = "coloque_aqui_o_link_da_sua_imagem"

    corpo_email = f"""
    <p>Boa tarde {name_to},</p>
    <p>E-mail Text</p>
    <p>Att., DEV</p>
    """

    msg.attach(MIMEText(corpo_email, "html"))

    with open(f"anexos/{file_to_attach}", "rb") as arquivo:
        msg.attach(MIMEApplication(arquivo.read(), Name=file_to_attach))

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(msg["From"], EMAIL_PASSWORD)
    servidor.send_message(msg)
    servidor.quit()
    if DEBUG:
        print("Email enviado")
