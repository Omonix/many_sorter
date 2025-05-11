import random, time
def selection(t):
    before = time.time()
    for i in range(len(t)):
        mini = len(t) - 1
        for x in range(i, len(t)):
            if t[x] < t[mini]:
                mini = x
        temp = t[mini]
        t[mini] = t[i]
        t[i] = temp
    return [t, time.time() - before]

random_list = [i for i in range(0, 20000)]
random.shuffle(random_list)
print(f'{selection(random_list)[1]} second for {len(random_list)} elements')