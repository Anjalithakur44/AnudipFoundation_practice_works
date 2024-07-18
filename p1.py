#convert seconds into time
ts=float(input("Any number:"))

# print("time in min",tm)
# print("time in hr",th)
if(ts>=0):
     th=0
     tm=0
#    print("time in min",tm)
#    print("time in hr",th)
#    print("time in hr",th)
     if(ts>=60):
         tm=ts//60
         ts=ts%3600
         
     if(ts>=3600):
           th=ts//3600
           ts=th&3600 
     print("time=",th,"hour",tm,"mins",ts,"secs")       
else:
   print("time entered is not positive")

