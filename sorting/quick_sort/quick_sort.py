def pivot(array,start,end):
    """
        First it places the pivot at the end, then it swaps elements to make sure that larger elements are at the end of the list and
        smaller elements are at the start of the list
    """
    part = start
    for i in range(start+1,end+1):
        if array[i]<array[start]:
            # Swap the elements
            part+=1
            array[i],array[part] = array[part],array[i]
    # Put the pivot index in the middle of the sorted list
    array[part], array[start] = array[start], array[part]
    return part

def quick_sort(array,start,end):
    if start>=end:
        return
    pivot_point = pivot(array,start,end)
    # Sort left part
    quick_sort(array,start,pivot_point-1)
    # Sort right part
    quick_sort(array,pivot_point+1,end)
    return



    