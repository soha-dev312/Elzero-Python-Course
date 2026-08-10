#-------string methods part2--------

my_string = "taehyung jungkook  jimin"
print(my_string)

#replace(old value, new value, count)
print(my_string.replace("jimin", "jhope"))

#join(Iterable)
my_list = ["kim", "tae", "hyung"]
print("-".join(my_list))
print(" ".join(my_list))
print("".join(my_list))
print("=" * 20)

#-------lists methods part2---------

myname = ["sohaila", "mohammed"]
print(myname)

#clear
myname.clear()
print(myname)

a = [1, 2, 3, 3]

#copy
a.copy()
print(a)

#count
print(a.count(3))

#index

s = ["RM", "yoongi", "jinn"]
print(s.index("yoongi"))

#isert
s.insert(0, "JK")
print(s)

#pop
print(a.pop(-1))
print("-" * 50)

#-------tuple methods part1-------

# tuple syntax & type test
mycartoons = ("lady bug", "toy story")
mycartoonss = "lady bug", "toy story"

print(mycartoons)
print(mycartoonss)

print(type(mycartoonss))
print(type(mycartoons))

#tuple indexing

my_tuple = (1, 5, 9, 0)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1])

#tuple concatenation

my_tuple1 = (2, 4, 6, 8)
my_tuple2 = (1, 3, 5, 7, 9)

c = my_tuple1 + my_tuple2
d = my_tuple1 + (True, "A") + my_tuple2

print(c)
print(d)

#Tuple, list, string repeat(*)

mylist = ["sooo", "tae"]
mytuple = ("jk", "rm")

print(mylist * 6)
print(my_tuple * 6)

#methods => count()
w = (1, 2, 3, 4, 5, 6, 2, 4, 6)
print(w.count(6))

#methods => index()
e = (0, 9, 8, 7, 6)
print(e.index(8))
print(f"the position of index is: {e.index(9)}")

#tuple destract
r = (4, 5, 9, 0)
x, y, z, _ = 4, 5, 9, 0
print(x)
print(y)
print(z)
print("=" * 50)

#-------set methods part1--------

#clear()

a = {1, 2, 3}
a.clear()
print(a)

#union()

b = {5, 6, 7, 8}
c = {"na", "hee", "doo"}

print(b|c)
print(b.union(c))

#add()

d= {7, 8, 9, 0,1}
d.add(10)
print(d)

#copy()

t = {12, 13, 15,17}
f = t.copy()
print(f) 

#remove()

u = {20, 30, 50}
u.remove(30)
print(u)

#discard()

o = {60, "sohaila"}
o.discard(70)
print(o)

#pop()
h = {"soha", True, 90}
print(h.pop())

#update()

j = {100, "saber"}
k = {200, "nour"}
j.update(k)
print(j)