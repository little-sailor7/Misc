from os import path

import pandas

class Reputation_IP():
    
    def __init__(self,p) -> None:
        
       
        abs_path = path.abspath(p)
        self.count = {}
        content=[]
        with open(f"{abs_path}","r") as file:
            content=file.readlines()
        self.res = []
        
        for i in content:
            self.res.append(i.replace("\n",""))

        
    
    def Counting_them_all(self):
        for i in self.res:
            if not i in self.count:
                self.count[i] = 1
            else:
                self.count[i] += 1
        print(self.count)
    
    def Creating_data(self):
        self.ylabel = [i for i in self.count.keys()]
        
        self.xlabel = [i for i in range(1,max(self.count.values())+1)]
        
        
        self.data = [i for i in self.count.values()]
        
        
    
    def Creating_dataframe_analisis(self):
        self.Dataframe =pandas.DataFrame(
            
            self.data,
            index=self.ylabel,
            columns = ['Ilosc powtorzen']
           
        )
    
    def Showtime(self):
        self.Counting_them_all()
        self.Creating_data()
        self.Creating_dataframe_analisis()
        print(self.Dataframe)


Rep=Reputation_IP("C:\\Users\\littl\\Desktop\\Projects\\Python\\Project\\IP.txt")
Rep.Showtime()
