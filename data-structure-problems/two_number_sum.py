# given an array and target sum and returns 
# pairs of numbers suming to target sum

# O(n) time, O(1) space
def two_number_sum(array, target_sum):
    look_up_dict = {}
    #output_pairs = []
    for i in array:
        result_num = target_sum-i
        if result_num not in look_up_dict:
            look_up_dict[i] = result_num
        else:
            return [i, result_num]
    return []


if __name__ == "__main__":
    print(two_number_sum([3,5,-4,8,11,1,-1,6], target_sum=10))