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

#Using XOR Operation (bit manipulation)

def getMissingNumber(arr):
 
    #for example a xor a will give 0 but a xor 0 will give a
    xor = 0
    # we xor all the elements in the orignal array
    for i in arr:
        xor = xor ^ i
 
    #now we xor the elements from orignal array and from the range function together. The similar terms when xor get cancelled and we have the missing element as 
    #asnwer.
    
    for i in range(1, len(arr) + 2):
        xor = xor ^ i
 
    return xor
 
 
if __name__ == '__main__':
 
    arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    print('The missing number is', getMissingNumber(arr))
