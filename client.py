import socket
from threading import Thread
import random
quiz=["What is 30/6 equal to?", " What was the first supercontinent called?", "When was Georeg Washington born?","Who won Super Bowl LVIII?"]
answers=[5,"pangaea","2/22/1732","kansas city chiefs"]
nickname=input("choose your nickname - ")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000
client.connect((ip_address,port))
print("Connected :)")
def recv ():
    while True:
        try:
            message=client.recv(2048).decode("utf-8")
            if message=="NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error Occured :(")
            client.close()
        break
def write_function ():
    while True:
        message='{},{}'.format(nickname,input(""))
        client.send(message.encode("utf-8"))
receive_thread=Thread(target=recv)
receive_thread.start()
write_thread=Thread(target=write_function)
write_thread.start()
random_num = random.randint(0,len(quiz))
print(quiz[random_num])
user_answer=input()
if user_answer==answers[random_num]:
    print("Correct")
else:
    print("Wrong")
quiz.remove(quiz[random_num])
answers.remove(answers[random_num])