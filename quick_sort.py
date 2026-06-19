def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    x = arr[len(arr) // 2]
    l ,m, r = [],[],[]
    for  i in arr:
        if i < x:
            l.append(i)
        elif i > x:
            r.append(i)
        else:
            m.append(i)
    return quick_sort(l) + m + quick_sort(r) 
print(quick_sort([9,8,7,6,5,4,3,2,1]))