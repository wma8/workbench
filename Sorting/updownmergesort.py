def UptoDownMergeSort(lists):
    if len(lists) <= 1:
        return lists
    middle = int( len(lists) / 2 )
    left = UptoDownMergeSort(lists[:middle])
    right = UptoDownMergeSort(lists[middle:])
    return merge(left, right)

def merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result

if __name__ == '__main__':
    array = [5, 3, 9, 13, 25, 32, 8, 10, 23, 15, 13]
    result = UptoDownMergeSort(array)
    print(result)

# array = [5, 3, 9, 13, 25, 32, 8, 10, 23, 15, 13]
# a = [222, 223]
# array.extend(a)
# print(array)

