# 1.2 write a program that determines weather the year ended by the uses is a leap year entered by the uses is a leap year or not using if-elif-else statements.

def CheckLeap(Year):    
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  else:  
    print ("Given Year is not a leap Year")  
Year = int(input("Enter the number: "))  
CheckLeap(Year)