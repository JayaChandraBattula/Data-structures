def get_merged_overlapping_arrays(array):

    if not array:
        return [[]]

    array = sorted(array, key = lambda x: x[0])
    print(array)
    current_interval = array[0]
    merged_intervals = []
    merged_intervals.append(current_interval)

    for next_interval in array:
        _, current_interval_end = current_interval
        next_interval_start, next_interval_end = next_interval

        if current_interval_end >= next_interval_start:
            current_interval[1] = max(current_interval_end, next_interval_end)
        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)

    return merged_intervals


# if __name__ == "__main__":
#     print(get_max_overlapping_arrays([[1,2], [2, 4], [0,3]]))






def get_max_overlapping_arrays(array):
    array = sorted(array)
    print(array)
    max_overlapping_array = []
    prev_array = array[0]
    for i in range(1, len(array)):
        current_array = array[i]
        curr_start_ele = current_array[0]
        curr_end_ele = current_array[1]
        prev_start_ele = prev_array[0]
        prev_end_ele = prev_array[1]
        print(f"curr_arr: {current_array}, prev_array: {prev_array}")
        if curr_start_ele >= prev_start_ele and curr_start_ele <= prev_end_ele:
            prev_array=[prev_start_ele, max(prev_end_ele, curr_end_ele)]
            print(prev_array)
            if i == len(array)-1:
                max_overlapping_array.append(prev_array)

        else:
            max_overlapping_array.append(prev_array)
            prev_array=array[i]

    return max_overlapping_array



if __name__ == "__main__":
    print(get_max_overlapping_arrays([[1,2], [2, 4], [0,3]]))