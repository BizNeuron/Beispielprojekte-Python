import smtplib
import socket
import threading
from email.message import EmailMessage
from typing import Union
from random import randrange

import db_controll

EMAIL_ADDRESS = "example@e.com"  # The address used to send confirmation codes
EMAIL_PASSWORD = "XXXXXXXXXXXX"
EMAIL_SMTP = "smtp-e.e.com"


def send_email(send_mail_address: str, send_mail_subject: str, send_mail_text) -> Union[int, bool]:
    mail = EmailMessage()
    mail.set_content(send_mail_text)
    mail["From"] = f"Very Simple Server <{EMAIL_ADDRESS}>"
    mail["To"] = send_mail_address
    mail["Subject"] = send_mail_subject
    try:
        mamazone_mail = smtplib.SMTP(EMAIL_SMTP, 587)  # bizone.run@hotmail.com
        mamazone_mail.starttls()
        mamazone_mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        try:
            mamazone_mail.send_message(mail)
            return True
        except smtplib.SMTPException:
            return False
    except smtplib.SMTPException:
        return False


class LogInThread(threading.Thread):
    def __init__(self, port: int):
        super(LogInThread, self).__init__()
        ip_address = socket.gethostbyname(socket.gethostname())
        self.log_in_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_in_socket.bind((ip_address, port))
        self.lock = threading.Lock()

    def run(self) -> None:
        while True:
            try:
                while True:
                    self.log_in_socket.listen(1)
                    while True:
                        communication, address = self.log_in_socket.accept()
                        while True:
                            data = communication.recv(2048)
                            if not data:
                                communication.close()
                                break
                            data = data.decode("utf-8")
                            data = data.split("|next|")  # Data format: USERNAME|next|EMAIL|next|PASSWORD
                            try:
                                with self.lock:
                                    log_in = db_controll.log_in(data[0], data[1], data[2])
                            except IndexError:
                                communication.send("Error".encode("utf-8"))
                                communication.close()
                                break
                            if log_in:
                                communication.send("True".encode("utf-8")) # Login successful.
                                communication.close()
                                break
                            else:
                                communication.send("False".encode("utf-8")) # Login unsuccessful.
                                communication.close()
                                break
                        break
            except socket.error:
                continue


class CreateNewAccountThread(threading.Thread):
    def __init__(self, port: int):
        super(CreateNewAccountThread, self).__init__()
        ip_address = socket.gethostbyname(socket.gethostname())
        self.create_new_account_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.create_new_account_socket.bind((ip_address, port))
        self.lock = threading.Lock()

    def run(self) -> None:
        while True:
            try:
                self.create_new_account_socket.listen(1)
                while True:
                    communication, address = self.create_new_account_socket.accept()
                    while True:
                        data = communication.recv(2048)
                        if not data:
                            communication.close()
                            break
                        data = data.decode("utf-8")
                        account_data = data.split("|next|")  # Data format: REALNAME|next|REALFAMILYNAME|next|ADDRESS|next|EMAIL|next|USERNAME|next|PASSWORD
                        random_value = randrange(1000000000)
                        send_confirmation_mail = send_email(f"{account_data[3]}", "Confirmation",
                                                            f"Enter this code {random_value}, to create your Account.")
                        if send_confirmation_mail:
                            communication.send(f"{random_value}".encode("utf-8"))
                            while True:
                                data = communication.recv(2048)
                                while True:
                                    if not data:
                                        break
                                    if int(data.encode("utf-8")) == random_value:
                                        write_account_in_db = db_controll.create_new_account(account_data[0],
                                                                                             account_data[1],
                                                                                             account_data[2],
                                                                                             account_data[3],
                                                                                             account_data[4],
                                                                                             account_data[5])
                                        if write_account_in_db:  # Make sure that the new account is saved before the confirmation is sent
                                            communication.send("True".encode("utf-8"))
                                            communication.close()
                                            break
                                        else:
                                            communication.close()
                                            break
                                break
                        else:
                            communication.send("False".encode("utf-8"))
                            communication.close()
                            break
            except (socket.error, IndexError):
                continue
