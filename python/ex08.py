x = int(input())

a = x//1000
b = x%1000
c = b//100
d = x%100
e = d//10
f = x%10
print(a,c,e,f)
sum = a+c+e+f
print(sum)