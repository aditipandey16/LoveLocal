def count_n3(num):
    n = len(num)
    base = n//3

    store = {}
    for i in num:
        if i not in store.keys():
            store[i] = 0
        store[i] += 1
    
    nums = []
    for key, value in store.items():
        if value > base:
            nums.append(key)
    
    return nums

num = list(map(int, input().split()))
print(count_n3(num))