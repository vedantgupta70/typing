from time import *
import random as r
def mistake(partest,usertext):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertext[i]:
                error = error + 1
        except:
            error = error + 1
    return error
def speep_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R=round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
test = ["I am vedant gupta", "I am from Ratanpur", "Banglore is a good place"]
test1 = r.choice(test)
print(test1)
print()
print()
time_1=time()
testinput=input("Enter : ")
time_2=time()
print('Speed',speep_time(time_1,time_2,testinput,),"w/sec")
print('error',mistake(test1,testinput))
