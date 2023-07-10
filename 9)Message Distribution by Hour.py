name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst=list()
for line in handle:
     line=line.split()
     if len(line) < 1 or line[0] != ('From'):continue
        
     line=line[5]
     hour=line.split(":")
     hour=hour[:1]
     z=hour[0]
     lst.append(z)
     

dt=dict()
for x in lst:
    dt[x]=dt.get(x,0)+1

    
y=sorted(dt.items())
for m,k in y:
    print (m,k)