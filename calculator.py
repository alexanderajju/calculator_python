from tkinter import *

window=Tk()
window.geometry("354x460")
window.title("Calculator")
label = Label(window,text="Calculator",font=("Courier New",20,'bold'))
label.pack(side=TOP)


but1=Button(window,padx=14,pady=14,bd=4,bg='white',text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(window,padx=14,pady=14,bd=4,bg='white',text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(window,padx=14,pady=14,bd=4,bg='white',text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(window,padx=14,pady=14,bd=4,bg='white',text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(window,padx=14,pady=14,bd=4,bg='white',text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(window,padx=14,pady=14,bd=4,bg='white',text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(window,padx=14,pady=14,bd=4,bg='white',text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(window,padx=14,pady=14,bd=4,bg='white',text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

butdot=Button(window,padx=47,pady=14,bd=4,bg='white',text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)

butpl=Button(window,padx=14,pady=14,bd=4,bg='white',text="+",font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(window,padx=14,pady=14,bd=4,bg='white',text="-",font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(window,padx=14,pady=14,bd=4,bg='white',text="*",font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(window,padx=14,pady=14,bd=4,bg='white',text="/",font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(window,padx=14,pady=119,bd=4,bg='white',text="CE",font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)

butequal=Button(window,padx=151,pady=14,bd=4,bg='white',text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)

window.mainloop()