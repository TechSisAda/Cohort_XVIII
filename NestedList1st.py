array = [[1, 2, 3], [2, 4, 7]]
for list_item in array:
    print(list_item)

list1 = [0, 2, 4, 6, 8, 10, 12, 14]
list2 = [3, 5, 8, 13, 21, 34, 55, 89]
equal = len(list1) == len(list2)
zipped = zip(list1, list2)
numerated = enumerate(list1)

print("zipped: ", zipped)
print("Zipped data type: ", type(zipped))
print("numerated: ", numerated)
print(f"numerated data type: {type(numerated)}")
print("numerated item: ", list(numerated))
# print("zipped items: ", list(zipped))


for (item1, item2) in zipped:
    print(f"List1 item: {item1}")
    print(f"List2 item: {item2}")