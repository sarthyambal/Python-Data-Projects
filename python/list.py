names = ["HARRY","PERYY","CHERRY","MERRY"]
element = [1, 34, 67, False, True]

print(names)
print(type(names))

print(element[0])
element[2] = 69
print(element)

items = ["apple","banana","grapes"]
print(len(items))
items.append("Satberries")
items.insert(2,"Staberries")
items.extend(["more banana","pineapple"])
items.remove("banana")
items.pop(0)
items.clear()
# print(items.index("banana"))
print(items)
numbers =  [1,45,34,86,92,21]
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

print(11 in numbers )