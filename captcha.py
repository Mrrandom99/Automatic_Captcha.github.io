import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "123456789"

all = upper + number
lenght = 5
while True:
        captcha = "".join(random.sample(all,lenght))
        print ("The captcha is:",captcha)
        
        operation = str(input("Enter captcha:"))
        
        if operation == captcha:
            print ("Done")
            
        else:
            print ("Invalid Captcha")
            