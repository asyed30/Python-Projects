score = input("Enter Score: ")
try:
 sc=float(score)
except:
 print("Please enter a numerical value")
 quit()
if sc>1:
 print("Please enter a valid score")
 quit()
if sc<0:
 print("Please enter a valid score")
 quit()
elif sc>=0.9 and sc <1:
 print("A")
elif sc>=0.8 and sc <1:
 print("B")
elif sc>=0.7 and sc <1:
 print("C")
elif sc>=0.6 and sc <1:
 print("D")
elif sc<0.6 and sc <1:
 print("F")