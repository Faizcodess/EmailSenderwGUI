from tkinter import *
import smtplib as s

root= Tk()
root.geometry('500x600')
root.title("Email Sender")
root.configure(bg='dark sea green')

def sendmail():
    obj=s.SMTP('smtp.gmail.com',587)
    obj.ehlo()
    obj.starttls()
    subjectval=subject.get()
    bodyval=body.get(1.0,'end')
    message="subject:{}\n\n{}".format(subjectval,bodyval)
    obj.login(sender.get(),password.get())
    listrec=receiver.get().split(",")
    obj.sendmail(sender.get(),listrec,message)
    print("Mail Sent!")
    obj.quit()
    Label(root, text="Mail Sent!", width=20,fg='green', font=("bold",15)).place(x=140,y=530)

def clear_entry():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    body.delete(1.0,END)

Label(root,text="Email App",width=20,font="buffallo 20 bold",bg="dark sea green").place(x=70,y=10)

Label(root, text="Your Email ID:", width=20, font=("arial",10,"bold"),bg="dark sea green").place(x=20,y=70)

sender=StringVar()
password=StringVar()
receiver=StringVar()
subject=StringVar()

e1=Entry(root, width=40, textvariable=sender)
e1.place(x=200, y=70)

Label(root, text="Your Password:", width=20, font=("arial",10,"bold"),bg="dark sea green").place(x=20,y=120)

e2=Entry(root, width=40, show="*", textvariable=password)
e2.place(x=200, y=120)

Label(root, text="Compose Your Email", width=20, font=("verdana 12 bold"),bg="dark sea green").place(x=130,y=190)

Label(root, text="Receivers:", width=20, font=("arial 10 bold"),bg="dark sea green").place(x=20,y=250)

e3=Entry(root, width=40, textvariable=receiver)
e3.place(x=200, y=250)

Label(root, text="Subject:", width=20, font=("arial 10 bold"),bg="dark sea green").place(x=20,y=300)

e4=Entry(root, width=40, textvariable=subject)
e4.place(x=200, y=300)

Label(root, text="Message:", width=20, font=("arial 10 bold"),bg="dark sea green").place(x=20,y=350)

body=Text(root, width=30, height=10)
body.place(x=200, y=350)

Button(root,text="Send", width=20, bg='saddle brown',fg="white", command=sendmail,font="arial 10 italic").place(x=50, y=550)

Button(root,text="Reset", width=20, bg='saddle brown',fg="white", command=clear_entry,font="arial 10 italic").place(x=250, y=550)

Label(root, text="Developed By Mo Faizan Ali", width=60, font=("bold",10),bg="black",fg="white").place(x=0,y=620)

root.mainloop()