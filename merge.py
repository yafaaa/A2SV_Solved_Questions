def merge(left_half,right_half) -> List[int]:
    # write your code here
    left, right = 0, 0
    merged = []
    while left < len(left_half) and right < len(right_half):
        if left_half[left] <= right_half[right]:
            merged.append(left_half[left])
            left += 1
        else:
            merged.append(right_half[right])
            right += 1
    
    while left < len(left_half):
        merged.append(left_half[left])
        left += 1
        
    while right < len(right_half):
        merged.append(right_half[right])
        right += 1
    
    return merged

def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = (left + right) // 2
    ml = mergeSort(left, mid, arr)
    mr = mergeSort(mid+1, right, arr)
    return merge(ml, mr)
    


def test():
    assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    print("Great Job !!!")
test()
