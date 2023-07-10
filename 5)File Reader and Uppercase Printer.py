# Use words.txt as the file name
fname = input("Enter file name: ")
try:
 fh = open(fname)
except:
 print("File not found")
 quit()
fh=fh.read()
fh=fh.rstrip()
print(fh.upper())