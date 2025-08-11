import networking


if __name__ == "__main__":
    for port in range(1300, 1303):
        log_in_thread = networking.LogInThread(port)
        log_in_thread.start()
    for port in range(1304, 1307):
        new_account_thread = networking.CreateNewAccountThread(port)
        new_account_thread.start()
