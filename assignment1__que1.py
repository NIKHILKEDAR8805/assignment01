num = int(input("enter number :"))
n1,n2=0,1
sum=0
if num<=0:
    print("enter num greater than zero")
else:
    print("fibonacci series :",end="")
    for i in range(0,num):
        n1=n2
        n2=sum
        sum=n1+n2
        print(sum,end="")
