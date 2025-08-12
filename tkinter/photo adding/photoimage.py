from tkinter import*
root=Tk()
label=Label(root,text='This is image').pack(side=TOP,pady=10)
path=PhotoImage(file=r"C:\Users\princ\Downloads\itachi-manga-pages-wallpaper-v0-hu5ulwzxhl2f1.png")
label_image=Label(root,image=path,width=400,height=600)
label_image.pack()
root.geometry("900x400")
root.title("pythonphoto.com")
root.mainloop()