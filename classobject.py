class Class:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b    
    def sub(self):
        return self.a-self.b 
if __name__ == "__main__":
    a = int (input("Enter a : "))     
    b = int (input("Enter b : "))         
    c = Class(a,b) 
    print(c.add())
    print(c.sub())