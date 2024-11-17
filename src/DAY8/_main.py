# def calculate_love_score(name_1, name_2):
#     count_1 = 0
#     count_2 = 0
#     list = []
#     for name in name_1:
#         list.append(name)
#     for name in name_2:
#         list.append(name)
#     keywords_1 = 'true'
#     keywords_2 = 'love'
#     keyword_list_1 = []
#     keyword_list_2 = []
#     for keyword in keywords_1:
#         keyword_list_1.append(keyword)
#     for keyword in keywords_2:
#         keyword_list_2.append(keyword)
#
#     for name in list:
#         if name in keyword_list_1:
#             count_1 += 1
#         if name in keyword_list_2:
#             count_2 += 1
#
#     score = count_1 * 10 + count_2
#     print(score)
#
# calculate_love_score()
#
# SOLUTION:

def calculate_love_score(name_1,name_2):
    name_1 = name_1.lower()
    name_2 = name_2.lower()

    combined_name = name_1 + name_2
    lower_name = combined_name.lower()

    t = lower_name.count('t')
    r = lower_name.count('r')
    u = lower_name.count('u')
    e = lower_name.count('e')

    #LOVE:
    l= lower_name.count('l')
    o = lower_name.count('o')
    v= lower_name.count('v')
    e = lower_name.count('e')

    true = t+r+u+e
    love = l+o+v+e
    score = int(str(true) + str(love))
    print(score)

calculate_love_score('Tatto','Babbo')