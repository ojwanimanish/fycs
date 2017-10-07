
num=65
for i in range(0,5,1):
    for j in range(i+1):
        ch=chr(num)
        print(ch,end="  ")
        num=num+1
    print("\r")


