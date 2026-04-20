# 20.Write functions to implement map(), filter(), and reduce() manually.


# simple manual map, filter, reduce

def my_map(f, lst):
    return [f(x) for x in lst]

def my_filter(f, lst):
    return [x for x in lst if f(x)]

def my_reduce(f, lst):
    res = lst[0]
    for x in lst[1:]:
        res = f(res, x)
    return res


# main
nums = [1, 2, 3, 4]

print("Map:", my_map(lambda x: x*2, nums))        # double
print("Filter:", my_filter(lambda x: x%2==0, nums)) # even
print("Reduce:", my_reduce(lambda x,y: x+y, nums))  # sum
