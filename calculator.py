class Calculator:
    def _init_(self):
        self.memory=0
        self.current_result=0
    
    def add(self,a,b):
        
        if abs(a) > 1e15 or abs(b) >1e15:
            raise ValueError("Invalid Input")
        self.current_result=a+b
        self.current_result=round(self.current_result,3)
        return self.current_result
    
    def subtract(self,a,b):
       
        if abs(a) > 1e15 or abs(b) >1e15:
            raise ValueError("Invalid Input")
        self.current_result=a-b
        self.current_result=round(self.current_result,3)
        return self.current_result
    
    def multiply(self,a,b):
        
        if abs(a) > 1e15 or abs(b) >1e15:
            raise ValueError("Invalid Input")
        self.current_result=a*b
        self.current_result=round(self.current_result,3)
        return self.current_result
    
    def divide(self,a,b):
        if b==0:
            raise ValueError("Cannot divide by zero")
        if abs(a) > 1e15 or abs(b) >1e15:
            raise ValueError("Invalid Input")
        self.current_result=a/b
        self.current_result=round(self.current_result,3)
        return self.current_result
    
    def clear(self):
        self.current_result=0
    
    def memory_store(self,value):
        self.memory=value

    def memory_recall(self):
        return self.memory
    
    def display(self):
        return self.current_result
        
        


        