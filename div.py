def abc(a,b):
    sign = (-1 if((a<0)^(b<0) )else 1);
    a = abs(a)
    b = abs(b)
    q = 0
    temp = 0
    for i in range(31,-1,-1):
        if temp +(b<<i)<=a:
            temp = temp+b<<i
            q|=1<<i
    if sign == -1:
        q = -q
    return q
a = int(input("enter a number"))
b = int(input("enter another number"))
print(abc(a,b))