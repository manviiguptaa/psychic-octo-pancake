cha = ['m', 'd', 'a', 'a', 'm']

d = {}
for char in cha:
    if char in d: 
        d[char]+=1 
    else:
        d[char] = 1 
        
for char,count in d.items():
    if count%2 != 0:
        print(char)
