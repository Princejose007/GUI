from tkinter import*
root=Tk()
root.title("my First title")

root.geometry('650x500')

lbl=Label(root,text="My first desktop Application",font=("Roboto",12),fg='red',bg="#F5F5F5")
lbl.pack()


lb2=Label(root,text="Name :",font=("Roboto",12),fg='Black',bg="#F5F5F5")
lb2.place(x=100,y=100)
entry=Entry(root,width=35)
entry.place(x=160,y=105)


lb3=Label(root,text="age:",font=("Roboto",12),fg='Black',bg="#F5F5F5")
lb3.place(x=120,y=135)
entry2=Entry(root,width=35)
entry2.place(x=160,y=135)


def clicked():
    print("submited")

#planting Buttonn to our  GUI APP
btn=Button(root,text="click me",command=clicked())
btn.pack()
root.geometry('250x200')







root.mainloop()