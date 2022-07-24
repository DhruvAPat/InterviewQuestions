#Using Sum of n natural numbers
def missarray(arr):
    l=len(arr)
    natural=[]
    #calculating and storing the number in the list
    for i in range(1,l+2):
        natural.append(i)
    
    s=sum(natural)
    s1=sum(arr)
    target=s-s1
    return target
arr=[1,2,3,4,5,6,7,8,10]
print("The missing no in the array is",missarray(arr))
