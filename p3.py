cp=float(input("enter cost price="))
sp=float(input("enter selling price="))
if(cp<0 or sp<0):
    print("Entered prices are not valid")
else:
    if(cp>sp):
        print("Loss=",(cp-sp))
    elif(sp>cp):
        print("Profit=",(sp-cp))
    else:
        print("Neither profit nor loss")
print("end")