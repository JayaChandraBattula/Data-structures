def tournament_winner(competitions, results):

    if not competitions:
        return ""

    best_team = ""
    competetors_dict = {}
    for i in range(len(competitions)):
        if results[i] == 1:
            competetors_dict[competitions[i][0]]  = competetors_dict.get(competitions[i][0], 0)+3
            best_team = get_best_team(best_team, competetors_dict, competitions[i][0])
        else:
            competetors_dict[competitions[i][1]]  = competetors_dict.get(competitions[i][1], 0)+3
            best_team = get_best_team(best_team, competetors_dict, competitions[i][1])
    print(competetors_dict)
    return best_team

def get_best_team(best_team, competetors_dict, curr_team):
    best_team_score = competetors_dict.get(best_team, 0)
    if competetors_dict[curr_team]>best_team_score:
        return curr_team
    return best_team


if __name__=="__main__":
    competitions = [
        ["html", "c#"],
        ["c#", "python"],
        ["python", "html"]
    ]
    results = [1,0,0]
    print(tournament_winner(competitions=competitions, results=results))