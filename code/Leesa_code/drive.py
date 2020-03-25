driving_age =  eval(input("what is the legal driving age where you live"))
your_age = eval(input("how many years old are you"))
if your_age >= driving_age:
    print("your old enough to drive")
else:
    print("sorry you can drive in",driving_age - your_age,"years")
