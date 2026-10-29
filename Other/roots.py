a=1
b=4
c=4
def roots(a,b,c):
    n=(b**2)- 4*a*c
    if n>=0:
        x1=((-b)+(b**2 - 4*a*c)**0.5)/2*a
        x2=((-b)-(b**2 - 4*a*c)**0.5)/2*a
        return x1,x2
    else:
        return "No proper roots"
print(roots(a,b,c))
