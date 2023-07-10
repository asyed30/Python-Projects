fname = input("Enter file name: ")
try:
 fh = open(fname)
except:
    print("File not found:")
    quit()
lst = list()
for line in fh:
    word=line.split()
    for x in word:
        if x in lst:
            continue
        else:
            lst.append(x)
    
lst.sort()
print (lst)