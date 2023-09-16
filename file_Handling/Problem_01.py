class StudentIDCard:
    name =""
    roll =""
    
    def display(self):
        print(f"name :{self.name}   Roll : {self.roll}")
    
ob1 = StudentIDCard()
ob1.name ="Rana"
ob1.roll = 10
ob1.display()

ob2 = StudentIDCard()
ob2.name ="Juel"
ob2.roll = 11
ob2.display()

ob3 = StudentIDCard()
ob3.name ="Amin"
ob3.roll = 12
ob3.display()

# print(ob1.name)
# print(ob1.roll)

# print(isinstance(ob1,StudentIDCard))