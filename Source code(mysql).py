#MODULES
import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tkinter import *
import mysql.connector as m
import datetime as d
#MODULES
#root window
print("Current Working Directory:", os.getcwd())


dotenv_path = dotenv_path = "C:\\Users\\HP\\PROJECTS\\PETRO PREDICT\\.env"
if os.path.exists(dotenv_path):
    print("✅ Found .enq file!")
    load_dotenv(dotenv_path)
else:
    print("❌ .env file not found at", dotenv_path)

a=m.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)
b=a.cursor()
r=Tk()
r.title('PETRO PREDICT')
def root():
    global f 
    f=Frame(r,)
    f.grid()
    l=Label(f,text='Welcome to Petro Predict',fg='blue',font=('Times',15))
    l.grid(columnspan=2)
    b1=Button(f,text='Predict  ',bg='orange',fg='blue',padx=40,pady=20,command=predict,font=('Times',15))
    b1.grid(row='1',column='0')
    b2=Button(f,text='  Graph',bg='orange',fg='blue',padx=40,pady=20,command=graph,font=('Times',15))
    b2.grid(row='1',column='1')
    b7=Button(f,text='N.Cost  ',padx=40,pady=20,bg='orange',fg='blue',font=('Times',15),command=next_cost)
    b7.grid(row='2',column='0')
    b9=Button(f,text='  Train  ',padx=40,pady=20,bg='orange',fg='blue',font=('Times',15),command=train)
    b9.grid(row='3',column='0')
    b8=Button(f,text='  exit ',padx=50,pady=20,bg='orange',fg='blue',font=('Times',15),command=r.destroy)
    b8.grid(row='3',column='1')
    b10=Button(f,text='N.graph',padx=40,pady=20,bg='orange',fg='blue',font=('Times',15),command=n_graph)
    b10.grid(row='2',column='1')
    b11=Button(f,text='Devolopers',padx=25,pady=20,bg='orange',fg='blue',font=('Times',15),command=devolopers)
    b11.grid(row='4',column='0')
    b12=Button(f,text='  About ',padx=40,pady=20,bg='orange',fg='blue',font=('Times',15),command=about)
    b12.grid(row='4',column='1')
#functions
def predict():
    global k
    f.grid_forget()
    k=Frame(r,)
    k.grid()
    l2=Label(k,text='Choose the type of fuel to predict',fg='blue',font=('Times',15))
    l2.grid(row='0',column='0',columnspan=2)
    b4=Button(k,text='Petrol',padx=40,pady=20,command=petrol,bg='yellow',fg='red',font=('Times',15))
    b5=Button(k,text='Diesel',padx=40,pady=20,command=diesel,bg='black',fg='red',font=('Times',15))
    b6=Button(k,text='speed Petrol',padx=40,pady=20,command=speed_petrol,bg='blue',fg='red',font=('Times',15))
    b4.grid(row='1',column='0')
    b5.grid(row='1',column='1')
    b6.grid(row='1',column='2')
#for petrol(start) 
def petrol():
    k.grid_forget()
    k1=Frame(r,)
    k1.grid()
    p_label=Label(k1,text='enter the cost',font=('Times',15))
    p_label.grid()
    p_entry=Entry(k1,width=40)
    p_entry.grid(row='0',column='1')
    def ok():
        try:
            v=int(p_entry.get())
            b.execute('select * from petrol')
            d=pd.DataFrame(b.fetchall())
            x=d.iloc[:,1:2]
            y=d.iloc[:,0]
            m=LinearRegression()
            m.fit(x,y)
            t=m.predict([[v]])
            str(t)
            k1.grid_forget()
            k2=Frame(r,)
            k2.grid()
            out_label=Label(k2,text='the predicted value is:',font=('Times',15))
            out_label1=Label(k2,text=t,font=('Times',15))
            out_label2=Label(k2,text='L',font=('Times',15))
            out_label.grid()
            out_label1.grid(row='0',column='1')
            out_label2.grid(row='0',column='2')
            def back():
                k2.grid_forget()
                root()
            b8=Button(k2,text='home',padx=20,pady=10,command=back,bg='orange',fg='blue',font=('Times',15))
            b8.grid()
        except:
            k1.grid_forget()
            petrol()
    b7=Button(k1,text='next',padx=20,pady=10,command=ok,bg='orange',fg='blue',font=('Times',15))
    b7.grid()
