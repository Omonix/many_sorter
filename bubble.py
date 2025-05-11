import random, time
def bubble(t):
    before = time.time()
    while t != [x for x in range(0, len(t))]:
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:
                temp = t[i]
                t[i] = t[i + 1]
                t[i + 1] = temp
    return [t, time.time() - before]

random_list = [i for i in range(0, 20000)]
random.shuffle(random_list)
print(f'{bubble(random_list)[1]} second for {len(random_list)} elements')