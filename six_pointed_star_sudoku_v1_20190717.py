"""
GET Six_pointed_star answer with python script

version 1.0
author：liujuanjuan1984
date：2019-07-17
notice: bad script. pls take a look at version2.0

HOW does Six_pointed_star look like? view this picture:
https://user-images.githubusercontent.com/31027645/63708468-23d72600-c867-11e9-9347-5ef925b4d108.png

"""

'''
# bad script ever.
def areyouwin(point_list):
    if point_list[0] + point_list[6] + point_list[11] + point_list[4] != 26 :
        return False
    elif point_list[0] + point_list[7] + point_list[8] + point_list[2] != 26 :
        return False
    elif point_list[1] + point_list[7] + point_list[6] + point_list[5] != 26 :
        return False
    elif point_list[1] + point_list[9] + point_list[8] + point_list[3] != 26 :
        return False
    elif point_list[4] + point_list[9] + point_list[10] + point_list[2] != 26 :
        return False
    elif point_list[3] + point_list[10] + point_list[11] + point_list[5] != 26 :
        return False
    else:
        return True

'''
# better script.
def areyouwin(point_list):
    lines_list = [[0,4,6,11,],[0,2,7,8],[1,5,6,7],[1,3,8,9],[2,4,9,10],[3,5,10,11]]
    for lines in lines_list:
        sum = 0
        for idx in lines:
            sum += point_list[idx]
        if sum != 26:
            break
    else:
        return True

#point_list = [1,2,3,4,5,6,7,8,9,10,11,12] # bad script ever.
point_list = [x for x in range(1,13)] # better script.

point_1_list = point_list[:]

# when I finish this 12-times-for-script, I realized that it's terrible.
# Maybe I should write a better script.
for p_1 in point_1_list:
    point_2_list = point_1_list[:]
    point_2_list.remove(p_1)
    for p_2 in point_2_list:
        point_3_list = point_2_list[:]
        point_3_list.remove(p_2)
        for p_3 in point_3_list:
            point_4_list = point_3_list[:]
            point_4_list.remove(p_3)
            for p_4 in point_4_list:
                point_5_list = point_4_list[:]
                point_5_list.remove(p_4)
                for p_5 in point_5_list:
                    point_6_list = point_5_list[:]
                    point_6_list.remove(p_5)
                    for p_6 in point_6_list:
                        point_7_list = point_6_list[:]
                        point_7_list.remove(p_6)
                        for p_7 in point_7_list:
                            point_8_list = point_7_list[:]
                            point_8_list.remove(p_7)
                            for p_8 in point_8_list:
                                point_9_list = point_8_list[:]
                                point_9_list.remove(p_8)
                                for p_9 in point_9_list:
                                    point_10_list = point_9_list[:]
                                    point_10_list.remove(p_9)
                                    for p_10 in point_10_list:
                                        point_11_list = point_10_list[:]
                                        point_11_list.remove(p_10)
                                        for p_11 in point_11_list:
                                            point_12_list = point_11_list[:]
                                            point_12_list.remove(p_11)
                                            p_12=point_12_list[0]
                                            one_list=[p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12]

                                            if areyouwin(one_list):
                                                print(one_list)