#for petrol(end)
#for diesel(start)
def diesel():
    k.grid_forget()
    k1=Frame(r,)
    k1.grid()
    p_label=Label(k1,text='enter the cost',font=('Times',15))
    p_label.grid()
    p_entry=Entry(k1,width=40)
    p_entry.grid(row='0',column='1')
    def ok():
        try:
            v=int(p_entry.get())
            b.execute('select * from diesel')
            d=pd.DataFrame(b.fetchall())
            x=d.iloc[:,1:2]
            y=d.iloc[:,0]
            m=LinearRegression()
            m.fit(x,y)
            t=m.predict([[v]])
            str(t)
            k1.grid_forget()
            k2=Frame(r,)
            k2.grid()
            out_label=Label(k2,text='the predicted value is:',font=('Times',15))
            out_label1=Label(k2,text=t,font=('Times',15))
            out_label2=Label(k2,text='L',font=('Times',15))
            out_label.grid()
            out_label1.grid(row='0',column='1')
            out_label2.grid(row='0',column='2')
            def back():
                k2.grid_forget()
                root()
            b8=Button(k2,text='home',padx=20,pady=10,command=back,bg='orange',fg='blue',font=('Times',15))
            b8.grid()
        except:
            k1.grid_forget()
            diesel()
    b7=Button(k1,text='next',padx=20,pady=10,command=ok,bg='orange',fg='blue',font=('Times',15))
    b7.grid()
#for diesel(end)
#for speed petrol(start)
def speed_petrol():
    k.grid_forget()
    k1=Frame(r,)
    k1.grid()
    p_label=Label(k1,text='enter the cost',font=('Times',15))
    p_label.grid()
    p_entry=Entry(k1,width=40)
    p_entry.grid(row='0',column='1')
    def ok():
        try:
            v=int(p_entry.get())
            b.execute('select * from speed')
            d=pd.DataFrame(b.fetchall())
            x=d.iloc[:,1:2]
            y=d.iloc[:,0]
            m=LinearRegression()
            m.fit(x,y)
            t=m.predict([[v]])
            str(t)
            k1.grid_forget()
            k2=Frame(r,)
            k2.grid()
            out_label=Label(k2,text='the predicted value is:',font=('Times',15))
            out_label1=Label(k2,text=t,font=('Times',15))
            out_label2=Label(k2,text='L',font=('Times',15))
            out_label.grid()
            out_label1.grid(row='0',column='1')
            out_label2.grid(row='0',column='2')
            def back():
                k2.grid_forget()
                root()
            b8=Button(k2,text='home',padx=20,pady=10,command=back,bg='orange',fg='blue',font=('Times',15))
            b8.grid()
        except:
            k1.grid_forget()
            speed_petrol()
    b7=Button(k1,text='next',padx=20,pady=10,command=ok,bg='orange',fg='blue',font=('Times',15))
    b7.grid()
def graph():
    f.grid_forget()
    j=Frame(r,)
    j.grid()
    def back1():
        plt.close()
        j.grid_forget()
        root()
    b13=Button(j,text='home',padx=40,pady=20,command=back1,bg='orange',fg='blue',font=('Times',15))
    b13.grid()
    b.execute('select * from petrol')
    d=pd.DataFrame(b.fetchall())
    b.execute('select * from diesel')
    d1=pd.DataFrame(b.fetchall())
    b.execute('select * from speed')
    d2=pd.DataFrame(b.fetchall())
    z=d[0]
    z1=d[1]
    plt.scatter(z1,z,color='yellow')
    n=d1[0]
    n1=d1[1]
    plt.scatter(n1,n,color='green')
    e=d2[0]
    e1=d2[1]
    plt.scatter(e1,e,color='blue')
    plt.xlabel('cost')
    plt.ylabel('volume')
    plt.legend(['petrol','diesel','speed petrol'],loc='upper left')
    plt.show()
