#add()	Adds an element to the set

set1={"a","b",1}
set1.add("c")
print(set1)

#clear()	Removes all the elements from the set

set2={1, 2, 3}
set2.clear()
print(set2)

#copy()	Returns a copy of the set

x={}
x = set1.copy()
print(x)

#difference()	Returns a set containing the difference between two or more sets

print(set1.difference(set2))

#difference_update()	Removes the items in this set that are also included in another, specified set

set2.difference_update(set1)
print(set2)
print(set1)

#discard()	Remove the specified item

set1.discard(1)
print(set1)

#intersection()	Returns a set, that is the intersection of two other sets

set3 = {"Mango", "Orange", "Cherry"}
set4 = {"Joey", "Mia", "Mango"}
z = set3.intersection(set4)
print(z)

#intersection_update()	Removes the items in this set that are not present in other, specified set(s)

z = set3.intersection_update(set4)
print(z)

#isdisjoint()	Returns whether two sets have a intersection or not

z = x.isdisjoint(set3)
print(z)

#issubset()	Returns whether another set contains this set or not

a = {"a", "b", "c"}
b = {"f", "e", "d", "c", "b", "a"}
c = a.issubset(b)
print(c)

#issuperset()	Returns whether this set contains another set or not

c = a.issuperset(b)
print(c)

#pop()	Removes an element from the set

x.pop()
print(x)

#remove()	Removes the specified element

x.remove("a")
print(x)

#symmetric_difference()	Returns a set with the symmetric differences of two sets

z = set3.symmetric_difference(set4)
print(z)

#symmetric_difference_update()	inserts the symmetric differences from this set and another

set3 = {"apple", "banana", "cherry"}
set4 = {"google", "microsoft", "apple"}
set3.symmetric_difference_update(set4) 
print(x)

#union()	Return a set containing the union of sets

a = {"q", "w", "e", "r", "t", "y"}
b = {"a","b","c","d","e","f"}
c = a.union(b)
print(c)

#update()	Update the set with the union of this set and others

c = a.update(b)
print(c)