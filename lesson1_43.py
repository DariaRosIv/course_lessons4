# На вход подается строка. Нужно посчитать и вывести в консоль кол-во каждого символа в этой строке.
# Реализовать решение в виде функции.
# Вход: abbcdd
# Выход: a - 1, b - 2, c - 1, d - 2.

def strcounter(s):   # сложность O(N^2)
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, "-", counter)

# strcounter('aabbcd')

def strcounter2(s):  # O(N+M) = O(2*N) = O(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(sym, "-", count)

strcounter2('qwerttttty')





