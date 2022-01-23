"""
Problem Description:
Apartment-Hunting ---> O(B^2R)/ O(BR)
"""
from typing import List, Dict

def apartment_hunting(blocks: List[Dict[str, str]], reqs: List[str]) -> int:
    max_distance_from_blocks = []
    for i in range(len(blocks)):
        req_distance_list = []
        for req in reqs:
            smallest_distance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    # caluclating the distance of each req from the block 
                    # present in first loop to each block in this loop hence (i-j)
                    smallest_distance = min(smallest_distance, abs(i-j)) 
            req_distance_list.append(smallest_distance)
        print(f"for req {req} dist is {req_distance_list}")
        max_distance_from_blocks.append(max(req_distance_list))
        print(f"for blocks {i} dist is {max_distance_from_blocks}")

    return get_optimized_block(max_distance_from_blocks)


def  get_optimized_block(max_distance_from_blocks: List[int]) -> int:
    print(f"max blocks {max_distance_from_blocks}")
    idx = 0
    smallest_distance_from_index = float("inf")
    for i in range(len(max_distance_from_blocks)):
        if max_distance_from_blocks[i]<smallest_distance_from_index:
            print(max_distance_from_blocks[i], smallest_distance_from_index)
            smallest_distance_from_index = max_distance_from_blocks[i]
            print(smallest_distance_from_index)
            idx = i

    return idx


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

            


