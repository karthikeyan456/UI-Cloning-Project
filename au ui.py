import tkinter 
from tkinter import *
window=Tk()
from PIL import ImageTk,Image
lbl=Label(window, text="Change Password", fg='blue', font=("Helvetica", 30))
lbl.place(x=110, y=80)

img=Image.open(r'img1.jpeg')
test=ImageTk.PhotoImage(img)
lbli=Label(image=test)
lbli.image=test
lbli.place(x=0,y=0)


lbl1=Label(window, text="Password", fg='black', font=("Helvetica",15))
lbl1.place(x=116, y=150)
def validate(sv):
    global txtfld1
    
    #print('VALIDATED')
    #print(sv.get())
    pwd=sv.get()
    if len(pwd)<8:
        lbl3=Label(window, text=u'\u274c'+" be atleast 8 characters long.  ", fg='red', font=("Helvetica",10))
        lbl3.place(x=125, y=290)
        flag1=True
        
    elif len(pwd)>=8:
        lbl3=Label(window, text=u'\u2713'+" be atleast 8 characters long.  ", fg='green', font=("Helvetica",10))
        lbl3.place(x=125, y=290)
        flag1=False
        
    numcount=0
    lcount=0
    symcount=0
    for i in pwd:
        if i.isdigit():
            numcount=numcount+1
        elif i.isalpha():
            lcount=lcount+1
        elif i.isalnum()==False and i.isspace()==False:
            symcount=symcount+1
    
    if numcount==0:
        lbl5=Label(window, text=u'\u274c'+" contain a number.  ", fg='red', font=("Helvetica",10))#u274c is unicode for X mark
        lbl5.place(x=125, y=330)
        flag2=True
    elif numcount!=0:
        lbl5=Label(window, text=u'\u2713'+" contain a number.  ", fg='green', font=("Helvetica",10))#u2713 is unicode for tick mark
        lbl5.place(x=125, y=330)
        flag2=False
    
    if lcount==0:
        lbl4=Label(window, text=u'\u274c'+" contain a letter.  ", fg='red', font=("Helvetica",10))
        lbl4.place(x=125, y=310)
        flag3=True
    elif lcount!=0:
        lbl4=Label(window, text=u'\u2713'+" contain a letter.  ", fg='green', font=("Helvetica",10))
        lbl4.place(x=125, y=310)
        flag3=False
    
    if  symcount==0:
        lbl6=Label(window, text=u'\u274c'+" contain a symbol.  ", fg='red', font=("Helvetica",10))
        lbl6.place(x=125, y=350)
        flag4=True
    elif symcount!=0:
        lbl6=Label(window, text=u'\u2713'+" contain a symbol.  ", fg='green', font=("Helvetica",10))
        lbl6.place(x=125, y=350)
        flag4=False
    
    if flag1==True or flag2==True or flag3==True or flag4==True:
        lblr=Label(window,text='Please review the password requirements',fg='red',font=('Helvectica',10))
        lblr.place(x=118,y=220)
        txtfld1.configure(highlightcolor='red',highlightbackground='red')
        

    elif flag1==False or flag2==False or flag3==False or flag4==False:
        lblr=Label(window,text='                                                                                     ',fg='red',font=('Helvectica',10))
        lblr.place(x=118,y=220)
        txtfld1.configure(highlightcolor='black',highlightbackground='black')




        


    


    


    
sv=StringVar()
sv.trace('w',lambda name,index,mode,sv=sv: validate(sv))

txtfld1=Entry(window, bd=3,width=40,textvariable=sv,highlightthickness=2)
txtfld1.place(x=118, y=190) 

txtfld1.default_show_val=txtfld1['show']
txtfld1['show']=u'\u2022'
txtfld1.configure(highlightbackground='black',highlightcolor='black')




def passwordtoggle():
    global txtfld1,cb
    if cb.var.get()==True:
        txtfld1['show']=''
    elif cb.var.get()==False:

        txtfld1['show']=u'\u2022'#Unicode for password dot


#btn=Button(window, text="Show", fg='blue',font=("Helvetica", 10),width=7,bg='white',command=passwordtoggle)
#btn.place(x=365, y=190)
cb=Checkbutton(window,text='Show',onvalue=True,offvalue=False,command=passwordtoggle,fg='blue',font=("Helvetica",15))
cb.var=BooleanVar(value=False)
cb['variable']=cb.var
cb.place(x=370,y=185)


lbl2=Label(window, text="Your password must:", fg='black', font=("Helvetica",10))
lbl2.place(x=118, y=270)

lbl3=Label(window, text="be atleast 8 characters long.", fg='black', font=("Helvetica",10))
lbl3.place(x=125, y=290)

lbl4=Label(window, text="contain a letter.", fg='black', font=("Helvetica",10))
lbl4.place(x=125, y=310)

lbl5=Label(window, text="contain a number.", fg='black', font=("Helvetica",10))
lbl5.place(x=125, y=330)

lbl6=Label(window, text="contain a symbol.", fg='black', font=("Helvetica",10))
lbl6.place(x=125, y=350)









window.title('Password UI')
window.geometry("500x500+10+10")
window.mainloop()

