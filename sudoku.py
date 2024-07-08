from tkinter import *
from tkinter.messagebox import *
from random import *

win=Tk()
win.title("Sudoku Solver")
win.geometry('285x380')

C=Canvas(win)
l1=C.create_line(98,350,98,50,width=2)
l2=C.create_line(188,350,188,50,width=2)
l3=C.create_line(10,139,275,139,width=2)
l4=C.create_line(10,229,275,229,width=2)
C.pack()

b1=Entry(win,font=1,width=2)
b1.place(x=10,y=50)
b2=Entry(win,font=1,width=2)
b2.place(x=40,y=50)
b3=Entry(win,font=1,width=2)
b3.place(x=70,y=50)
b4=Entry(win,font=1,width=2)
b4.place(x=100,y=50)
b5=Entry(win,font=1,width=2)
b5.place(x=130,y=50)
b6=Entry(win,font=1,width=2)
b6.place(x=160,y=50)
b7=Entry(win,font=1,width=2)
b7.place(x=190,y=50)
b8=Entry(win,font=1,width=2)
b8.place(x=220,y=50)
b9=Entry(win,font=1,width=2)
b9.place(x=250,y=50)
b10=Entry(win,font=1,width=2)
b10.place(x=10,y=80)
b11=Entry(win,font=1,width=2)
b11.place(x=40,y=80)
b12=Entry(win,font=1,width=2)
b12.place(x=70,y=80)
b13=Entry(win,font=1,width=2)
b13.place(x=100,y=80)
b14=Entry(win,font=1,width=2)
b14.place(x=130,y=80)
b15=Entry(win,font=1,width=2)
b15.place(x=160,y=80)
b16=Entry(win,font=1,width=2)
b16.place(x=190,y=80)
b17=Entry(win,font=1,width=2)
b17.place(x=220,y=80)
b18=Entry(win,font=1,width=2)
b18.place(x=250,y=80)
b19=Entry(win,font=1,width=2)
b19.place(x=10,y=110)
b20=Entry(win,font=1,width=2)
b20.place(x=40,y=110)
b21=Entry(win,font=1,width=2)
b21.place(x=70,y=110)
b22=Entry(win,font=1,width=2)
b22.place(x=100,y=110)
b23=Entry(win,font=1,width=2)
b23.place(x=130,y=110)
b24=Entry(win,font=1,width=2)
b24.place(x=160,y=110)
b25=Entry(win,font=1,width=2)
b25.place(x=190,y=110)
b26=Entry(win,font=1,width=2)
b26.place(x=220,y=110)
b27=Entry(win,font=1,width=2)
b27.place(x=250,y=110)
b28=Entry(win,font=1,width=2)
b28.place(x=10,y=140)
b29=Entry(win,font=1,width=2)
b29.place(x=40,y=140)
b30=Entry(win,font=1,width=2)
b30.place(x=70,y=140)
b31=Entry(win,font=1,width=2)
b31.place(x=100,y=140)
b32=Entry(win,font=1,width=2)
b32.place(x=130,y=140)
b33=Entry(win,font=1,width=2)
b33.place(x=160,y=140)
b34=Entry(win,font=1,width=2)
b34.place(x=190,y=140)
b35=Entry(win,font=1,width=2)
b35.place(x=220,y=140)
b36=Entry(win,font=1,width=2)
b36.place(x=250,y=140)
b37=Entry(win,font=1,width=2)
b37.place(x=10,y=170)
b38=Entry(win,font=1,width=2)
b38.place(x=40,y=170)
b39=Entry(win,font=1,width=2)
b39.place(x=70,y=170)
b40=Entry(win,font=1,width=2)
b40.place(x=100,y=170)
b41=Entry(win,font=1,width=2)
b41.place(x=130,y=170)
b42=Entry(win,font=1,width=2)
b42.place(x=160,y=170)
b43=Entry(win,font=1,width=2)
b43.place(x=190,y=170)
b44=Entry(win,font=1,width=2)
b44.place(x=220,y=170)
b45=Entry(win,font=1,width=2)
b45.place(x=250,y=170)
b46=Entry(win,font=1,width=2)
b46.place(x=10,y=200)
b47=Entry(win,font=1,width=2)
b47.place(x=40,y=200)
b48=Entry(win,font=1,width=2)
b48.place(x=70,y=200)
b49=Entry(win,font=1,width=2)
b49.place(x=100,y=200)
b50=Entry(win,font=1,width=2)
b50.place(x=130,y=200)
b51=Entry(win,font=1,width=2)
b51.place(x=160,y=200)
b52=Entry(win,font=1,width=2)
b52.place(x=190,y=200)
b53=Entry(win,font=1,width=2)
b53.place(x=220,y=200)
b54=Entry(win,font=1,width=2)
b54.place(x=250,y=200)
b55=Entry(win,font=1,width=2)
b55.place(x=10,y=230)
b56=Entry(win,font=1,width=2)
b56.place(x=40,y=230)
b57=Entry(win,font=1,width=2)
b57.place(x=70,y=230)
b58=Entry(win,font=1,width=2)
b58.place(x=100,y=230)
b59=Entry(win,font=1,width=2)
b59.place(x=130,y=230)
b60=Entry(win,font=1,width=2)
b60.place(x=160,y=230)
b61=Entry(win,font=1,width=2)
b61.place(x=190,y=230)
b62=Entry(win,font=1,width=2)
b62.place(x=220,y=230)
b63=Entry(win,font=1,width=2)
b63.place(x=250,y=230)
b64=Entry(win,font=1,width=2)
b64.place(x=10,y=260)
b65=Entry(win,font=1,width=2)
b65.place(x=40,y=260)
b66=Entry(win,font=1,width=2)
b66.place(x=70,y=260)
b67=Entry(win,font=1,width=2)
b67.place(x=100,y=260)
b68=Entry(win,font=1,width=2)
b68.place(x=130,y=260)
b69=Entry(win,font=1,width=2)
b69.place(x=160,y=260)
b70=Entry(win,font=1,width=2)
b70.place(x=190,y=260)
b71=Entry(win,font=1,width=2)
b71.place(x=220,y=260)
b72=Entry(win,font=1,width=2)
b72.place(x=250,y=260)
b73=Entry(win,font=1,width=2)
b73.place(x=10,y=290)
b74=Entry(win,font=1,width=2)
b74.place(x=40,y=290)
b75=Entry(win,font=1,width=2)
b75.place(x=70,y=290)
b76=Entry(win,font=1,width=2)
b76.place(x=100,y=290)
b77=Entry(win,font=1,width=2)
b77.place(x=130,y=290)
b78=Entry(win,font=1,width=2)
b78.place(x=160,y=290)
b79=Entry(win,font=1,width=2)
b79.place(x=190,y=290)
b80=Entry(win,font=1,width=2)
b80.place(x=220,y=290)
b81=Entry(win,font=1,width=2)
b81.place(x=250,y=290)

