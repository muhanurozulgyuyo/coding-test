# def solution(answers):
#     pick = {'1' : [1, 2, 3, 4, 5],
#     '2' : [2, 1, 2, 3, 2, 4, 2, 5],
#     '3' : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
#             }
    
#     count = {'1' : 0,
#     '2' : 0,
#     '3' : 0,
#             }
    
#     answer = []
    
#     for key, value in pick.items():
#         if len(answers) <= len(value):
#             for i in range(len(answers)):
#                 if answers[i] == value[i]:
#                     count[key] += 1
#         else:
#             new_value = []
#             while len(value) < len(answers):
#                 new_value = new_value + value
#             for i in range(len(answers)):
#                 if answers[i] == new_value[i]:
#                     count[key] += 1
        
#         if count[key] >= max(count.values()):
#             answer.append(key)
           
#     return list(map(int, answer))
    
def solution(answers):
    pick = {
        '1': [1, 2, 3, 4, 5],
        '2': [2, 1, 2, 3, 2, 4, 2, 5],
        '3': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    }

    count = {'1': 0, '2': 0, '3': 0}

    for key, value in pick.items():
        for i in range(len(answers)):
            if answers[i] == value[i % len(value)]:
                count[key] += 1

    max_score = max(count.values())
    answer = [int(key) for key, score in count.items() if score == max_score]

    return answer