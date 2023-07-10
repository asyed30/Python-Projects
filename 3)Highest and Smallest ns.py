largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        mum=int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest=mum
    elif mum>largest:
        largest=mum
    if smallest is None:
        smallest=mum
    elif mum<smallest:
        smallest=mum

print("Maximum is",largest)
print("Minimum is",smallest)