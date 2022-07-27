from tkinter import *
import mysql.connector
from tkinter import ttk, messagebox


def admin():
    def action():
        x = username.get()
        y = password.get()
        if x.__eq__("Authority") and y.__eq__("Authority"):
            messagebox.showinfo("login successfully")

            winfire = Tk()
            winfire.geometry('800x700')
            winfire.title('Forest fire Detection')
            winfire['background'] = 'teal'
            Label(winfire, text='Forest fire Detection', bg='teal', font=('courier new', '15', 'bold')).place(x=230,
                                                                                                              y=150)
            Cameraid = Label(winfire, text='Cameraid', bg='maroon1', width=20, font='Verdana 10 bold')
            Cameraid.place(x=180, y=300)
            Location = Label(winfire, text='Location', bg='maroon1', width=20, font='Verdana 10 bold')
            Location.place(x=180, y=350)
            mail = Label(winfire, text='Fire Station Mail id', bg='maroon1', width=20, font='Verdana 10 bold')
            mail.place(x=180, y=400)

            Cameraid = StringVar()
            Location = StringVar()
            mail = StringVar()

            Cameraid = Entry(winfire, width=30, bg="silver", textvariable=Cameraid)
            Cameraid.place(x=430, y=300)
            Location = Entry(winfire, width=30, bg="silver", textvariable=Location)
            Location.place(x=430, y=350)
            mail = Entry(winfire, width=30, bg="silver", textvariable=mail)
            mail.place(x=430, y=400)

            def fire():
                myconn = mysql.connector.connect(host="localhost", user="root", passwd="root",
                                                 database="forest")
                print(myconn)
                print("MySQL Database connection successful")
                cur = myconn.cursor()
                cur.execute("INSERT INTO fire(Cameraid,Location,mail) values (%s,%s,%s)",
                            (Cameraid.get(), Location.get(), mail.get()))
                print(Cameraid.get())
                print(Location.get())
                print(mail.get())
                if messagebox.showinfo("information successfully"):
                    exec(open("main.py").read())
                myconn.commit()
                myconn.rollback()

            Button(winfire, text='submit', font='verdana 10 bold', bg='maroon1', command=fire).place(x=400, y=550)
            winfire.mainloop()


        else:
            messagebox.showinfo("failed username and password")

    winadmin = Tk()
    winadmin.title("Forest fire Detection")
    winadmin.geometry('700x600')
    winadmin['background'] = 'teal'

    Label(winadmin, text='Forest fire Detection', bg="gray", font=('courier new', '15', 'bold')) \
        .place(x=230, y=120)

    username = Label(winadmin, text="username", bg="maroon1", font='Verdana 10 bold')
    username.place(x=200, y=320)

    password = Label(winadmin, text="password", bg="maroon1", font='Verdana 10 bold')
    password.place(x=200, y=370)

    # Entry Box ------------------------------------------------------------------

    username = StringVar()
    password = StringVar()

    username = Entry(winadmin, width=30, bg="silver", textvariable=username)
    username.place(x=400, y=320)

    password = Entry(winadmin, width=30, bg="silver", textvariable=password)
    password.place(x=400, y=370)

    Button(winadmin, text="login", font='Verdana 10 bold', bg="maroon1", command=action).place(x=300, y=520)


win = Tk()
win.geometry('600x500')
win.title('Forest fire Detection')
win['background'] = 'teal'
Button(win, text="Authority", font='Verdana 10 bold', bg="maroon1", command=admin).place(x=250, y=300)
Label(win, text='Forest Fire Detection', bg="gray", font=('courier new', '15', 'bold')).place(x=170, y=130)
win.mainloop()
