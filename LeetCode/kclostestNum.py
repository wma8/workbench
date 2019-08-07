def binarySearch(s, target):
    start, end = 0, len(s)-1

    while(start + 1 < end):
        mid = int(start + (end - start)/2)
        # print(mid)
        if s[mid] == target:
            return mid
        elif s[mid] < target:
            start = mid
        else:
            end = mid

    return start if abs(s[start] - target) <= abs(s[end] - target) else end

def kClosestNumbers(list, target, k):
    mid = binarySearch(list, target)
    length = len(list)
    ret = [list[mid]]
    left,right=mid-1, mid+1

    while(k > 1):
        if left < 0:
            ret.append(list[right])
            right+=1
            k-=1
            continue

        if right >= length:
            ret.append(list[left])
            left -= 1
            k-=1
            continue

        if abs(list[left] - target) <= abs(list[right] - target): 
            ret.append(list[left])
            left-=1
        else:
            ret.append(list[right])
            right+=1

        k-=1

    return ret

if  __name__ == '__main__':
    array = [1,3,4,8,9,13,19]
    # print(binarySearch(array, 17))
    print(kClosestNumbers(array, 10, 7))

