a=int(input("輸入一個整數:"))
ans=(a%2==0)*"偶數"+(a%2!=0)*"奇數"
print(f"{a}是{ans}")