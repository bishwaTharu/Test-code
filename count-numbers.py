a = [1,2,3,4,3]
count = dict()
for i in a:
    if (i in count):
        count[i] +=1
    else:
        count[i]=1

print(count)