#next cost(start)
def next_cost():
    global h
    f.grid_forget()
    h=Frame(r,)
    h.grid()
    la=Label(h,text='Choose fuel type',font=('Times',15),fg='blue')
    la.grid()
    b14=Button(h,text='Petrol',padx=40,pady=20,bg='yellow',fg='blue',font=('Times',15),command=petr)
    b14.grid(row='1',column='0')
    b15=Button(h,text='Diesel',padx=40,pady=20,bg='black',fg='blue',font=('Times',15),command=diese)
    b15.grid(row='1',column='1')
    b16=Button(h,text='Speed Petrol',padx=40,pady=20,bg='blue',fg='red',font=('Times',15),command=speed_petrol1)
    b16.grid(row='1',column='2')
def petr():
    h.grid_forget()
    h1=Frame(r,)
    h1.grid()
    la=Label(h1,text='input year',font=('Times',15))
    la.grid()
    en=Entry(h1,width=40)
    en.grid(row='0',column='1')
    def ok1():
        try:
            v=int(en.get())
            if len(str(v))!=4 :
                raise ValueError
            b.execute('select * from pet')
            d=pd.DataFrame(b.fetchall())
            x=d.iloc[:,[0]]
            y=d.iloc[:,1]
            m=LinearRegression()
            m.fit(x,y)
            t=m.predict([[v]])
            str(t)
            h1.grid_forget()    
            k2=Frame(r,)
            k2.grid()
            out_label=Label(k2,text='Average petrol cost(all India) is:',font=('Times',15))
            out_label1=Label(k2,text=t,font=('Times',15))
            out_label2=Label(k2,text='L',font=('Times',15))
            out_label.grid()
            out_label1.grid(row='0',column='1')
            out_label2.grid(row='0',column='2')
            def back():
                k2.grid_forget()
                root()
            b8=Button(k2,text='home',padx=20,pady=10,command=back,bg='orange',fg='blue',font=('Times',15))
            b8.grid()
        except:
            h1.grid_forget()
            petr()   
    b7=Button(h1,text='next',padx=20,pady=10,command=ok1,bg='orange',fg='blue',font=('Times',15))
    b7.grid()
def diese():
    h.grid_forget()
    h1=Frame(r,)
    h1.grid()
    la=Label(h1,text='input year',font=('Times',15))
    la.grid()
    en=Entry(h1,width=40)
    en.grid(row='0',column='1')
    def ok1():
        try:
            v=int(en.get())
            if len(str(v))!=4 :
                raise ValueError
            b.execute('select * from dies')
            d=pd.DataFrame(b.fetchall())
            x=d.iloc[:,1:2]
            y=d.iloc[:,0]
            m=LinearRegression()
            m.fit(x,y)
            t=m.predict([[v]])
            str(t)
            h1.grid_forget()
            k2=Frame(r,)
            k2.grid()
            out_label=Label(k2,text='Average diesel cost(all India) is:',font=('Times',15))
            out_label1=Label(k2,text=t,font=('Times',15))
            out_label2=Label(k2,text='L',font=('Times',15))
            out_label.grid()
            out_label1.grid(row='0',column='1')
            out_label2.grid(row='0',column='2')
            def back():
                k2.grid_forget()
                root()
            b8=Button(k2,text='home',padx=20,pady=10,command=back,bg='orange',fg='blue',font=('Times',15))
            b8.grid()
        except:
            h1.grid_forget()
            diese()
    b7=Button(h1,text='next',padx=20,pady=10,command=ok1,bg='orange',fg='blue',font=('Times',15))
    b7.grid()
