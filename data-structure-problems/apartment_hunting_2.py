"""
Problem Description:
Apartment-Hunting ---> O(BR)/ O(BR)
"""
from typing import List, Dict

def apartment_hunting(blocks: List[Dict[str, str]], reqs: List[str]) -> int:
    min_distance_of_blocks = list(map(lambda req: get_min_distance_of_block_for_req(blocks, req), reqs))
    max_distance_for_each_block = get_max_distance_for_each_block(blocks, min_distance_of_blocks)
    return get_idx_of_smallest_block(max_distance_for_each_block)


def  get_idx_of_smallest_block(max_distance_from_blocks: List[int]) -> int:
    print(f"max blocks {max_distance_from_blocks}")
    idx = 0
    smallest_distance_from_index = float("inf")
    for i in range(len(max_distance_from_blocks)):
        if max_distance_from_blocks[i]<smallest_distance_from_index:
            smallest_distance_from_index = max_distance_from_blocks[i]
            idx = i
    return idx

def get_max_distance_for_each_block(blocks, min_distance_of_blocks):
    max_distance_for_req = [0 for block in blocks]
    for i in range(len(blocks)):
        int_list = list(map(lambda distances: distances[i], min_distance_of_blocks))
        max_distance_for_req[i] = max(int_list)
    return max_distance_for_req


def get_min_distance_of_block_for_req(blocks, req):
    min_distance_at_each_idx = [0 for block in blocks]
    closest_req_idx = float("inf")
    for i in range(len(blocks)):
        if blocks[i][req]:
            closest_req_idx = i
        min_distance_at_each_idx[i] = abs(i-closest_req_idx)

    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closest_req_idx = i
        min_distance_at_each_idx[i] = min(min_distance_at_each_idx[i], abs(i-closest_req_idx))
    return min_distance_at_each_idx
        


if __name__ == "__main__":
    input_data = blocks = [
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    
    "gym": True,
    "school": False,
    "store": False,
  },
  {
    "gym": True,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": True,
  },
]
reqs = ["gym", "school", "store"]
print(apartment_hunting(input_data, reqs))

