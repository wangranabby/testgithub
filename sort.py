import random


list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]


def qsort(L):
   if len(L)<2: return L
   temp = random.choice(L)
   small = [i for i in L if i< temp]
   large = [i for i in L if i> temp]
   return qsort(small) + [temp] + qsort(large)


def merge(list1, list2):
    return qsort(list1 + list2)


print(merge(list1, list2))