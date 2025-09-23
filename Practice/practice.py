
for i in range(101):
    if(i==0):
        print(0)

    elif(i%3==0 and i%5==0):
            print("FIZZ BUZZ")
    elif(i%3==0):
            print("FIZZ")
    elif(i%5==0):
            print("BUZZ")

    else:
            print(i)
#print(num)