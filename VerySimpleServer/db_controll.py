import sqlite3
from os.path import join
import password

DB_PATH = join("Data_Banks", "users_accounts.db")


def create_db(path=DB_PATH):
    try:
        db_connection = sqlite3.connect(path)
        db_cursor = db_connection.cursor()
    except FileNotFoundError:
        temp = open(path, "w")
        temp.close()
        db_connection = sqlite3.connect(path)
        db_cursor = db_connection.cursor()

    with db_connection:
        db_cursor.execute("""CREATE TABLE users_accounts (
                real_name TEXT, real_family_name TEXT, address TEXT, email_address TEXT, username TEXT, password TEXT  
                )""")
        return True


def create_new_account(real_name: str, real_family_name: str, address: str,
                       email_address: str, username: str, password_hashed: str, path=DB_PATH) -> bool:
    try:
        db_connection = sqlite3.connect(path)
        db_cursor = db_connection.cursor()
    except FileNotFoundError:
        create_db()
        db_connection = sqlite3.connect(path)
        db_cursor = db_connection.cursor()
    with db_connection:
        db_command = f"""INSERT INTO users_accounts VALUES (
                '{real_name}', '{real_family_name}', '{address}', '{email_address}', '{username}', '{password_hashed}' 
                )"""  # Duplicates must be removed in future / Duplikate müssen zukünftig entfernt werden
        db_cursor.execute(db_command)
        return True


def log_in(username: str, email_address: str, password_unhashed: str, path=DB_PATH) -> bool:
    try:
        db_connection = sqlite3.connect(path)
        db_cursor = db_connection.cursor()
    except FileNotFoundError:
        create_db()
        db_connection = sqlite3.connect(path)
        db_cursor = db_connection.cursor()
    db_command = f"""
        SELECT password FROM users_accounts WHERE username == '{username}' AND email_address == '{email_address}'"""
    db_cursor.execute(db_command)
    db_cursor_fetchall = db_cursor.fetchall()

    if not db_cursor_fetchall:
        return False
    else:
        account = list(db_cursor_fetchall[0])
        account_password = str(account[0])
        if password.p2_equal_p1(password_unhashed, account_password):
            return True
        else:
            return False
