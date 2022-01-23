def tournament_winner(competitions, results):

    if not competitions:
        return ""

    competetors_dict = {}
    for i in range(len(competitions)):
        if results[i] == 1:
            competetors_dict[competitions[i][0]]  = competetors_dict.get(competitions[i][0], 0)+3

        else:
            competetors_dict[competitions[i][1]]  = competetors_dict.get(competitions[i][1], 0)+3
    print(competetors_dict)
    largest_value = float("-inf")
    for key in competetors_dict:
        if competetors_dict[key]> largest_value:
            winner = key
            largest_value = competetors_dict[key]
    return winner


if __name__=="__main__":
    competitions = [
        ["html", "c#"],
        ["c#", "python"],
        ["python", "html"]
    ]
    results = [0,0,1]
    print(tournament_winner(competitions=competitions, results=results))