# на вход подается строка - посчитайте и выведите в консоль кол-во каждого символа в этой строке.

#   сложность O(N*M)  ->   O(N^2)
# def strcounter(s):
#     print(set(s))
#     for sym in set(s):   # set() - множество (струкутра данных с неупорядоченными уникальными значениями)
#         count = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 count += 1
#         print(sym, "-", count)
#
# strcounter('aab')

# O(N+M)   ->   O(N)
def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)

strcounter("aaabbbcccccdd")


