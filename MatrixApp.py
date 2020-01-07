import numpy as np
from tkinter import *
rWin=None

def intConvert(l):
    l = l.split(";")
    ind = 0
    for i in l:
        l[ind] = i.split(" ")
        ind += 1
    res = [[int(i) for i in t] for t in l]
    return res

def resultDisp(result):
    global rWin
    rWin=Tk()
    rWin.geometry("150x150")
    rWin.title("Result")
    ro=0
    for i in result:
        Label(rWin,text=i).grid(column=1,row=ro) 
        ro+=1
    rWin.mainloop()

def windowDestroy():
    global rWin
    try:
        rWin.destroy()
    except Exception as e:
        pass

   
def calculation(A,B,C,D,I,OP,ans):
    from numpy.linalg import matrix_power 
    from numpy import dot 
    OP=ans+OP
    print(OP)
    register={"A":A,"B":B,"C":C,"D":D,"I":I,"OP":OP,"ans":ans,"dot":dot,"matrix_power":matrix_power}
    exec(OP,{"__buitlins__":None},register)
    windowDestroy()
    resultDisp(register["ans"])

def stringConvert(s):
    while 1:
        if "^" in s:
            i=s.index("^")
            temp="matrix_power("+s[i-1]+","+s[i+1]+")"
            rep=s[i-1:i+2]
            s=s.replace(rep,temp)
        else:
            break
    print("s=",s)
    while 1:
        varList=["A","B","C","D","I"]
        if "*" in s:
            #print(s)
            i=s.index("*")
            if s[i+1]=="m" and s[i-4:i].isdigit()==True:
                temp="dot("+s[i-4:i]+","+s[i+1:i+17]+")"
                rep=s[i-4:i+17]
                s=s.replace(rep,temp)
            elif s[i+1] == "m" and s[i-3:i].isdigit()==True:
                temp = "dot("+s[i-3:i]+","+s[i+1:i+17]+")"
                rep = s[i-3:i+17]
                s = s.replace(rep, temp)

            elif s[i+1] == "m" and s[i-2:i].isdigit()==True:
                temp = "dot("+s[i-2:i]+","+s[i+1:i+17]+")"
                rep = s[i-2:i+17]
                s = s.replace(rep, temp)
            
            elif s[i+1] == "m" and s[i-1].isdigit()==True:
                temp = "dot("+s[i-1]+","+s[i+1:i+17]+")"
                rep = s[i-1:i+17]
                s = s.replace(rep, temp)

            elif s[i-4:i].isdigit()==True and s[i+1] in varList:
                temp = "dot("+s[i-4:i]+","+s[i+1]+")"
                rep = s[i-4:i+2]
                s = s.replace(rep, temp)

            elif s[i-3:i].isdigit()==True and s[i+1] in varList:
                temp = "dot("+s[i-3:i]+","+s[i+1]+")"
                rep = s[i-3:i+2]
                s = s.replace(rep, temp)

            elif s[i-2:i].isdigit()==True and s[i+1] in varList:
                temp = "dot("+s[i-2]+s[i-1]+","+s[i+1]+")"
                rep = s[i-2:i+2]
                s = s.replace(rep, temp)
            elif s[i-1].isdigit() == True and s[i+1] in varList:
                temp = "dot("+s[i-1]+","+s[i+1]+")"
                rep = s[i-1:i+2]
                s = s.replace(rep, temp)
            elif s[i-1] in varList and s[i+1] in varList:
                temp = "dot("+s[i-1]+","+s[i+1]+")"
                rep = s[i-1:i+2]
                s = s.replace(rep, temp)
            
            
            

        else:
            break
    return s
            

def getValues(a="0 0 0;0 0 0;0 0 0", b="0 0 0;0 0 0;0 0 0", c="0 0 0;0 0 0;0 0 0", d="0 0 0;0 0 0;0 0 0", op="None"):
    mat1=np.array(intConvert(a))
    mat2=np.array(intConvert(b))
    mat3=np.array(intConvert(c))
    mat4=np.array(intConvert(d))
    size=mat1.shape
    matId=np.identity(size[0],dtype=int)
    op=stringConvert(op)
    calculation(mat1,mat2,mat3,mat4,matId,op,"ans=")

def window():
    rt=Tk()
    rt.title("MatrixOps")
    rt.configure(bg="#1e3eb3")
    rt.geometry("500x530")
    
    Label(rt,text="\n",bg='#1e3eb3').grid(column=0,row=0)
    Label(rt,text="\n",bg='#1e3eb3').grid(column=1,row=0)
    Label(rt,text="Mat A:",font=("arialbold",20),bg='#1e3eb3',fg="#fff23b").grid(column=0,row=1)
    e1 = Entry(rt, font=('arialbold', 20), bg='white')
    e1.grid(column=1,row=1)
    e1.insert(0, "0 0 0;0 0 0;0 0 0"+'\n')
    
    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=2)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=2)
    Label(rt, text="Mat B:", font=("arialbold", 20), bg='#1e3eb3', fg="#fff23b").grid(column=0,row=3)
    e2 = Entry(rt, font=('arialbold', 20), bg='white')
    e2.grid(column=1,row=3)
    e2.insert(0, "0 0 0;0 0 0;0 0 0"+'\n')


    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=4)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=4)
    Label(rt, text="Mat C:", font=("arialbold", 20), bg='#1e3eb3', fg="#fff23b").grid(column=0,row=5)
    e3 = Entry(rt, font=('arialbold', 20), bg='white')
    e3.grid(column=1, row=5)
    e3.insert(0, "0 0 0;0 0 0;0 0 0"+'\n')


    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=6)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=6)
    Label(rt, text="Mat D:", font=("arialbold", 20), bg='#1e3eb3', fg="#fff23b").grid(column=0,row=7)
    e4 = Entry(rt, font=('arialbold', 20), bg='white')
    e4.grid(column=1, row=7)
    e4.insert(0, "0 0 0;0 0 0;0 0 0"+'\n')


    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=8)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=8)
    Label(rt, text="Operation:", font=("arialbold", 20),bg='#1e3eb3', fg="#fff23b").grid(column=0, row=9)
    e5 = Entry(rt, font=('arialbold', 20), bg='white')
    e5.grid(column=1, row=9)
    e5.insert(0, "A+B"+'\n')


    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=10)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=10)
    Button(rt, text="Calculate!", font=('arialbold', 20), relief='raised', command=lambda: getValues(e1.get(), e2.get(), e3.get(), e4.get(), e5.get()), bg='#606060').grid(column=1, row=11)

    rt.mainloop()

window()



#1 3 7;4 2 3;1 2 1
#A^3-4*A^2-20*A-35*I
