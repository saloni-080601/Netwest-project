def birthdayCakeCandes(s): 
    max_no=0
    for j in s:
        if max_no<j:
            max_no=j
    count=0
    for k in s:
        if max_no==k:
            count+=1
    return count
user=int(input("enter a number"))
list1=[]
for i in range(user):
    element=int(input("enter a element"))
    list1.append(element)
print(birthdayCakeCandes(list1))