def divop(dividend,divisor):
    sign=1
    if dividend*divisor<0:
        sign=-1
    dividend=abs(dividend)
    divisor=abs(divisor)
    res=0
    while dividend>=divisor:
        inc=1
        temp=divisor
        while temp<=dividend:
            dividend-=temp
            res+=inc
            inc=inc*2
            temp=temp*2
    return sign*res
divisor=4
dividend=57
print("The quotient of the above divison is",divop(dividend,divisor))