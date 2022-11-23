from tkinter import *

master = Tk() #创建窗口

master.title('Calculate work time') 
master.geometry("300x100+0+0")

btn_GotoWork = Button(master)
btn_GotoWork["text"] = "上班时间"
btn_GotoWork.pack()

v = StringVar()
 
def test():
     if e1.get() == '小甲鱼':
         print("正确")
         return True
     else:
         print('错误')
         e1.delete(0,END)
         return False
 
def test1():
     print('我被调用了....')
     return True
 
v=StringVar()
 
e1 = Entry(master,textvariable=v,validate='focusout',\
    validatecommand=test,invalidcommand=test1)  # validate 用于指定什么时候检测 . validatecommand 用于指定检测的标准
e2 = Entry(master)
e1.pack(padx=30,pady=10)
e2.pack(padx=30,pady=10)

mainloop()