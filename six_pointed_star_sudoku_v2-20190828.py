"""
GET Six_pointed_star answer with python script

version 2.0
author：liujuanjuan1984
date：2019-08-28

HOW does Six_pointed_star look like? view this picture:
https://user-images.githubusercontent.com/31027645/63708468-23d72600-c867-11e9-9347-5ef925b4d108.png

"""

import itertools

lines_list = [[1,8,9,3,],[1,7,12,5],[2,8,7,6],[2,9,10,4],[3,10,11,5],[4,11,12,6]]
times = 1 #count how many results will get

for a_rlt in itertools.permutations(range(1,13)):
    for a_line in lines_list:
        sum = 0
        for a_point in a_line:
            sum += a_rlt[a_point-1]
        if sum != 26:
            break
    else:
        with open('d:/shudu0828.txt','at',encoding='utf-8') as f:
            f.write(str(times)+" "+str(a_rlt))
        #print(times,end=',')
        times += 1
print('well done! all results are in this file: \nd:/shudu0828.txt')
