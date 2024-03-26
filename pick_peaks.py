def pick_peaks(arr):
    dic = {'pos': [], 'peaks': []}
    
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] >= arr[i+1]: # if is a peak
            if arr[i] == arr[i+1]:
                j = i + 1
                while j < len(arr): # walks on the arr until find a non equal element (bigger or smaller)
                    if arr[i] < arr[j]: # bigger element
                        i = j
                        break
                        
                    elif arr[i] > arr[j]: # smaller element -> means the arr[i] is a peak
                        dic['pos'].append(i)
                        dic['peaks'].append(arr[i])
                        i = j
                        break
                    else:
                        j += 1
            else:
                dic['pos'].append(i)
                dic['peaks'].append(arr[i])

    return dic

arr  = [[0, 1, 2, 5, 1, 0],
        [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3],
        [1, 2, 2, 2, 1],
        [1, 2, 2, 2, 3],
        [1, 2, 2, 2, 2]]

for vector in arr:
    print(pick_peaks(vector))
        
    
