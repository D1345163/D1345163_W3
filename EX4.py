a=int(input("輸入一個三位數字"))
n1=int(((a%1000)-(a%100))/100)
n2=int(((a%100)-(a%10))/10)
n3=int(a%10)
ans=n1+n2+n3
print(ans)