def speed_petrol1():
    h.grid_forget()
    h1=Frame(r,)
    h1.grid()
    la=Label(h1,text='input year',font=('Times',15))
    la.grid()
    en=Entry(h1,width=40)
    en.grid(row='0',column='1')
    def ok1():
        try:
            v=int(en.get())
            if len(str(v))!=4 :
                    raise ValueError
            b.execute('select * from speed_p')
            d=pd.DataFrame(b.fetchall())
            x=d.iloc[:,[0]]
            y=d.iloc[:,1]
            m=LinearRegression()
            m.fit(x,y)
            t=m.predict([[v]])
            str(t)
            h1.grid_forget()
            k2=Frame(r,)
            k2.grid()
            out_label=Label(k2,text='Average speed petrol cost(all India) is:',font=('Times',15))
            out_label1=Label(k2,text=t,font=('Times',15))
            out_label2=Label(k2,text='L',font=('Times',15))
            out_label.grid()
            out_label1.grid(row='0',column='1')
            out_label2.grid(row='0',column='2')
            def back():
                k2.grid_forget()
                root()
            b8=Button(k2,text='home',padx=20,pady=10,command=back,bg='orange',fg='blue',font=('Times',15))
            b8.grid()
        except:
            h1.grid_forget()
            speed_petrol1()
    b7=Button(h1,text='next',padx=20,pady=10,command=ok1,bg='orange',fg='blue',font=('Times',15))
    b7.grid()

#next cost(end)
#model training(start)
def train():
    global g
    f.grid_forget()
    g=Frame(r,)
    g.grid()
    l2=Label(g,text='Choose fuel type',fg='blue',font=('Times',15))
    l2.grid(row='0',column='0',columnspan=2)
    b4=Button(g,text='Petrol',padx=40,pady=20,bg='yellow',fg='red',font=('Times',15),command=pet)
    b5=Button(g,text='Diesel',padx=40,pady=20,bg='black',fg='red',font=('Times',15),command=dise)
    b6=Button(g,text='speed Petrol',padx=40,pady=20,bg='blue',fg='red',font=('Times',15),command=speed)
    b4.grid(row='1',column='0')
    b5.grid(row='1',column='1')
    b6.grid(row='1',column='2')
def pet():
    g.grid_forget()
    g1=Frame(r,)
    g1.grid()
    lab=Label(g1,text='Insert cost',font=('Times',15))
    lab.grid()
    ent=Entry(g1,width=40)
    ent.grid(row='0',column='1')
    lab1=Label(g1,text='Insert volume sold',font=('Times',15))
    lab1.grid(row='1',column='0')
    ent1=Entry(g1,width=40)
    ent1.grid(row='1',column='1')
    def ok1():
        t=(float(ent1.get()),int(ent.get()))
        k='insert into petrol values(%s,%s)'
        b.execute(k,t)
        a.commit()
        g1.grid_forget()
        g11=Frame(r,)
        g11.grid()
        labb=Label(g11,text='Sucessfully inserted the values',font=('Times',15))
        labb.grid()
        def back2():
            g11.grid_forget()
            root()
        b15=Button(g11,text='home',padx=20,pady=10,command=back2,bg='orange',fg='blue',font=('Times',15))
        b15.grid()
    def back4():
        g1.grid_forget()
        root()
    b17=Button(g1,text='Back',padx=20,pady=10,command=back4,bg='orange',fg='blue',font=('Times',15))
    b17.grid(row='2',column='2')
    b16=Button(g1,text='Train',padx=20,pady=10,command=ok1,bg='orange',fg='blue',font=('Times',15))
    b16.grid(row='2',column='1')
