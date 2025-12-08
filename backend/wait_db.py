#!/usr/bin/env python3
import socket
import time
import os

HOST = os.getenv("POSTGRES_HOST", "db")
PORT = int(os.getenv("POSTGRES_PORT", 5432))

def wait_for_db(host, port, timeout=1):
    while True:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                print(f"Conectado ao banco {host}:{port}")
                return
        except Exception as e:
            print(f"Aguardando o banco de dados iniciar... ({e})")
            time.sleep(1)

if __name__ == "__main__":
    wait_for_db(HOST, PORT)
    # substitui o processo atual pelo Django (mantém PID 1)
    os.execvp("python", ["python", "manage.py", "runserver", "0.0.0.0:8000"])
