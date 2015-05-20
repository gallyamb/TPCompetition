import itertools
letters = 'q w e r t y u i o p'.split()

pass_len, p1, _ = tuple(map(int, input().split()))
expected_hash = int(input())

to_int = {
    'q': 16,
    'w': 22,
    'e': 4,
    'r': 17,
    't': 19,
    'y': 24,
    'u': 20,
    'i': 8,
    'o': 14,
    'p': 15
}


def hash(string):
    tmp_result = 0
    for i in range(len(string)):
        tmp_result += to_int[string[i]] * p1 ** i
    return tmp_result

def gen2(prev, count):
    if count == 0:
        return
    if count == 1:
        for i in letters:
            curr = prev + i
            if hash(curr) == expected_hash:
                yield curr
    else:
        for i in letters:
            curr = prev + i
            yield from gen2(curr, count - 1)



# for i in filter(lambda x: hash(x) == expected_hash, itertools.product(letters, repeat=pass_len)):
#     print(''.join(i))

# for i in gen2("", pass_len):
#     print(i)

import timeit
print(timeit.timeit(lambda: list(filter(lambda x: hash(x) == expected_hash, itertools.product(letters, repeat=pass_len))), number=1))