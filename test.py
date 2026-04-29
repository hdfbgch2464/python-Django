class Dog:
    def __init__(self,name,age):
        self.age = age;
        self.name = name;
        print(f"{name}-{age}")
    def abc(self):{
        print(self.age)
    }
dog = Dog("大黄",3) 
dog.abc()
        