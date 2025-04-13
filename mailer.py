import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from configs import DEBUG, EMAIL_PASSWORD


def send_email(
    email_to: str,
    subject: str,
    store: str,
    body_text: str,
    file_to_attach: Path,
):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = "seuemail@gmail.com"
    msg["To"] = f"{email_to}"

    msg.attach(MIMEText(body_text, "html"))
    try:
        with open(f"anexos/{file_to_attach}", "rb") as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=file_to_attach))

        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(msg["From"], EMAIL_PASSWORD)
        servidor.send_message(msg)
        servidor.quit()
        if DEBUG:
            print(
                f"\u2713  Email da loja {store} enviado"
            ) if store is not None else print(
                "\u2713  Email da Diretoria enviado"
            )
    except FileNotFoundError as err:
        print(f"Erro ao busca o arquivo backup em anexo {err}")
        print(
            f"Abortando operacao de envio referente a loja {store}"
        ) if store is not None else print(
            "Abortando operacao de envio para a diretoria"
        )
