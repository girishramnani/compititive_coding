p=print
x="Fizz"
y="Buzz"
for i in range(1,101):
    if i%15==0:
        p(x+y)
    if i%3==0:
        p(x)
    if i%5==0:
        p(y)
    else:
        p(i)
        