#Ex1:
r = float(input("input circle radius: "))
pi = 3.14
area = pi* pow(r,2)
print("Area of circle is: ", area)


#Ex2:
c = float(input(" Enter the temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit is: ",f)

#Ex3:
n = int(input("Enter a number: "))
if n <2:
    print (f"{n} is not a prime number")
else:
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
        else:
            prime = True
    if prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number") 

#Ex4: 
n = int(input("Enter a number: "))
sum =0
for i in range(1,n):
    if n % i == 0:
        sum += i
if sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")

#Ex6:
range1 = range(0,7,1) 
range2= range(1,11,3)
range3 = range(5,0,-1)
range4 = range(6,-3,-2)
print(list(range1))
print(list(range2))
print(list(range3))
print(list(range4))

#Ex7: 
s ="hfdsjhf$$$$$$"
s1= s.replace("$", "")
print(s1)
s2="".join([c for c in s if c != "$"])
print(s2)

#Ex8:
def extract_even(l):
    result = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            result.append(l[i])
    return result  # cach 2 [return n for n in l if n % 2==0] 



n = input("enter many numbers: " )
num = [int (i) for i in n.split()]
even_num = extract_even(num)
print(even_num)

#Ex9:
def factorial(n):
    fac = 1
    for i in range(1,n+1,1):
        fac *= i
    return fac

n = int(input(print("enter a number: ")))
print (f"the factorial of {n}: ", factorial(n))

#Ex10:
def divs (n):
    out=[]
    for i in range (1,n+1):
        out+=[i]
    return out
print (divs(10))

#Ex11:
col = int (input("cols: "))
row = int (input("row: "))
for i in range (row):
    for j in range (col):
        if i==0 or i==row -1 or j ==0 or j == col-1:
            print("*", end="  ")
        else:
            print( "  ", end=" ")
    print()
