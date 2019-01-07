import tkinter

#tkinter._test()

def baseLabel(event):
    global baseFrame
    print("press button....")
    lb = tkinter.Label(baseFrame,text="thanks for press")
    lb.pack()


#画出程序总框架
baseFrame = tkinter.Tk()

lb = tkinter.Label(baseFrame, text="Simulation button")

#label 绑定相应的消息和处理函数
#自动获取左键点击，并启动相应的处理函数baseLabel
lb.bind("<Button-1>", baseLabel)
lb.pack()

#自动消息循环
#到此，表示程序开始运行
baseFrame.mainloop()