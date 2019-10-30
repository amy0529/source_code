import tkinter
MainForm=tkinter.Tk()
MainForm.geometry("250x150")
MainForm.title("三酷猫!")
MainForm.iconbitmap(r'D:\MyThirdBook2017年底计划\python入门及实践\第十一章\McuSDKTool.ico')
MainForm['background']='LightSlateGray' 
btn1=tkinter.Button(MainForm,text="退出", fg="black")
def turn_property(event):
    event.widget["activeforeground"]="red"
    event.widget["text"]="OK"
def mouse_Key(x):
    x.widget["background"]="green"
#btn1.bind("<Button-1>",mouse_Key) 
btn1.bind("<Enter>",turn_property)
btn1.pack()
MainForm.mainloop()


