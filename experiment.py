# 1-masala
# a = 10
# b = 22
#
# sonlar = [i for i in range(a, b) if i % 2 == 0]
#
# print("sonlar =", sonlar)
# a = 10
# b = 20
#
# sonlar   = [i for i in range(a, b) if i % 2 != 0]
#
# sonlar.reverse()
#
# print("sonlar =", sonlar)
# 2-masala
# list1 = ['salom', 123, True, 'Hayr', 'world', 3.14, '7214']
#
# TEXT = []
# OTHER = []
#
# for item in list1:
#     if isinstance(item, str):
#         TEXT.append(item)
#     else:
#         OTHER.append(item)
#
# TEXT.sort()
#
# OTHER.sort(reverse=True)
#
# print("TEXT =", TEXT)
# print("OTHER =", OTHER)
# 3-masala
# def juftliklarni_topish(lst, sonni_topish):
#     r = []
#     uzunligi = len(lst)
#
#     for i in range(uzunligi):
#         for j in range(i + 1, uzunligi):
#             if lst[i] + lst[j] == sonni_topish:
#                 r.append((i, j))
#
#     return r
#
#
# lst = [1, 2, 33, 5, 6, 7, 7]
# sonni_topish = int(input("INPUT = "))
#
# juft = juftliklarni_topish(lst, sonni_topish)
#
# if juft:
#     output = ' and '.join([f"{pair[0]}, {pair[1]}" for pair in juft])
#     print(output)
# else:
#     print("juftlik topilmadi")
# kiritish = input("input: ")
#
# soz = kiritish.split()
#
# taxlangan_soz = sorted(soz, key=lambda word: word[0])
#
# output = ' '.join(taxlangan_soz)
#
# print("output:", output)
# n = int(input("son kiriting: "))
#
# son = 0
#
# for i in range(1, n + 1):
#     son += i
#
#     ketma_ketlik = '+'.join(str(x) for x in range(1, i + 1))
#
#     print(f"{ketma_ketlik}={son}")
# input = input("gap kiriting: ")
#
# sozlar = input.split()
#
# qayta_ishlangan_soz = []
# for soz in sozlar:
#     if len(soz) % 2 == 1:
#         qayta_ishlangan_soz.append(soz[::-1])
#     else:
#         qayta_ishlangan_soz.append(soz)
#
# output = ' '.join(qayta_ishlangan_soz)
#
# print("Output:", output)
