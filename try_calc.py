# def get_row(board, row_num):
#     current_row = board // 10 ** (42 - ((row_num + 1) * 7))
#     return current_row % 10 ** 7


# # done
def get_count(window,n):
    empty=0
    count_2=0
    count_3=0
    for i in range(n):
        if window%10==1:
            empty+=1
            window//=10
         
        
        elif window%10==2:
            count_2+=1
            window//=10
       
        
        elif window%10==3:
            count_3+=1
            window//=10
          
    return empty,count_2,count_3

def get_score(list,player):
    element = 2
    opp = 1
    score=0
    # arkam el score kat over gdan fa kat btdrab el output 5ales
    # el numbers lazem tkon -= wa += mesh + wa - 3ashan y3ml deduction ml score law a7tmal n5sar mesh bas y7otot b -ve wa 5alas
    if player:
        element = 1
        opp = 2
    # print("opp:"+str(opp))
    if list[element] == 3 and list[0] == 1:
        score += 5
    elif list[element] == 2 and list[0] == 2:
        score += 2
    elif list[element] == 4:
        score += 100
    # if list[opp] == 4:
    #     score = -100
    if list[opp] == 3 and list[0] == 1:
        score -= 50


    return score

def get_row(board,row_num):

        current_row=board//10**(42-((row_num+1)*7))
        return current_row%10**7
    #done
def get_column(board,column):
    column_return=0
    # for i in range(6):
    #     row=get_row(board,i)
    #     print("row1:"+str(row))
    #     row=row//10**(6-column)
    #     print("row2:"+str(row))
    #     column_return=column_return+row*(10**(6-i))
    #     print()
    for i in range(6):
        row=get_row(board,i)
        row=row//10**(6-column)
        row %= 10
        column_return += row*10**(5-i)
  
    return column_return
# def get_element(board,row,column):
#     row=get_row(board,row)
#     element=row//(10**(6-column))
#     element=element%10
#     return element

# def get_diagonal(board,row,column,direction):
#     diagonal=0
#     limit_y=column
#     if column==0 or column==6:
#         limit_y=6-row
#     if row == 0 and direction==1:
#         limit_y = 7 - column
#     j=0
#     print(limit_y)
#     for i in range (limit_y):
#         diagonal=diagonal+get_element(board,row+i,column+j*direction)*10**(limit_y-i)
#         print(diagonal)
#         j=j+1
#     return diagonal//10


# def get_count(window,n):
#     empty=0
#     count_2=0
#     count_3=0
#     for i in range(n):
#         if window%10==1:
#             empty+=1
#             window//=10
        
#         elif window%10==2:
#             count_2+=1
#             window//=10
        
#         elif window%10==3:
#             count_3+=1
#             window//=10
       
#         print(window)

#     return empty,count_2,count_3


def get_element(board,row,column):
    row=get_row(board,row)
    element=row//(10**(6-column))
    element=element%10
    return element

def get_diagonal(board,row,column,direction):
    diagonal=0
    # limit_y=column
    # if column==0 or column==6:
    #     limit_y=6-row
    # if row == 0 and direction==1:
    #     limit_y = 7 - column
    j=0
    limit_y=4
    # print(limit_y)
    for i in range (limit_y):
        diagonal=diagonal+get_element(board,row+i,column+j*direction)*10**(limit_y-i)
        # print("diagonal:"+str(i)+" " +str(diagonal))

        # print(diagonal)
        j=j+1
    return diagonal//10


state=922133311811111111111111111114449894214567
# 1123331,1122211,1112111,1111111,1111111,1111111
state3=112211311121131111112111111111111111111111
player=True

# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 2
# 1 1 1 2 1 1 3
# 1 1 2 2 1 1 3

# center = 3
# horizontal = 5-4-4=-3
# vertical = 0
# pos_diag=0
# negatice_diag=0
# total = 0



# score=0
# score=0
# centrecolumn=get_column(state3,3)
# print(centrecolumn)

# # fl heuristic mesh bndrab score el column x3 , bndrab count el pieces x 3\

# # for j in range(3):
# #     ex = centrecolumn
# #     # 232313
# #     ex = ex % 10 ** (6 - j)
# #     window = ex // 10 ** (2 - j)
# #     print("window"+str(window))
# #     # assuming mazimizing 2

# empty, count_2, count_3 = get_count(centrecolumn,6)
# list = [empty, count_2, count_3]

# if player:
#     score += 3*count_2
# else:
#     score += 3*count_3

# center_score=score
# print("center score:"+str(score))

# for i in range (6):
#     row= get_row(state3,i)
#     # print("actual row:"+str(row))
#     for j in range(4):
#         ex = row
#         ex = ex % 10 ** (7 - j)
#         window=ex // 10 ** (3 - j)
#         # print("window:"+str(i)+" "+str(window))
#         #assuming mazimizing 2
#         empty,count_2,count_3=get_count(window,4)
#         list= [empty,count_2,count_3]
#         score+=get_score(list,player)
# horizontal_score=score-center_score
# print("horizon score:"+str(horizontal_score))

