def score(dice_scores):
    count = [0 ,0, 0, 0, 0, 0]

    for score in dice_scores:
        count[score - 1] += 1
    
    final_score = 0

    prev_count = list(count)

    while any(count):
        if count[0] >= 3:
            final_score += 1000
            count[0] -= 3

        elif count[1] >= 3:
            final_score += 200
            count[1] -= 3

        elif count[2] >= 3:
            final_score += 300
            count[2] -= 3

        elif count[3] >= 3:
            final_score += 400
            count[3] -= 3

        elif count[4] >= 3:
            final_score += 500
            count[4] -= 3

        elif count[5] >= 3:
            final_score += 600
            count[5] -= 3

        elif count[0] >= 1:
            final_score += 100
            count[0] -= 1

        elif count[4] >= 1:
            final_score += 50
            count[4] -= 1

        if prev_count == count:
            break

        else:
            prev_count = list(count)
            
    return final_score


teste = [[5, 1, 3, 4, 1], # 250
         [1, 1, 1, 3, 1], # 1100
         [2, 4, 4, 5, 4]] # 450

for element in teste:
    print(score(element))
