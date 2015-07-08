num1 = input()
num2 = input()
ans = str(int(num1)+ int(num2))


num1 = num1.replace("0","")

num2= num2.replace("0","")

ans  = ans.replace("0","")
if int(num1)+int(num2) == int(ans):
    print("YES")
else:
    print("NO")

