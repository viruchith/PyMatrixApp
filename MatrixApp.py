import numpy as np
from numpy import dot
from numpy.linalg import matrix_power
from tkinter import *
rWin = None


class Matrix(object):
    def __init__(self, mat):
      self.mat = mat

    def __add__(self, other):
        return Matrix(self.mat+other.mat)

    def __sub__(self, other):
        return Matrix(self.mat-other.mat)

    def __mul__(self, other):
        return Matrix(dot(self.mat, other.mat))

    def __pow__(self, other):
        return Matrix(matrix_power(self.mat, other.mat))

    def __str__(self):
        return str(self.mat)


def stringConvert(s):
    import re
    t = "ans="
    s = re.sub(r'(\d+)', r'Matrix(\1)', s)
    s = s.replace("^", "**")
    s = t+s
    print(s)
    return s


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
    result = str(result)
    rWin = Tk()
    rWin.geometry("150x150")
    rWin.title("Result")
    Label(rWin, text=result, font=("arialbold", 20)).pack()
    rWin.mainloop()


def windowDestroy():
    global rWin
    try:
        rWin.destroy()
    except Exception as e:
        pass


def calculation(A, B, C, D, I, OP, ans):
    register = {"A": A, "B": B, "C": C, "D": D,
                "I": I, "OP": OP, "ans": ans, "Matrix": Matrix}
    exec(OP, register)
    ans = register["ans"]
    windowDestroy()
    resultDisp(ans)


def getValues(a="0 0 0;0 0 0;0 0 0", b="0 0 0;0 0 0;0 0 0", c="0 0 0;0 0 0;0 0 0", d="0 0 0;0 0 0;0 0 0", op="None"):
    mat1 = np.array(intConvert(a))
    mat2 = Matrix(np.array(intConvert(b)))
    mat3 = Matrix(np.array(intConvert(c)))
    mat4 = Matrix(np.array(intConvert(d)))
    size = mat1.shape
    mat1 = Matrix(np.array(intConvert(a)))
    matid = Matrix(np.identity(size[0], dtype=int))
    op = stringConvert(op)
    calculation(mat1, mat2, mat3, mat4, matid, op, "ans=")


def window():
    rt = Tk()
    rt.title("MatrixOps")
    rt.configure(bg="#1e3eb3")
    rt.geometry("500x530")

    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=0)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=0)
    Label(rt, text="Mat A:", font=("arialbold", 20),
          bg='#1e3eb3', fg="#fff23b").grid(column=0, row=1)
    e1 = Entry(rt, font=('arialbold', 20), bg='white')
    e1.grid(column=1, row=1)
    e1.insert(0, "0 0 0;0 0 0;0 0 0"+'\n')

    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=2)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=2)
    Label(rt, text="Mat B:", font=("arialbold", 20),
          bg='#1e3eb3', fg="#fff23b").grid(column=0, row=3)
    e2 = Entry(rt, font=('arialbold', 20), bg='white')
    e2.grid(column=1, row=3)
    e2.insert(0, "0 0 0;0 0 0;0 0 0"+'\n')

    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=4)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=4)
    Label(rt, text="Mat C:", font=("arialbold", 20),
          bg='#1e3eb3', fg="#fff23b").grid(column=0, row=5)
    e3 = Entry(rt, font=('arialbold', 20), bg='white')
    e3.grid(column=1, row=5)
    e3.insert(0, "0 0 0;0 0 0;0 0 0"+'\n')

    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=6)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=6)
    Label(rt, text="Mat D:", font=("arialbold", 20),
          bg='#1e3eb3', fg="#fff23b").grid(column=0, row=7)
    e4 = Entry(rt, font=('arialbold', 20), bg='white')
    e4.grid(column=1, row=7)
    e4.insert(0, "0 0 0;0 0 0;0 0 0"+'\n')

    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=8)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=8)
    Label(rt, text="Operation:", font=("arialbold", 20),
          bg='#1e3eb3', fg="#fff23b").grid(column=0, row=9)
    e5 = Entry(rt, font=('arialbold', 20), bg='white')
    e5.grid(column=1, row=9)
    e5.insert(0, "A+B"+'\n')

    Label(rt, text="\n", bg='#1e3eb3').grid(column=0, row=10)
    Label(rt, text="\n", bg='#1e3eb3').grid(column=1, row=10)
    Button(rt, text="Calculate!", font=('arialbold', 20), relief='raised', command=lambda: getValues(
        e1.get(), e2.get(), e3.get(), e4.get(), e5.get()), bg='#606060').grid(column=1, row=11)

    rt.mainloop()


window()
