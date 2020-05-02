# Masz listę
# list_a = [1, 2, 3, 4, 5, 6, 7]
# Przy pomocy operacji, z którymi zapoznaliśmy się na tej lekcji przekształć daną listę w następujące listy:
#
# [1, 3, 5, 7]
# [2, 4, 6]
# [7, 6, 5, 4, 3, 2, 1]
# [6, 4, 2]
# [1, 7]
# [7, 4, 1]
# [] # pusta lista
# [5, 6, 7]

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = list_a[::2]
list_c = list_a[1::2]
list_d = list_a[::-1]
list_e = list_a[-2::-2]
list_f = list_a[::len(list_a) - 1]
list_g = list_a[::-3]
list_h = list_a.copy()
list_h.clear()
list_i = list_a[4:]

print(f"{list_a}\{list_b}\n{list_c}\n{list_d}\n{list_e}\n{list_f}\n{list_g}\n{list_h}\n{list_i}")

