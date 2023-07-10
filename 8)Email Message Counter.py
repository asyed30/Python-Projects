name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lt=list()
for line in handle:
    if not line.startswith('From'):continue
    line=line.split()      
    lt.append(line[1])
    
count=dict()
for sword in lt :
 count[sword]=count.get(sword,0)+1
        
bigcount=None
bigword=None
for x,y in count.items():
    if bigcount is None or y>bigcount:
     bigword=x
     bigcount=y
    
print(bigword, int(bigcount/2))