#Valid mountain array .
    
# Naive  Approach
""" 
1) First we declare a pointer i for comparison purpose at index 1 to compare the previous element.
2)  declare while loop Iterate over an array and compare if current element is greater than previous element .
    condition for this is until current element (less than) < size of array
    increment the value of i.
    
3) check if i==1 or i== size of Array 
   means 1. if size is 1.
         2. after iterating whole array we can't find any elemnet which less than previous elemnet .
         return false 
         
         
4) another while loop to check after first while loop break condition  not satisfy that if i<size of array and current element(i)
   is less than previous element in the whole array till it i==len(array)
   increment the value of i .
   
5) return True (if i == len(array))
6) if len of array is less than 3 return false .

"""
# optimal sollution using two pointer method .

                                                    # Source code
                                                    



def MountainArray(arr,n):
    if n<3:
        return False

    i=1
    while(i< n and arr[i] > arr[i-1]):
        i+=1

    if i==1 or i==n:
        return False

    while (i<n and arr[i] < arr[i-1]):
        i+=1

    if i==n:
        return True

n=int(input("Enter the size of array : "))
arr= [int(i) for i in input("Enter the element in array sep. by spaces : ").split()]
arr= arr[0:n]
ans= MountainArray(arr,n)
print(ans)
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                             