b=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,b81]
us=[]
sl=[]

#seperating the values into each grid
g1=[b1,b2,b3,b10,b11,b12,b19,b20,b21]
g2=[b4,b5,b6,b13,b14,b15,b22,b23,b24]
g3=[b7,b8,b9,b16,b17,b18,b25,b26,b27]
g4=[b28,b29,b30,b37,b38,b39,b46,b47,b48]
g5=[b31,b32,b33,b40,b41,b42,b49,b50,b51]
g6=[b34,b35,b36,b43,b44,b45,b52,b53,b54]
g7=[b55,b56,b57,b64,b65,b66,b73,b74,b75]
g8=[b58,b59,b60,b67,b68,b69,b76,b77,b78]
g9=[b61,b62,b63,b70,b71,b72,b79,b80,b81]
g=[g1,g2,g3,g4,g5,g6,g7,g8,g9]

#row lists
r1=[b1,b10,b19,b28,b37,b46,b55,b64,b73]
r2=[b2,b11,b20,b29,b38,b47,b56,b65,b74]
r3=[b3,b12,b21,b30,b39,b48,b57,b66,b75]
r4=[b4,b13,b22,b31,b40,b49,b58,b67,b76]
r5=[b5,b14,b23,b32,b41,b50,b59,b68,b77]
r6=[b6,b15,b24,b33,b42,b51,b60,b69,b78]
r7=[b7,b16,b25,b34,b43,b52,b61,b70,b79]
r8=[b8,b17,b26,b35,b44,b53,b62,b71,b80]
r9=[b9,b18,b27,b36,b45,b54,b63,b72,b81]
r=[r1,r2,r3,r4,r5,r6,r7,r8,r9]

#column lists
c1=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
c2=[b10,b11,b12,b13,b14,b15,b16,b17,b18]
c3=[b19,b20,b21,b22,b23,b24,b25,b26,b27]
c4=[b28,b29,b30,b31,b32,b33,b34,b35,b36]
c5=[b37,b38,b39,b40,b41,b42,b43,b44,b45]
c6=[b46,b47,b48,b49,b50,b51,b52,b53,b54]
c7=[b55,b56,b57,b58,b59,b60,b61,b62,b63]
c8=[b64,b65,b66,b67,b68,b69,b70,b71,b72]
c9=[b73,b74,b75,b76,b77,b78,b79,b80,b81]
c=[c1,c2,c3,c4,c5,c6,c7,c8,c9]


def solution():
    sl=[] #list of filled indexes 
    us=[] #list of empty indexes
    for i in b:
        if i.get()=='':
            us.append(i) 
        else:
            sl.append(i)
    #for k in range(0,len(us)):
    #    print(us[k])

    if len(us)>64: # a sudoku puzzle must have a minimum of 17 values to be solvable
        nw=Toplevel(win)
        nw.title("Error")
        t=Label(nw,text="Unable to solve as sudoku must have a minimum of 17 filled values. TRY AGAIN.")
        t.pack()
    else:
        for p in g:
            val=[1,2,3,4,5,6,7,8,9]
            ent_val=[] #list of values in the grid
            for q in p: #looping through each grid
                if q.get()!='': #empty values in a grid
                    ent_val.append(int(q.get()))
            #print(ent_val)
            for d in ent_val:
                val.remove(d)
            for q in p:
                if q.get()=='':
                    v=choice(val)
                    q.insert(INSERT,v)
                    val.remove(v)


sol=Button(win,text="SOLVE",command=lambda: solution(),bg="green",fg="white",height=1,width=6)
sol.place(x=30,y=330)
q=Button(win,text="QUIT",command=win.destroy,bg="red",fg="white",height=1,width=6)
q.place(x=210,y=330)


win.mainloop()