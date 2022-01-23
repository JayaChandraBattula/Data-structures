def get_min_rewards(scores):
    if not scores:
        return []

    rewards = [1 for i in scores]

    for i in range(1, len(scores)):
        j = i-1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j+1]:
                rewards[j] = max(rewards[j], rewards[j+1]+1)
                j -= 1
    print(rewards)
    return sum(rewards)



if __name__ == "__main__":
    print(get_min_rewards([8,4,2,1,3,6,7,9,5]))