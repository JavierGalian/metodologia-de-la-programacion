def shell(lst):
 n = len(lst)
 gap = n // 2 # … 112,48,21,7,5,1
 while gap > 0:
    for i in range(gap, n):
        tmp = lst[i]
        j = i
        while j >= gap and lst[j - gap] > tmp:
            lst[j] = lst[j - gap]
            j -= gap
        lst[j] = tmp
    gap = gap // 2
 return lst

lst = []
shell(lst) 