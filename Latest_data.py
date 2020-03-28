from tkinter import *
import COVID19Py as pack


master = Tk()

class fir:
    def __init__(self,master):
        master.geometry('500x500')
        Label(master, text='First Name:  ').grid(row=0,column=0) 
        #Label(master, text='Last Name').grid(row=1) 
        self.e1 = Entry(master) 
        #e2 = Entry(master) 
        self.e1.grid(row=0, column=2) 
        #e2.grid(row=1, column=0) 
        self.btn = Button(master, text = 'serch',command=self.funcky).grid(row=1,column=2)  
    
    def funcky(self):
        name=self.e1.get()
        id="";country="";country_code="";c_pop="";lst_up="";lat="";long="";conf="";death=""
        ds=pack.COVID19(data_source="jhu")
        cod=ds.getAll()
        for i in cod["locations"]:
            if(i["country"]==name):
                #print(i)
                id=i["id"]
                country=i["country"]
                country_code=i["country_code"]
                c_pop=i["country_population"]
                lst_up=i["last_updated"]
                lat=i["coordinates"]["latitude"]
                long=i["coordinates"]["longitude"]
                conf=i["latest"]["confirmed"]
                death=i["latest"]["deaths"]
        
        id="id : "+str(id)
        country="country : "+country
        country_code="country_code : "+country_code
        c_pop="country_pop : "+str(c_pop)
        lst_up="last_update : "+lst_up
        lat="latitude : "+lat
        long="longitude : "+long
        conf="confirmed : "+str(conf)
        death="deaths : "+str(death)
        
        Label(master, text=id).grid(row=3,column=0) 
        Label(master, text=country).grid(row=4,column=0) 
        Label(master, text=country_code).grid(row=5,column=0) 
        
        Label(master, text=c_pop).grid(row=6,column=0) 
        Label(master, text=lst_up).grid(row=7,column=0) 
        Label(master, text=lat).grid(row=8,column=0) 
        
        Label(master, text=long).grid(row=9,column=0) 
        Label(master, text=conf).grid(row=10,column=0) 
        Label(master, text=death).grid(row=11,column=0) 
        

def st():
    obj=fir(master)
    master.mainloop()
    
st()