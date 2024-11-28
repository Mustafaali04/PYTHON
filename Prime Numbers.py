num=int(input("Enter the number:"))
if num>1:
    for i in range(2,(num//2)+1):
        if num%i ==0:
            print("Not a prime")
            break
    else:
        print("Number is a Prime")
else:
    print("Not a Prime")
