# 1
a = ['python', 'c#', 'c', 'java', 'c', ]
print(a.count('c'))
# 2
numbers = [1, 2, 3, 4]
print(numbers[0]+numbers[1]+numbers[2]+numbers[3])
print(sum(numbers[:]))
# 3
a = ['python', 'c#', 'c', 'java', 'c']
print(max(a))
# 4
a = ['python', 'c#', 'c', 'java', 'c']
print(min(a))
# 5
a = ['python', 'c#', 'c', 'java', 'c']
print('java' in a)
# 6
a = ['python', 'c#', 'c', 'java', 'c']
print(a[0] if a else None)
# if it is empty
a = []
print(a[0] if a else None)
# 7
a = ['python', 'c#', 'c', 'java', 'c']
print(a[-1])
# if it is empty
a = []
print(a[-1])
# 8
a = ['python', 'c#', 'c', 'java', 'c']
b = a[0:3]
print(b)
# 9
a = ['python', 'c#', 'c', 'java', 'c']
b = list(reversed(a))
print(b)
# 10
a = ['python', 'c#', 'c', 'java', 'c']
b = list(sorted(a))
print(b)
# 11
a = ['python', 'c#', 'c', 'java', 'c']
b = list(set(a))
print(b)
# 12
a = ['python', 'c#', 'c', 'java', 'c']
a.insert(2, 'php')
print(a)
# 13
a = ['python', 'c#', 'c', 'java', 'c']
print(a.index("c"))
# 14
a = []
print(a.index('') if a else False)
# 15
numbers = [1, 2, 3, 4]
even = sum(1 for n in numbers if n % 2 == 0)
print(even)
# 16
numbers = [1, 2, 3, 4]
odd = sum(1 for n in numbers if n % 2 == 1)
print(odd)
#17
numbers = [1, 2, 3, 4]
a = ['python', 'c#', 'c', 'java', 'c']
c = a+numbers
print(c)
#18
numbers = [1, 2, 3, 4]
a = ['python', 'c#', 'c', 'java', 'c']
c = numbers in a
print(c)
#19
a = ['python', 'c#', 'c', 'java', 'c']
a[a.index("c")] = 'php'
print(a)
#20
a = ['python', 'c#', 'c', 'java', 'c']
a.pop(a.index(max(a)))
print(max(a))
#21
a = ['python', 'c#', 'c', 'java', 'c']
a.pop(a.index(min(a)))
print(min(a))
#22
numbers = [1, 2, 3, 4]
even = list(n for n in numbers if n % 2 == 0)
print(even)
#23
numbers = [1, 2, 3, 4]
odd = list(n for n in numbers if n % 2 == 1)
print(odd)
#24
a = ['python', 'c#', 'c', 'java', 'c']
print(a.__len__())
#25
a = ['python', 'c#', 'c', 'java', 'c']
b = a.copy()
#26
a = ['python', 'c#', 'c', 'java', 'c']
m = a.__len__()//2
c = len(a)
if  c % 2 ==1:
    print(a[m])
else :
    print(a[m-1:m+1])
#27
a = [10, 20, 5, 30, 25]
sublist = a[1:4]
print(max(sublist))
#28
a = [10, 20, 5, 30, 25]
sublist = a[1:4]
print(min(sublist))
#29
a = ['python', 'c#', 'c', 'java', 'c']
index_to_remove = 2
if 0  <=index_to_remove <len(a):
    a.pop(index_to_remove)