# for i in range(7):
#     column = get_column(state3, i)
#     for j in range(3):
#         ex = column
#         ex = ex % 10 ** (6 - j)
#         window = ex // 10 ** (2 - j)
    
#         # assuming mazimizing 2
#         empty, count_2, count_3 = get_count(window,4)
#         list = [empty, count_2, count_3]
#         score += get_score(list, player)
# vertical_score=score-horizontal_score-center_score
# print("vertical_score:"+str(vertical_score))



# for i in range(3):
#     for j in range(4):
#         diagonal = get_diagonal(state3,i,j,1)
#         empty, count_2, count_3 = get_count(diagonal,4)
#         list = [empty, count_2, count_3]
#         score += get_score(list, player)

# pos_diag=score-horizontal_score-center_score-vertical_score
# print("pos_diag:"+str(pos_diag))



# for i in range(3):
#     for j in range(4):
#         diagonal = get_diagonal(state3,i,6-j,-1)
#         empty, count_2, count_3 = get_count(diagonal,4)
#         list = [empty, count_2, count_3]
#         score += get_score(list, player)

# negative_diag=score-horizontal_score-center_score-vertical_score-pos_diag

# print("negative_diag:"+str(negative_diag))
# print("total_score:"+str(score))










score=0
centrecolumn=get_column(state3,3)
# fl heuristic mesh bndrab score el column x3 , bndrab count el pieces x 3\

# for j in range(3):
#     ex = centrecolumn
#     # 232313
#     ex = ex % 10 ** (6 - j)
#     window = ex // 10 ** (2 - j)
#     print("window"+str(window))
#     # assuming mazimizing 2

empty, count_2, count_3 = get_count(centrecolumn,6)
list = [empty, count_2, count_3]

print(list)
if player:
    score += 3*count_2
    
else:
    score += 3*count_3

center_score=score
print("center score:"+str(score))

#horizontally
for i in range (6):
    row= get_row(state3,i)
    # print("actual row:"+str(row))
    for j in range(4):
        ex = row
        ex = ex % 10 ** (7 - j)
        window=ex // 10 ** (3 - j)
        # print("window:"+str(i)+" "+str(window))
        #assuming mazimizing 2
        empty,count_2,count_3=get_count(window,4)
        list= [empty,count_2,count_3]
        score+=get_score(list,player)
horizontal_score=score-center_score
print("horizon score:"+str(horizontal_score))
    # print("horizontal score"+str(score))
# vertically
for i in range(7):
    column = get_column(state3, i)
    for j in range(3):
        ex = column
        #232313
        ex = ex % 10 ** (6 - j)
        window = ex // 10 ** (2 - j)
        # assuming mazimizing 2
        empty, count_2, count_3 = get_count(window,4)
        list = [empty, count_2, count_3]
        score += get_score(list, player)
vertical_score=score-horizontal_score-center_score
print("vertical_score:"+str(vertical_score))
#diagonally +ve
for i in range(3):
    for j in range(4):
        diagonal = get_diagonal(state3,i,j,1)
        empty, count_2, count_3 = get_count(diagonal,4)
        list = [empty, count_2, count_3]
        score += get_score(list, player)
pos_diag=score-horizontal_score-center_score-vertical_score
print("pos_diag:"+str(pos_diag))

    
#diagonally -ve
for i in range(3):
    for j in range(4):
        diagonal = get_diagonal(state3,i,6-j,-1)
        empty, count_2, count_3 = get_count(diagonal,4)
        list = [empty, count_2, count_3]
        score += get_score(list, player)

negative_diag=score-horizontal_score-center_score-vertical_score-pos_diag

print("negative_diag:"+str(negative_diag))
print("total_score:"+str(score))



tree=[[['1', '0', '0'], ['1', '0', '1'], ['1', '0', '2'],  ['1', '0', '4'], ['1', '0', '5'], ['1', '0', '6']],[['2', '3', '0']]]
def fill_the_gaps(list):
    final_list=[]
    for j in range(len(list)):
        gap=int(list[j][0][2])
        if gap >1:
                for j in range(gap-1):
                    final_list.append(None)
        for i in range(len(list[j])-1):
            
            gap=int(list[j][i+1][2])-int(list[j][i][2])
            if gap >1:
                for j in range(gap-1):
                    final_list.append(None)
           # final_list.append(list[i+1][2])
        final_list.append(list[j][-1])

    return final_list
tree=fill_the_gaps(tree)
print(tree)
# window=323232
# empty,count2,count3=get_count(window,4)
# print("empty:"+str(empty))
# print("2:"+str(count2))
# print("3:"+str(count3))
# 4 2 1 4 5 6 7
# 1 4 4 4 9 8 9
# 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1
# 1 1 8 1 1 1 1
# 9 2 2 1 3 3 3
# print(get_diagonal(state,0,1,1))
