def three_number_sum(array, target_sum):
    output_triplets = []
    array.sort()
    #print(f"sorted array {array}")
    for current_idx in range(len(array)):
        current_num = array[current_idx]
        i = current_idx+1
        j = len(array)-1
        
        while i<j:
            #print(f"current_num {current_num}, i {array[i]}, j {array[j]}")
            curr_sum = current_num+array[i]+array[j]
            if curr_sum == target_sum:
                output_triplets.append([current_num, array[i], array[j]])
                i+=1
                j-=1
            elif curr_sum < target_sum:
                i+=1
            elif curr_sum > target_sum:
                j-=1

    return output_triplets


if __name__ == "__main__":
    print(three_number_sum([12,3,1,2,-6,5,-8,6], target_sum=0))
        
