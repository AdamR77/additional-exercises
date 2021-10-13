
from typing import List

# słownik
# 1. Stwórz z listy liczb histogram.
sequence = [ 9, 4, 2, 3, 2, 'lab' , 7, 5, 9, 2, 2, 3, 2]
print(sequence)
def histogram(sequence: list):
  hist = {}
  
  for element in sequence:
    counter = 0
    for index in range(len(sequence)):
      if element == sequence[index]:
        counter += 1
    hist[element] = counter  
  return hist  

#spr.
print(histogram(sequence),"\n")

# ilustracja graficzna :)

hist = histogram(sequence)
for x in hist:
  value = hist[x]
  print(x,":", end = " ")
  print(value * "+")

print("")

# 2. Usuń wszystkie elementy słownika mające daną wartość
# {'a': 2, 'b': 3, 'c': 2}, usuń 2 -> {'b': 3}

value_for_del = 2
_list_for_del = []
for x in hist:
  if hist[x] == value_for_del:
    _list_for_del.append(x)
for x in _list_for_del:    
  del hist[x]

print(hist)



# 3. Zwróć wartość o danym kluczu lub jeżeli nie istnieje to zwróć zero
key = 5 
def key_search(key):
  for x in hist:
    if x == key:
      return hist[x]

print(key_search(key))




# 4. Stwórz listę zawierającą wartości w słowniku
# P.S. stworzyłem nową liste

example_dict = {'Auto': 'Ford', 'Model': 'Focus', 'Type': 'Kombi', 'Fuel Type': 'gasoline'}
values_list = []
for key in example_dict:
  value = example_dict.get(key)
  values_list.append(value)
print(values_list)
print(example_dict.values(), "\n")

# 5. Stwórz listę zawierającą klucze w słowniku
key_list = []
for key in example_dict:
  key_list.append(key)
print(key_list)
print(example_dict.keys(), "\n")


# 6. Stwórz listę zawierającą pary (tuple) klucz, wartość ze słownika

example_dict_list = [example_dict.items()]
print(example_dict_list)






# Przy użyciu słownika, sprawdź czy w liście liczb są dwie liczby, które sumują się do danej liczby. Uwaga: iterując tylko raz (tylko w jednej pętli)


# 7. Usuń wartość ze słownika

def check(list: List[int], target: int):
  pass

# lista

# 1. odwróć listę w Pythonie nie używając funkcji reverse
def list_reversed(_list):
  list_reversed = _list[::-1]
  return list_reversed

_list = [1, 3, 5, 8, 'Ala ma kota', 4, 12]
print(list_reversed(_list), "\n")


# 2. Stwórz listę list w Pythonie za pomocą listy składanej (list comprehension)
_list1 = ['a', 'b', 'c' , 'd', 'e', 'f']
_list_of_lists = [ _list1 for x in range(6)]
print(_list_of_lists, "\n")


# 3. Znajdź elementy wspólne dwóch list. I zwróć listę elementów wspólnych. Bez używania set

list_a = [ 3, 5, 2, 6, 'abc', 24, 12]
list_b = [12, 2, 0, 0, 'cde', 16, 8]
common_list = []
def common(list_a, list_b):
  for x in list_a:
    if x in list_b:
     common_list.append(x)
  return common_list
common(list_a, list_b)
print(common_list, "\n")




# 4. Wykonaj unię dwóch list. Zwróć listę elementów unii
list_union = list_a + list_b
print(list_union, "\n")


# set 
# 1. Iloczyn zbiorów - zwróć zbiór będący iloczynem
set_a = {1, 2, 3, 4, 5}
set_b = {2, 4, 6, 8, 10}
print(set_a & set_b, "\n")

# 2. Suma zbiorów - zwróć sumę zbiorów
print(set_a | set_b)

print("\n")
# 3. Iloczyn kartezjański zbiorów - zwróć iloczyn kartezjański
# (a, b) i (c, d) -> ( (a,c), (a, d), (b, c), (b,d) )

a_set = ('a','b')
b_set = ('c','d')

axb_set = []
for x in a_set:
  for y in b_set:
    axb_tuple = (x,y) 
    axb_set.append(axb_tuple)
print(axb_set, "\n")   

# 4. sprawdź czy coś jest w zbiorze, jeśli nie ma to dodaj to coś.
def check_set(_set, element):
  if element in _set:
    return True
  if element not in _set:
    print(element," has been added")
    _set.add(element)

_set = {3, 5, 10}
print(check_set(_set, 2))
print(_set,"\n")


# tuple

# 1. Stwórz z jednego tuple nowy tuple o jeden większy z elementem z lewej strony
tuple_1 = (1, 2, 3, 5, 10)
tuple_2 = (0,) +tuple_1
print(tuple_2)


# przyklad -> (0,1,2) -> (50, 0, 1, 2)

# 2. Stwórz z jednego tuple nowy tuple o jeden większy z elementem z prawej strony
tuple_3 = tuple_1 + (0,)
print(tuple_3, "\n")

# 3. Stwórz z jednego tuple nowy tuple o jeden większy z elementem w środku arytmetycznym ilości elementów (a,b,c,d) -> (a,b,NOWY,c,d).
tuple_ = ('a', 'b', 'c', 'd')
half_tuple_ = tuple_[0:int(1/2*len(tuple_)):]
half2_tuple_ = tuple_[int(1/2*len(tuple_))::]
tuple_new = half_tuple_ + ('new',) + half2_tuple_
print(tuple_new,"\n")

# 4. Stwórz nowy tuple, który jest odwróconym tuplem 
tuple_new_list = list(tuple_new)
tuple_new_list.reverse()
tuple_new_reversed = tuple(tuple_new_list)
print(tuple_new_reversed, "\n")

# 5. Stwórz listę z tuple'a
# rób to w takim formacie:
# def f(tuple):
#   return tuple
def tuple_converse(t: tuple):
  conversed_tuple = list(t)
  return conversed_tuple
t = (1, 2, 3, 5, 'abcd')
print(tuple_converse(t))


