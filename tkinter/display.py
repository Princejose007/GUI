from tkinter import*
root=Tk()
#customize root window title-->
root.title("my First title")

#customizing root window dimention
root.geometry('650x500')

lbl=Label(root,text="My first desktop Application",font=("Roboto",12),fg='red',bg="#F5F5F5")
lbl.pack()


lb2=Label(root,text="Name:",font=("Roboto",12),fg='Black',bg="#F5F5F5")
lb2.place(x=100,y=100)

root.mainloop()