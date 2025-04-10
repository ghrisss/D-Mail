import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from pandas._libs.tslibs.timestamps import Timestamp

from configs import DEBUG, EMAIL_PASSWORD


def send_email(
    email_to: str, name_to: str, today: Timestamp, store: str, file_to_attach: Path
):
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

    try:
        with open(f"anexos/{file_to_attach}", "rb") as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=file_to_attach))

        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(msg["From"], EMAIL_PASSWORD)
        servidor.send_message(msg)
        servidor.quit()
        if DEBUG:
            print(f"\u2713  Email enviado ao gerente {name_to} da loja {store}")
    except FileNotFoundError as err:
        print(f"Erro ao busca o arquivo backup em anexo {err}")
        print(f"Abortando operacao de envio referente a loja {store}")
