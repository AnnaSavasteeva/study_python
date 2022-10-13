# RLE алгоритм — “run-length encoding” — это способ сокращённой записи последовательности чего угодно, при котором
# для подряд идущих группы одинаковых символов (run) записываются длина этой группы (run length) и сам этот символ.
# Например, “99999” превратится в “5 9” («пять девяток»), и так далее. RLE широко используется в самых разных областях.

my_run = '223334444555551'


def encode(run):
    encoding = []
    count = 0
    run_length = len(run)
    if run_length == 1:
        encoding.append((1, run[0]))
    else:
        for i in range(run_length):
            count += 1
            if (i + 1) == len(run) or run[i] != run[i + 1]:
                encoding.append((count, run[i]))
                count = 0
    return encoding


def decode(encoded_data):
    return ''.join(list(map(lambda e: e[0] * e[1], encoded_data)))


encoding = encode(my_run)
print(my_run)
print(encoding)
print(decode(encoding))
