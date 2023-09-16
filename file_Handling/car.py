class Car():
    Car_name =""
    model_name =""
    car_color =""
    price =""
    
    def Car_details(self):
        print(f"Car name :{self.Car_name}   Car model : {self.model_name}  Car Color : {self.car_color} Car Price : {self.price}")
        
        
car1 = Car()
car1.Car_name ="Mahindra"
car1.model_name = "XQV"
car1.car_color = "Black"
car1.price ="1000000"
car1.Car_details()