#Questin10

number = int(input("Enter a number:- "))
if number>1 and number<86400:
    hr = number//3600
    sec= number%3600 
    min = sec//60
    sec = sec%60
    print("hr" ,hr)
    print("min" ,min)
    print("sec" ,sec) 
else:
    print("invalid input")