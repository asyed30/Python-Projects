# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
 fh = open(fname)
except:
    print("File not found")
    quit()
count=0
fvalue=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        x=line.find("0")
        value=float(line[x:])
        count=count+1
        fvalue=fvalue+value
       

print("Average spam confidence:", fvalue/count)