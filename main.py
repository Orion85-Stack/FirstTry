sec = 42000
convert_to_min = sec / 60
print (convert_to_min)

convert_to_hour = convert_to_min / 60
print (convert_to_hour)

convert_to_days = convert_to_hour / 24
print (convert_to_days)

age = "hello"
print(age)

test = ["help", "alas", "the", "world"]
test.append("Simon")
test.append("Sarah")
test.insert(2, "Hello")
test.extend("john")
print(test)

l_1 = [1, 2, 3, 4]
l_2 = [5, 6, 7]
l_1.extend(l_2)
print (l_1)

age = int(input("Please enter your age: "))

if age < 18:
        print("sorry we can't serve you")
else:
  drink = input("please choose a drink: ")
  print (f"you ordered {drink}, thank you")

list(range(10))

hours = int(input("Enter hours: "))
h = float(hours)
rte = int(input("Enter rate: "))
r = float(rte)

if h <= 40:
  pay = h * rte
elif h > 40:
  pay = ((h-40) * rte * 1.5) + (rte * 40)
print = ("Your pay is: ")
