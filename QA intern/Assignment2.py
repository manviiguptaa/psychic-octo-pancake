arr = [1,5,1,3,7,21,25,2,5,3,21]
list1 = []
list2 = []

d = {}

for element in arr:
    if element in d:
        d[element]+=1 
    else:
        d[element] = 1 
    
for element, count in d.items():
    if count>1:
        list1.append(element)
    else:
        list2.append(element)
        
print(list1)
print(list2)