def dise():
    g.grid_forget()
    g1=Frame(r,)
    g1.grid()
    lab=Label(g1,text='Insert cost',font=('Times',15))
    lab.grid()
    ent=Entry(g1,width=40)
    ent.grid(row='0',column='1')
    lab1=Label(g1,text='Insert volume sold',font=('Times',15))
    lab1.grid(row='1',column='0')
    ent1=Entry(g1,width=40)
    ent1.grid(row='1',column='1')
    def ok1():
        try:
            t=(float(ent1.get()),int(ent.get()))
            k='insert into diesel values(%s,%s)'
            b.execute(k,t)
            a.commit()
            g1.grid_forget()
            g11=Frame(r,)
            g11.grid()
            labb=Label(g11,text='Sucessfully inserted the values',font=('Times',15))
            labb.grid()
            def back2():
                g11.grid_forget()
                root()
            b15=Button(g11,text='home',padx=20,pady=10,command=back2,bg='orange',fg='blue',font=('Times',15))
            b15.grid()
        except:
            g1.grid_forget()
            dise()
    def back4():
        g1.grid_forget()
        root()
    b17=Button(g1,text='Back',padx=20,pady=10,command=back4,bg='orange',fg='blue',font=('Times',15))
    b17.grid(row='2',column='2')
    b16=Button(g1,text='Train',padx=20,pady=10,command=ok1,bg='orange',fg='blue',font=('Times',15))
    b16.grid(row='2',column='1')
def speed():
    g.grid_forget()
    g1=Frame(r,)
    g1.grid()
    lab=Label(g1,text='Insert cost',font=('Times',15))
    lab.grid()
    ent=Entry(g1,width=40)
    ent.grid(row='0',column='1')
    lab1=Label(g1,text='insert volume sold',font=('Times',15))
    lab1.grid(row='1',column='0')
    ent1=Entry(g1,width=40)
    ent1.grid(row='1',column='1')
    def ok1():
        try:
            t=(float(ent1.get()),int(ent.get()))
            k='insert into speed values(%s,%s)'
            b.execute(k,t)
            a.commit()
            g1.grid_forget()
            g11=Frame(r,)
            g11.grid()
            labb=Label(g11,text='Sucessfully inserted the values',font=('Times',15))
            labb.grid()
            def back2():
                g11.grid_forget()
                root()
            b15=Button(g11,text='home',padx=20,pady=10,command=back2,bg='orange',fg='blue',font=('Times',15))
            b15.grid()
        except:
            g1.grid_forget()
            speed()
    def back4():
        g1.grid_forget()
        root()
    b17=Button(g1,text='Back',padx=20,pady=10,command=back4,bg='orange',fg='blue',font=('Times',15))
    b17.grid(row='2',column='2')
    b16=Button(g1,text='Train',padx=20,pady=10,command=ok1,bg='orange',fg='blue',font=('Times',15))
    b16.grid(row='2',column='1')
#model training(end)
#yearly cost graph(start)
def n_graph():
    f.grid_forget()
    f1=Frame(r,)
    f1.grid()
    def back2():
        plt.close()
        f1.grid_forget()
        root()
    b18=Button(f1,text='back',padx=20,pady=10,command=back2,bg='orange',fg='blue',font=('Times',15))
    b18.grid()

    # Query and check main table
    b.execute('select * from yearly')
    d = pd.DataFrame(b.fetchall())
    if d.empty or d.shape[1] < 2:
        from tkinter import messagebox
        messagebox.showerror("Data Error", "No data or not enough columns in table 'yearly'.")
        return
    x = d.iloc[:, [0]]
    y = d.iloc[:, 1]

    # Query and check others similarly:
    b.execute('select * from dies')
    d1 = pd.DataFrame(b.fetchall())
    if d1.empty or d1.shape[1] < 2:
        messagebox.showerror("Data Error", "No data or not enough columns in table 'dies'.")
        return
    v = d1.iloc[:, [0]]
    p = d1.iloc[:, 1]

    b.execute('select * from speed_p')
    d2 = pd.DataFrame(b.fetchall())
    if d2.empty or d2.shape[1] < 2:
        messagebox.showerror("Data Error", "No data or not enough columns in table 'speed_p'.")
        return
    l = d2.iloc[:, [0]]
    k = d2.iloc[:, 1]

    plt.plot(x, y, color='red')
    plt.plot(v, p, color='blue')
    plt.plot(l, k, color='green')
    plt.xlabel('year')
    plt.ylabel('rate')
    plt.legend(['petrol','diesel','speed petrol'], loc='upper left')
    plt.show()

