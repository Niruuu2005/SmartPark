from datetime import datetime
from pathlib import Path
from tkinter import END, W, Button, Canvas, Entry, Frame, Label, PhotoImage, Scrollbar, Tk
import tkinter.messagebox as mess
import mysql.connector
import customtkinter
from tkinter import ttk as v

def close():
    root.destroy()

root=Tk()

loc = Path(__file__).parent.resolve()
loc = str(loc) + "\\"

insert_img1 = PhotoImage(file=loc + "DETAILS.png")
insert_img2 = PhotoImage(file=loc + "ENTRY.png")
insert_img3 = PhotoImage(file=loc + "EXIT.png")
insert_img4 = PhotoImage(file=loc + "close.png")
insert_img5 = PhotoImage(file=loc + "DIAPLAY.png")

dati = datetime.now()
date = dati.strftime("%d/%m/%Y || %I:%M:%S %p")

final=[]
final1=[]
final2=[]

frame = Frame(root, bg="beige")


def into_put():

    can = Canvas(root, width=4000, bg='aquamarine')
    can.pack(side='left', fill='y')

    # customer details
    def info():

        can.destroy()
        frame.destroy()

        framegrid = Frame(bg="beige")

        cusname = Label(
            framegrid, text="Customer Name :", font=("", 15), fg="black")
        cusname_ = Entry(framegrid, font=("", 15), justify="center")
        final.append(cusname_)

        cusnum = Label(
            framegrid, text="Customer Ph.no. :", font=("", 15), fg="black")
        cusnum_ = Entry(framegrid, font=("", 15), justify="center")
        cusnum__ = Entry(framegrid, font=("", 15), justify="center")
        final.append(cusnum_)
        final.append(cusnum__)

        car_number = Label(
            framegrid, text="Vehicle no. :", font=("", 15), fg="black")
        car_enter = Entry(framegrid, font=("", 15), justify="center")
        final.append(car_enter)

        cusname.grid(row=0, column=0, pady=20)
        cusname_.grid(row=0, column=1, pady=20)

        cusnum.grid(row=1, column=0, pady=20)
        cusnum_.grid(row=1, column=1, pady=20)
        cusnum__.grid(row=1, column=2, pady=20, padx=10)

        car_number.grid(row=5, column=0, pady=20)
        car_enter.grid(row=5, column=1, pady=20)

        framegrid.pack(anchor='center', pady=75)

        fra = Frame(framegrid)

        # save the details in mysql table parking_span
        def insert():

            list1 = []
            for i in final:
                list1.append(i.get())

            if list1 == ["", "", "", ""]:
                mess.showinfo("insert status", "insert empty")

            else:
                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "insert into parking_span VALUES (%s,%s,%s,%s)"
                cur.execute(query, list1)
                mess.showinfo("insert status", "success value inputted")
                a.commit()
                a.close

                framegrid.destroy()
                b1_1.destroy()
                b1_2.destroy()
                b1_3.destroy()
                into_put()

        b1_2 = customtkinter.CTkButton(
            fra, text="SAVE", command=insert, width=20, height=4)

        def clear():

            for i in final:
                i.delete(0, END)

        b1_3 = customtkinter.CTkButton(
            fra, text="CLEAR", command=clear, width=20, height=4)

        def back():

            b1_1.destroy()
            b1_2.destroy()
            b1_3.destroy()
            framegrid.destroy()
            into_put()

        b1_1 = customtkinter.CTkButton(
            fra, text="BACK", command=back, width=20, height=4)

        b1_2.grid(row=0, column=0, pady=20)
        b1_3.grid(row=0, column=2, pady=20)
        b1_1.grid(row=1, column=1, pady=20)

        fra.grid(row=6, column=1, pady=50)

    b1 = Button(can, image=insert_img1, command=info, borderwidth=0,
                bg="aquamarine", activebackground="aquamarine")
    b1.pack(pady=30, anchor='center')

    # to store the entry time date im db
    def entered():

        can.destroy()
        frame.destroy()

        frame1 = Frame(bg="beige")

        car_number = Label(
            frame1, text="Vehicle no. :", font=("", 15), fg="black")
        car_enter = Entry(frame1, font=("", 15), justify="center")
        final1.append(car_enter)

        slot_park = Label(
            frame1, text="Parking slot :", font=("", 15), fg="black")
        slot_ = Entry(frame1, font=("", 15), justify="center")
        final1.append(slot_)

        car_number.grid(row=0, column=0)
        car_enter.grid(row=0, column=1)

        slot_park.grid(row=1, column=0, pady=20)
        slot_.grid(row=1, column=1)

        frame1.pack(anchor='center', pady=100)

        fra =Frame(frame1)

        # sql query to store entry date time in parking_span1
        def enteredtab():

            list2 = [car_enter.get(), slot_.get(), date]

            if list2 == ["", "", ""]:
                mess.showinfo("insert status", "insert empty")

            else:
                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "insert into parking_span1 VALUES( %s ,%s,%s)"
                cur.execute(query, list2)
                mess.showinfo("insert status", "success value inputted")
                a.commit()
                a.close

                frame1.destroy()
                b2_1.destroy()
                b2_2.destroy()
                b2_3.destroy()
                into_put()

        b2_2 = customtkinter.CTkButton(
            fra, text="ENTER-->", command=enteredtab, width=10, height=2)

        def clear():

            for i in final1:
                i.delete(0, END)

        b2_3 = customtkinter.CTkButton(
            fra, text="CLEAR", command=clear, width=10, height=2)

        def back1():

            b2_1.destroy()
            b2_2.destroy()
            b2_3.destroy()
            frame1.destroy()
            into_put()

        b2_1 = customtkinter.CTkButton(
            fra, text="BACK", command=back1, width=10, height=2)

        b2_2.grid(row=0, column=0, pady=20)
        b2_3.grid(row=0, column=2, pady=20)
        b2_1.grid(row=1, column=1, pady=20)

        fra.grid(row=3, column=0, pady=50, columnspan=2)

    b2 = Button(can, image=insert_img2, command=entered,
                bg="aquamarine", borderwidth=0, activebackground="aquamarine")
    b2.pack(pady=30, anchor='center')

    # to store the date time of exit in db
    def exit():

        can.destroy()
        frame.destroy()

        frame2 = Frame(bg="beige")

        car_number = Label(
            frame2, text="Vehicle no. :", font=("", 15), fg="black")
        car_enter = Entry(frame2, font=("", 15), justify="center")
        final2.append(car_enter)

        car_number.grid(row=0, column=0)
        car_enter.grid(row=0, column=1)

        frame2.pack(anchor='s', pady=120)

        fra = Frame(frame2)

        # query to store data in db table parking_span2
        def exitedtab():

            global list3

            list3 = [car_enter.get(), date]

            if list3 == ["", date]:
                mess.showinfo("insert status", "insert empty")

            else:
                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "insert into parking_span2 VALUES( %s ,%s)"
                cur.execute(query, list3)
                mess.showinfo("insert status", "success value inputted")
                a.commit()
                a.close

                frame2.destroy()
                b3_1.destroy()
                b3_2.destroy()
                b3_3.destroy()
                into_put()

        b3_2 = customtkinter.CTkButton(
            fra, text="<--EXIT", command=exitedtab, width=10, height=2)

        def clear():

            for i in list3:
                i.delete(0, END)

        b3_3 = customtkinter.CTkButton(
            fra, text="CLEAR", command=clear, width=10, height=2)

        def back2():

            b3_1.destroy()
            b3_2.destroy()
            b3_3.destroy()
            frame2.destroy()
            into_put()

        b3_1 = customtkinter.CTkButton(
            fra, text="BACK", command=back2, width=10, height=2, bg="beige")

        b3_2.grid(row=0, column=0, pady=20)
        b3_3.grid(row=0, column=2, pady=20)
        b3_1.grid(row=1, column=1, pady=20)

        fra.grid(row=2, column=0, pady=50, columnspan=2)

    b3 = Button(can, image=insert_img3, command=exit, bg="aquamarine",
                borderwidth=0, activebackground="aquamarine")
    b3.pack(pady=30, anchor='center')

    # treeview+sql to show data in a tab
    def showplay():

        can.destroy()
        frame.destroy()

        tree = Frame(root)
        tree.pack(pady=10)

        scroll = Scrollbar(tree)
        scroll.pack(side='right', fill='y')

        tee = v.Treeview(tree, yscrollcommand=scroll.set,
                         selectmode="extended")
        tee.pack()

        scroll.config(command=tee.yview)

        tee['columns'] = ("vehicle no.", "Customer name", "Phone no.1",
                          "Phone no. 2", "slot", "Dte-time entry", "Dte-time exit")

        tee.column("#0", width=0, stretch='no')
        tee.column("vehicle no.", width=200, anchor=W)
        tee.column("Customer name", width=200, anchor=W)
        tee.column("Phone no.1", width=200, anchor=W)
        tee.column("Phone no. 2", width=200, anchor=W)
        tee.column("slot", width=200, anchor=W)
        tee.column("Dte-time entry", width=200, anchor=W)
        tee.column("Dte-time exit", width=200, anchor=W)

        tee.heading("#0", text='')
        tee.heading("vehicle no.", text='vehicle no.', anchor=W)
        tee.heading("Customer name", text='Customer name', anchor=W)
        tee.heading("Phone no.1", text='Phone no.1', anchor=W)
        tee.heading("Phone no. 2", text='Phone no. 2', anchor=W)
        tee.heading("slot", text='slot alloted', anchor=W)
        tee.heading("Dte-time entry", text='Dte-time entry', anchor=W)
        tee.heading("Dte-time exit", text='Dte-time exit', anchor=W)

        a = mysql.connector.connect(
            host="localhost", user="root", password="@20June2005", database="minpro")

        cur = a.cursor()

        q1 = "use minpro"
        cur.execute(q1)

        query = "select p1.vehicle_no, p.customer_name, p.customer_phone1, p.customer_phone2 , p1.slot , p1.datetime_entry, p2.datetime_exit from parking_span p join parking_span1 p1 on p.vehicle_no = p1.vehicle_no join parking_span2 p2 on p1.vehicle_no = p2.vehicle_no order by p1.datetime_entry"
        cur.execute(query)

        fetch = cur.fetchall()

        for rec in fetch:
            tee.insert(parent='', index="end", values=(
                rec[0], rec[1], rec[2], rec[3], rec[4], rec[5], rec[6],))

        a.commit()
        a.close

        # UPDAte query of sql for different combination of updates
        f = Frame(root)
        f.pack()

        dumy = Label(
            f, text='For update(enter the vehicle number of which the data is to be updated)')
        dumy.grid(row=0, column=0, pady=20)

        car_number = Label(
            f, text="Vehicle no. :", font=("", 15), fg="black")

        car_enter = Entry(f, font=("", 15), justify="center")

        car_number.grid(row=1, column=0)
        car_enter.grid(row=1, column=1)

        dumy = Label(f, text='Update(enter the data to be updated)')
        dumy.grid(row=2, column=0, pady=20)

        cusname = Label(
            f, text="Customer Name :", font=("", 15), fg="black")
        cusname_ = Entry(f, font=("", 15), justify="center")

        cusname.grid(row=3, column=0, pady=10)
        cusname_.grid(row=3, column=1, pady=10)

        cusnum = Label(
            f, text="Customer Ph.no. :", font=("", 15), fg="black")
        cusnum_ = Entry(f, font=("", 15), justify="center")
        cusnum__ = Entry(f, font=("", 15), justify="center")

        cusnum.grid(row=3, column=2, pady=10, padx=10)
        cusnum_.grid(row=3, column=3, pady=10)
        cusnum__.grid(row=3, column=4, pady=10,)

        slot_park = Label(
            f, text="Parking slot :", font=("", 15), fg="black")
        slot_ = Entry(f, font=("", 15), justify="center")

        slot_park.grid(row=4, column=0)
        slot_.grid(row=4, column=1)

        list0 = []
        list0.append(car_enter)
        list0.append(cusname_)
        list0.append(cusnum_)
        list0.append(cusnum__)
        list0.append(slot_)

        def update():
            lista = []
            listb = []

            for i in list0:
                print(i.get())
                lista.append(i.get())

            if lista == ["", "", "", "", ""]:
                mess.showinfo("UPDATE status", "insert empty")

            elif lista == [lista[0], lista[1], "", "", "", ]:
                listb = [lista[1], lista[0]]
                for j in listb:
                    print(j)
                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "update parking_span set customer_name =%s where vehicle_no =%s"
                cur.execute(query, listb)

                mess.showinfo("insert status", "success value inputted")

                a.commit()
                a.close

            elif lista == [lista[0], "", lista[2], "", "", ]:
                listb = [lista[2], lista[0]]

                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "update parking_span set customer_phone1 =%s where vehicle_no =%s"
                cur.execute(query, listb)

                mess.showinfo("insert status", "success value inputted")

                a.commit()
                a.close

            elif lista == [lista[0], "", "", lista[3], "", ]:
                listb = [lista[3], lista[0]]

                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "update parking_span set customer_phone2 =%s where vehicle_no =%s"
                cur.execute(query, listb)

                mess.showinfo("insert status", "success value inputted")

                a.commit()
                a.close

            elif lista == [lista[0], "", "", "", lista[4]]:
                listb = [lista[4], lista[0]]
                for j in listb:
                    print(j)
                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "update parking_span1 set slot =%s where vehicle_no =%s"
                cur.execute(query, listb)

                mess.showinfo("insert status", "success value inputted")

                a.commit()
                a.close

            elif lista == [lista[0], lista[1], lista[2], "", ""]:
                listb = [lista[1], lista[2], lista[0], ]
                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "update parking_span1 set customer_name=%s,customer_phone1=%s where vehicle_no =%s"
                cur.execute(query, listb)

                mess.showinfo("insert status", "success value inputted")

                a.commit()
                a.close

            else:
                listb = [lista[4], lista[2], lista[1], lista[0]]

                a = mysql.connector.connect(
                    host="localhost", user="root", password="@20June2005", database="minpro")

                cur = a.cursor()

                q1 = "use minpro"
                cur.execute(q1)

                query = "update parking_span1 set slot =%s ,customer_phone1=%s, customer_name=%s,where vehicle_no =%s"
                cur.execute(query, listb)

                mess.showinfo("insert status", "success value inputted")

                a.commit()
                a.close

        b5_2 = customtkinter.CTkButton(root, text='UPDATE', command=update,
                                       bg="aquamarine", borderwidth=0,)
        b5_2.pack(pady=20, anchor='center')

        def backo():

            tree.destroy()
            b5_1.destroy()
            f.destroy()
            b5_2.destroy()
            into_put()

        b5_1 = customtkinter.CTkButton(root, text='BACK', command=backo,
                                       bg="aquamarine", borderwidth=0,)
        b5_1.pack(pady=20, anchor='center')

    b5 = Button(can, image=insert_img5, command=showplay, borderwidth=0,
                bg="aquamarine", activebackground="aquamarine")
    b5.pack(pady=30, anchor='center')

    b4 = Button(can, text="CLose", image=insert_img4, command=close,
                bg="aquamarine", activebackground="aquamarine", borderwidth=0)
    b4.pack(pady=30)
    
into_put()
root.mainloop()