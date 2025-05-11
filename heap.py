import random, time
def heaper(list, length, i):
    head = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < length and list[left] > list[head]:
        head = left
    if right < length and list[right] > list[head]:
        head = right
    if head != i:
        list[i], list[head] = list[head], list[i]
        heaper(list, length, head)
def heap_sort(t):
    before = time.time()
    n = len(t)
    for i in range(n // 2 - 1, -1, -1):
        heaper(t, n, i)
    for i in range(n - 1, 0, -1):
        t[0], t[i] = t[i], t[0]
        heaper(t, i, 0)
    return [t, time.time() - before]

random_list = [i for i in range(20000)]
random.shuffle(random_list)
print(f'{heap_sort(random_list)[1]} second for {len(random_list)} elements')