print(a)
#30
a = [1, 2, 3, 4, 5]
print(a == sorted(a))
#31
a = ['python', 'c#', 'c']
print(a * 3)
#32
a = [3, 1, 4]
b = [2, 5, 0]
c = sorted(a + b)
print(c)
#33
a = ['python', 'c#', 'c', 'java', 'c']
b = a.index("c")
c = b+1
d = a[c:].index('c')
print(b, d+c)
#34
a = [1, 2, 3, 4, 5]
k = 2 
rotated = a[-k:] + a[:-k]
print(rotated)
#35
# Numbers from 1 to 10
numbers = list(range(1, 11))
print(numbers)
#36
numbers = [10, -5, 3, -2, 7]
positive_sum = sum([x for x in numbers if x > 0])
print(positive_sum)
#37
numbers = [10, -5, 3, -2, 7]
negative_sum = sum([x for x in numbers if x < 0])
print(negative_sum)
#38
a = ['python', 'c#', 'c', 'c#', 'python']
is_palindrome = a == a[::-1]
print(is_palindrome)
#39
a = [1, 2, 3, 4, 5, 6, 7]
n = 3
nested = [a[i:i+n] for i in range(0, len(a), n)]
print(nested)
#40
a = ['python', 'c#', 'c', 'java', 'c']
unique_set = set(a)
unique_list = list(unique_set)
print(unique_list)
##tuple
#1
t = ('python', 'c#', 'c', 'java', 'c')
element = 'c'
count = t.count(element)
print(count)
#2
t = (10, 5, 20, 3, 15)
maximum = max(t)
print(maximum)
#3
t = (10, 5, 20, 3, 15)
minimum = min(t)
print(minimum)
#4
t = ('python', 'c#', 'c', 'java')
element = 'c'
exists = element in t
print(exists)
#5
t = ('python', 'c#', 'c', 'java')
if t:
    first = t[0]
else:
    first = None 

print(first)
#6
t = ('python', 'c#', 'c', 'java')
last = t[-1] if t else None
print(last)
#7
t = ('python', 'c#', 'c', 'java')
print(len(t))
#8
t = ('python', 'c#', 'c', 'java')
new_tuple = t[:3]
print(new_tuple)
#9
t1 = ('python', 'c#')
t2 = ('c', 'java')
combined = t1 + t2
print(combined)
#10
t = ('python', 'c#', 'c')
print(len(t) == 0)
#11
t = ('python', 'c#', 'c', 'java', 'c')
element = 'c'
indices = [i for i, x in enumerate(t) if x == element]
print(indices)
#12
t = (10, 20, 5, 20, 3)
unique_sorted = sorted(set(t), reverse=True)
second_largest = unique_sorted[1] if len(unique_sorted) > 1 else None
print(second_largest)

#13
t = (10, 20, 5, 20, 3)
unique_sorted = sorted(set(t))
second_smallest = unique_sorted[1] if len(unique_sorted) > 1 else None
print(second_smallest)
#14
element = 'python'
single_tuple = (element,)
print(single_tuple)

#15
lst = ['python', 'c#', 'c', 'java']
t = tuple(lst)
print(t)
#16
t = (1, 2, 3, 4, 5)
print(t == tuple(sorted(t)))
#17
t = (10, 20, 5, 30, 25)
subtuple = t[1:4]
print(max(subtuple))
#18
t = (10, 20, 5, 30, 25)
subtuple = t[1:4]
print(min(subtuple))
#19
t = (1, 2, 3, 4, 5)
element_to_remove = 3
t_new = tuple(x for x in t if x != element_to_remove)
print(t_new)
#20
t = (1, 2, 3, 4, 5, 6)
n = 2
nested = tuple(tuple(t[i:i+n]) for i in range(0, len(t), n))
print(nested)
#21
t = (1, 2, 3)
n = 3
repeated = tuple(x for x in t for _ in range(n))
print(repeated)
#22
t = tuple(range(1, 11))
print(t)
#23
t = (1, 2, 3, 4, 5)
print(t[::-1])
#24
t = (1, 2, 3, 2, 1)
print(t == t[::-1])
#25
t = (1, 2, 2, 3, 4, 3)
unique = tuple(dict.fromkeys(t))
print(unique)

