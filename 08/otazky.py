# lst = [10,20,30,40,50,60,70]
# for v in lst:
#     print(v)
# print("---------------")
# for v in lst:
#     print(v, lst.pop(0))

lst1 = [
  {'name': 'Josef Novák', 'age': 27},
  {'name': 'Jan Srp', 'age': 80}
]
# create a copy of lst1
lst2 = []
for v in lst1:
    lst2.append(v)
lst2.pop()
lst2[0]['age'] = 15
print(lst1)
print(lst2)
print(lst1)