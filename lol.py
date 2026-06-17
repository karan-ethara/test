str1 = "sheena loves eating mango and apple. her sister also loves eating apple and mango."

l1  = str1.split()
d = {}

for i in l1:
# for i in str1:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1

print(d)