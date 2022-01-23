# def longest_peak(array):
#     if not array or len(array)<3:
#         return 0
    
#     peak_indices = []
#     for i in range(1, len(array)-1):
#         if array[i-1]<array[i] and array[i]>array[i+1]:
#             peak_indices.append(i)
#     print(peak_indices)
#     max_peak_len = 0
#     for peak_idx in peak_indices:
#         peak = array[peak_idx]
#         left_val = get_left_peak(peak_idx, array)
#         right_val = get_right_peak(peak_idx, array)
#         print(left_val, right_val)
#         max_peak_len = max(max_peak_len, abs(right_val-left_val)+1)

#     return max_peak_len

# def get_left_peak(idx, array):

#     left_value_idx = idx
#     for i in reversed(range(idx)):
#         if array[i-1] < array[i] and i>0:
#             continue
#         else:
#             left_value_idx = i
#             break
#     return left_value_idx


# def get_right_peak(idx, array):
    
#     right_value_idx = idx+1
#     print(f"right_value_idx {right_value_idx}")
#     for i in range(idx, len(array)-1):
#         print(i)
#         if array[i] > array[i+1]:
#             continue
#         else:
#             right_value_idx = i
#             break
#     print(f"sds{right_value_idx}")
#     return right_value_idx




def longest_peak(array):
    longest_peak = 0
    i = 1
    while i < len(array)-1:
        is_peak = array[i] > array[i-1] and array[i] > array[i+1]
        if not is_peak:
            i+=1
            continue

        left_idx = i-2
        while left_idx>=0 and array[left_idx]<array[left_idx+1]:
            left_idx-=1

        right_idx = i+2
        while right_idx<len(array) and array[right_idx] < array[right_idx-1]:
            right_idx+=1

        current_longest_peak = right_idx-left_idx-1
        longest_peak = max(current_longest_peak, longest_peak)

        i = right_idx
    return longest_peak


if __name__ == "__main__":
    print(longest_peak([5, 4, 3, 2, 1, 2, 1]))