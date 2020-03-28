from tkinter import *
import COVID19Py as pack
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

master = Tk()

class fir:
    
    sp=[]
    data=pd.read_csv("C:/Users/Harshan/Desktop/jupyter/time_series_covid_19_confirmed.csv")
    x=[]
    def __init__(self,master):
        
        for i in range(1,66):
            self.x.insert(i,i)
        
        #self.data=pd.read_csv("C:/Users/Harshan/Desktop/jupyter/time_series_covid_19_confirmed.csv")
        self.c=0
        for i in self.data["Country/Region"]:
            self.sp.insert(self.c,i)
            self.c=self.c+1
        
        master.geometry('500x500')
        Label(master, text='First Name:  ').grid(row=0,column=0) 
        #Label(master, text='Last Name').grid(row=1) 
        self.e1 = Entry(master) 
        #e2 = Entry(master) 
        self.e1.grid(row=0, column=2) 
        #e2.grid(row=1, column=0) 
        self.btn = Button(master, text = 'serch',command=self.funcky).grid(row=1,column=2)  
    
    def funcky(self):
        
        self.name=str(self.e1.get())
        self.index=self.indexret(self.name)
        #print(self.index)
        self.y0=self.data.loc[self.index]
        self.y=np.array(self.y0[4:])
        plt.plot(self.x,self. y) 
        plt.xlabel('x - axis : no of days') 
        plt.ylabel('y - axis : no of patients') 
        plt.title(self.name+" corona virus!") 
        plt.show() 
    
    def indexret(self,name):
        for i in range(0,len(self.sp)):
            if(self.sp[i]==self.name):
                return i
    
def st():
    obj=fir(master)
    master.mainloop()
    
st()