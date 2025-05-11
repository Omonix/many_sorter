import random, time
def merge_sort(t):
    before = time.time()
    return [cut(t), time.time() - before]
def cut(t):
    list_a = t[:len(t) // 2]
    list_b = t[len(t) // 2:]
    if len(list_a) != 1:
        list_a = cut(list_a)
    if len(list_b) != 1:
        list_b = cut(list_b)
    return merge(list_a, list_b)
def merge(list_a, list_b):
    sorted_list = []
    x, y = 0, 0
    while x < len(list_a) and y < len(list_b):
        if list_a[x] <= list_b[y]:
            sorted_list.append(list_a[x])
            x += 1
        else:
            sorted_list.append(list_b[y])
            y += 1
    sorted_list.extend(list_a[x:])
    sorted_list.extend(list_b[y:])
    return sorted_list

random_list = [i for i in range(200)]
random.shuffle(random_list)
print(f'{merge_sort(random_list)[1]} second for {len(random_list)} elements')