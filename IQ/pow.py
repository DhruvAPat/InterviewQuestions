from re import A


def power(a,n):
    if n==1:
        return a
    else:
        mid=n//2
        b=power(a,mid)
        c=b*b
        if n%2==0:
            return c
        else:
            return c*a


a=int(input("Enter the number"))
n=int(input("enter the power"))
print("The answer is",power(a,n))