#yearly cost graph(end)
#devolopers info(start)
def devolopers():
    f.grid_forget()
    j=Frame(r,)
    j.grid()
    m1=Label(j,text='Pradosh.G',fg='blue',font=('Times',15))   
    m1.grid(row='2',column='0')
   
    def back3():
        j.grid_forget()
        root()
    b13=Button(j,text='home',padx=20,pady=10,command=back3,bg='orange',fg='blue',font=('Times',15))
    b13.grid(row='4',column='1')
#devolopers info(end)
#About system(start)
def about():
    f.grid_forget()
    x=Frame(r,)
    x.grid()
    l1=Label(x,text='USER-GUIDE',fg='blue',font=('Times',15))
    l1.grid()
    l2=Label(x,text='Predict - Enter the price of fuel estimated to be sold to get the minimum volume required to store',fg='blue',font=('Times',15))
    l2.grid()
    l3=Label(x,text='Graph - Graphical representation of volume and cost  ',fg='blue',font=('Times',15))
    l3.grid()
    l4=Label(x,text='N.Cost- Cost of fuel for year provided',fg='blue',font=('Times',15))
    l4.grid()
    l5=Label(x,text='N.Graph- Graphical comparison of fuel price from 2000 to 2024',fg='blue',font=('Times',15))
    l5.grid()
    l6=Label(x,text='Insert- To enter the cost and volume sold for the machine to learn',fg='blue',font=('Times',15))
    l6.grid()
    l7=Label(x,text='Exit- To exit home screen',fg='blue',font=('Times',15))
    l7.grid()
    def back4():
        x.grid_forget()
        root()
    b18=Button(x,text='home',padx=30,pady=20,command=back4,bg='orange',fg='blue',font=('Times',15))
    b18.grid(row='7',column='1')
def main():
    F=Frame(r,)
    F.grid()
    def show():
        if value.get():
            l4.config(show='')
        else:
            l4.config(show='*') 
#login box
    t=Label(F,text='LOGIN ',fg='blue',font=('Arial',20))
    t.grid(row='0',column='0',columnspan=2)
    l1=Label(F,text='USER NAME',fg='blue',font=('Times',15))
    l1.grid(row='1',column='0')
    l2=Entry(F,width=30)
    l2.grid(row='1',column='1')
#pasword box
    l3=Label(F,text='PASSWORD',fg='blue',font=('Times',15))
    l3.grid(row='2',column='0')
    l4=Entry(F,width=30,show='*')
    l4.grid(row='2',column='1')
# Show password button
    value=BooleanVar()
    check=Checkbutton(F,variable=value,command=show)
    check.grid(row='2',column='2')
    def login():
        x=l2.get()
        y=l4.get()
        if x=='bvm' and y=='123':
            F.grid_forget()
            date=str(d.datetime.now())
            day=date[0:10]
            time=date[11::]
            b.execute('insert into entries values(%s,%s)',(day,time))
            a.commit()
            root()
        
        else:
            F.grid_forget()
            g=Frame(r,)
            g.grid()
            l8=Label(g,text='ACCESS DENIED 💀',fg='RED',font=('Arial',25))
            l8.grid()
            def back():
                g.grid_forget()
                main()
            
            b8=Button(g,text='Try again',padx=20,pady=10,command=back,bg='orange',fg='blue',font=('Times',15))
            b8.grid(row='1',column='0')
            b9=Button(g,text='Close',padx=20,pady=10,command=r.destroy,bg='orange',fg='blue',font=('Times',15))
            b9.grid(row='1',column='1')
    b2=Button(F,text='OK',padx=20,pady=10,command=login,bg='orange',fg='blue',font=('Times',15))
    b2.grid(row='3',column='1')
main()