## sets
#1
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)
#2
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)
#3
s1 = {1, 2, 3}
s2 = {2, 3}
print(s1 - s2)
#4
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1 <= s2)
#5
s = {1, 2, 3}
print(2 in s)
#6
s = {1, 2, 3}
print(len(s))
#7
lst = [1, 2, 2, 3]
s = set(lst)
print(s)
#8
s = {1, 2, 3}
s.discard(2)
print(s)
#9
s = {1, 2, 3}
s.clear()
print(s)
#10
s = {1, 2, 3}
print(len(s) == 0)
#11
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 ^ s2)
#12
s = {1, 2, 3}
s.add(4)
print(s)
#13
s = {1, 2, 3}
print(s.pop())
#14
s = {1, 2, 3}
print(max(s))
#15
s = {1, 2, 3}
print(min(s))
#16
s = {1, 2, 3, 4, 5}
evens = {x for x in s if x % 2 == 0}
print(evens)
#17
s = {1, 2, 3, 4, 5}
odds = {x for x in s if x % 2 == 1}
print(odds)
#18
s = set(range(1, 11))
print(s)
#19
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
s = set(lst1 + lst2)
print(s)
#20
s1 = {1, 2, 3}
s2 = {4, 5}
print(s1.isdisjoint(s2))
#21
lst = [1, 2, 2, 3, 3, 3]
lst_no_dupes = list(set(lst))
print(lst_no_dupes)
#22
lst = [1, 2, 2, 3, 3, 3]
print(len(set(lst)))
#23
import random
s = {random.randint(1, 20) for _ in range(5)}
print(s)
##dictionary
#1
d = {'a': 1, 'b': 2}
print(d.get('a'))
#2
d = {'a': 1, 'b': 2}
print('a' in d)
#3
d = {'a': 1, 'b': 2}
print(len(d))
#4
d = {'a': 1, 'b': 2}
print(list(d.keys()))
#5
d = {'a': 1, 'b': 2}
print(list(d.values()))
#6
d1 = {'a': 1}
d2 = {'b': 2}
d = {**d1, **d2}
print(d)
#7
d = {'a': 1, 'b': 2}
d.pop('a', None)
print(d)
#8
d = {'a': 1, 'b': 2}
d.clear()
print(d)
#9
d = {'a': 1, 'b': 2}
print(len(d) == 0)
#10
d = {'a': 1, 'b': 2}
print(('a', d['a']) if 'a' in d else None)
#11
d = {'a': 1, 'b': 2}
d['a'] = 10
print(d)
#12
d = {'a': 1, 'b': 2, 'c': 1}
value = 1
count = sum(1 for v in d.values() if v == value)
print(count)
#13
d = {'a': 1, 'b': 2}
d_inverted = {v: k for k, v in d.items()}
print(d_inverted)
#14
d = {'a': 1, 'b': 2}
value = 2
keys = [k for k, v in d.items() if v == value]
print(keys)
#15
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))
print(d)
#16
d = {'a': 1, 'b': 2, 'c': {'d': 3}}
nested = any(isinstance(v, dict) for v in d.values())
print(nested)
#17
d = {'a': {'x': 10}}
print(d['a']['x'])
#18
from collections import defaultdict
d = defaultdict(int)
print(d['missing'])
#19
d = {'a': 1, 'b': 2, 'c': 1}
unique_values = len(set(d.values()))
print(unique_values)
#20
d = {'b': 2, 'a': 1, 'c': 3}
sorted_by_key = dict(sorted(d.items()))
print(sorted_by_key)
#21
d = {'a': 3, 'b': 1, 'c': 2}
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_by_value)
#22
d = {'a': 3, 'b': 1, 'c': 2}
filtered = {k: v for k, v in d.items() if v > 1}
print(filtered)
#23
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
common_keys = set(d1.keys()) & set(d2.keys())
print(common_keys)
#24
t = (('a', 1), ('b', 2))
d = dict(t)
print(d)
#25
d = {'a': 1, 'b': 2}
first_key = next(iter(d))
print((first_key, d[first_key]))
