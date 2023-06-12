
    # Move Zeros at the end in the array while maintaing the relative  order 
    
"""
   Brute Force approch
  =======================
  
1) Create two  empty array . 
2) Loop over input array and push non-Zero elements to new  array and zero to other.
3) concatinate both the array .

""" 
arr= [int(i) for i in input("Enter an array seprated by spaces : ").split()]
l= len(arr)
new= []
po = []
cnt = 0
print(f" Given array will be arr : {arr} ")

for i in arr:
    if i != 0:
        new.append(i)
    else:
        po.append(i)
print(f"New array will be arr : {new + po} ")
    



        
    
    
    

