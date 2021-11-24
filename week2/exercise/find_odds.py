def find_odds(li):
    odds_list = list()
    for i in li:
        if i % 2 != 0:
            odds_list.append(i)
    return odds_list
