import math
import random

import igraph
from igraph import Graph, EdgeSeq
import plotly.graph_objects as go
ID=0
def int_to_oneD(state):

        list=[0,0,0,0,0,0,0,0,0]

        for i in range (0,9):

                list[8-i]=state%10 

                state//=10
        return list 

def column_to_list(columns):
    column_list=[0,0,0,0,0,0,0]
    for i in range(7):
        column_list[6 - i] = columns % 10

        columns //= 10
    return column_list

def get_I_J(index):
    # btraga3 42 - el index
            Row=index//6
            Column=index%6

            return Row , Column
# 1111111,1111111,1444989,1234567
# 1111111,
# 9221333,

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
        # print(diagonal)
        j=j+1
    return diagonal//10
    
# get column bayza 5ales
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


def get_available_columns(board):

    return board%10**7

    # done
def list_available_columns(columns):
    list_column=column_to_list(columns)
    index_available_columns=[7,7,7,7,7,7,7]
    for i in range(7):
        if list_column[i]==1:
            index_available_columns[i]=i
        
    return index_available_columns



def get_row(board,row_num):

        current_row=board//10**(42-((row_num+1)*7))
        return current_row%10**7
    #done

def get_next_empty_row(board,column):

    for i in range(6):
        row=get_row(board,i)
        #print(row)
        row=row//10**(6-column)
        row %= 10
       # print(row)
        if row == 1:
            return i

# ba2olha ya 1 ya 2 wa btadd el piece fl x wel y ely badyhomlaha
def insert_piece(main_board,row,column,player):
    board=main_board
    if player==1:#2
        piece=10**(41-(row*7+column))   
        board=board+piece
        return board

    else:#3
        piece=2*10**(41-(row*7+column))   
        board=board+piece
   
        return board
        #done



    
def minmax(available_colums):

    for i in range(7):
        current_columm=available_colums//10**(6-i)
        available_colums %= 10**(6-i)
        #print(current_columm)
        # da mogarad bylef 3ala kol el columns



        # if current_columm != 1:
        #     continue
        # else:
        #     pass
def is_terminal(board):
    columns= get_row(board,5)
    sum=0
    for i in range(7):
        if columns%10==1:
            sum=sum+1
        columns=columns//10
        
    if sum == 0:
        return True
    else:
        return False
heuristic_matrix=[[3,4,5,7,5,4,3],
                  [4,6,8,10,8,6,4],
                  [5,8,11,13,11,8,5],
                  [5,8,11,13,11,8,5],
                  [4,6,8,10,8,6,4],
                  [3,4,5,7,5,4,3]]
# tree=[]
# tree.append([])

tree_list=[]

def draw_tree(show,tree_list):
    if show:
        nr_vertices = ID
       
        maps=map(str,tree_list)

        v_label = list(maps)



        G = Graph.Tree(nr_vertices, 7) # 2 stands for children number
        lay = G.layout('rt')

        position = {k: lay[k] for k in range(nr_vertices)}
        Y = [lay[k][1] for k in range(nr_vertices)]
        M = max(Y)

        es = EdgeSeq(G) # sequence of edges
        E = [e.tuple for e in G.es] # list of edges

        L = len(position)
        Xn = [position[k][0] for k in range(L)]
        Yn = [2*M-position[k][1] for k in range(L)]
        Xe = []
        Ye = []
        for edge in E:
            Xe+=[position[edge[0]][0],position[edge[1]][0], None]
            Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]

        labels = v_label


        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe,
                        y=Ye,
                        mode='lines',
                        line=dict(color='rgb(210,210,210)', width=1),
                        hoverinfo='none'
                        ))
        fig.add_trace(go.Scatter(x=Xn,
                        y=Yn,
                        mode='markers',
                        name='bla',
                        marker=dict(symbol='circle-dot',
                                        size=60,
                                        color='#6175c1',    #'#DB4551',
                                        line=dict(color='rgb(50,50,50)', width=1)
                                        ),
                        text=labels,
                        hoverinfo='text',
                        opacity=0.8
                        ))
        
        axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
                    zeroline=False,
                    showgrid=False,
                    showticklabels=False,
                    )

        fig.update_layout(title= 'Tree with Reingold-Tilford Layout',
                    annotations=make_annotations(M,labels,position, v_label),
                    font_size=12,
                    showlegend=False,
                    xaxis=axis,
                    yaxis=axis,
                    margin=dict(l=40, r=40, b=85, t=100),
                    hovermode='closest',
                    plot_bgcolor='rgb(248,248,248)'
                    )
        fig.show()

def make_annotations(M,labels,pos, text, font_size=10, font_color='rgb(250,250,250)'):
            L=len(pos)
            if len(text)!=L:
                raise ValueError('The lists pos and text must have the same len')
            annotations = []
            for k in range(L):
                annotations.append(
                    dict(
                        text=labels[k], # or replace labels with a different list for the text within the circle
                        x=pos[k][0], y=2*M-pos[k][1],
                        xref='x1', yref='y1',
                        font=dict(color=font_color, size=font_size),
                        showarrow=False)
                )
            return annotations

def calculate_score(board):
    scoreAI=0
    scorePlayer=0
    # fl heuristic mesh bndrab score el column x3 , bndrab count el pieces x 3\

    # for j in range(3):
    #     ex = centrecolumn
    #     # 232313
    #     ex = ex % 10 ** (6 - j)
    #     window = ex // 10 ** (2 - j)
    #     print("window"+str(window))
    #     # assuming mazimizing 2
    #horizontally
    for i in range (6):
        row= get_row(board,i)
        # print("actual row:"+str(row))
        for j in range(4):
            ex = row
            ex = ex % 10 ** (7 - j)
            window=ex // 10 ** (3 - j)
            # print("window:"+str(i)+" "+str(window))
            #assuming mazimizing 2
            empty,count_2,count_3=get_count(window,4)
            if count_2==4:
                scoreAI+=1
            if count_3==4:
                scorePlayer+=1
    # vertically
    for i in range(7):
        column = get_column(board, i)
        for j in range(3):
            ex = column
            #232313
            ex = ex % 10 ** (6 - j)
            window = ex // 10 ** (2 - j)
            # assuming mazimizing 2
            empty, count_2, count_3 = get_count(window,4)
            if count_2==4:
                scoreAI+=1
            if count_3==4:
                scorePlayer+=1
    #diagonally +ve
    for i in range(3):
     for j in range(4):
        diagonal = get_diagonal(board,i,j,1)
        empty, count_2, count_3 = get_count(diagonal,4)
        if count_2==4:
                scoreAI+=1
        if count_3==4:
                scorePlayer+=1
    #diagonally -ve
    for i in range(3):
     for j in range(4):
        diagonal = get_diagonal(board,i,6-j,-1)
        # print(diagonal)s
        empty, count_2, count_3 = get_count(diagonal,4)

        if count_2==4:
            scoreAI+=1
         
        if count_3==4:
            scorePlayer+=1
      
    print("AI_score:"+str(scoreAI))
    print("player_score:"+str(scorePlayer))
    if scoreAI > scorePlayer:
        print("AI_wins!!")
    elif scorePlayer > scoreAI:
        print("palyer_wins!!")
    else:
        print("tie")
   



def heuristic(board,player):
    columns=get_available_columns(board)#6177163
    max=0
    #column_oh=[0,1,2,3,4,5,6]
    list_Available_Columns=list_available_columns(columns)
    for colum in list_Available_Columns:
        if colum ==7:
            continue
        else:
            row=get_next_empty_row(board,colum)
            if heuristic_matrix[row][colum]>max:
                max=heuristic_matrix[row][colum]
    return max

def count_nodes(board):
    global ID
    ID = ID + 1

def aux_minimax(board,depth,maximizing_player,show=False,mode=True):
    global ID
    ID=0
    global tree_list
    tree_list=[]
    tree=[]
    tree = [[] for x in range(depth+1)]
    if mode:
        best_column,value=minimax(board,depth,maximizing_player,tree)
    else:
        best_column,value=minimax_pruning(board,depth,-math.inf, math.inf, maximizing_player,0 ,tree)
    sum_nodes=0
    for i in tree:
        print(i)
        sum_nodes+=len(i)
        print("fasel")
        
    print("sum_nodes:"+str(sum_nodes))
    for i in range(depth+1):
        # print(len(tree[depth-i]))
        tree_list.extend(tree[depth-i])
    tree_list[0]=str(best_column)+" "+str(tree_list[0])
    ID=len(tree_list)
    print(ID)
    # calculate_score(board)
    draw_tree(show,tree_list)
    
    return best_column,value
# get count kat fixed 3ala window 4 m23en el middle column fyh 6 pieces wa mesh byt3ado 
# fa 5aleto fyh n , 4 law window wa 6 law column
# get count makatsh bt devide el number by 10 kol mara fa dyman gyba el count 3'alat

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

# TRUE == AI == MAX ==2, FLASE == player ==MIN ==3

def get_score(list,player):
    element = 2
    opp = 1
    score=0
    # arkam el score kat over gdan fa kat btdrab el output 5ales
    # el numbers lazem tkon -= wa += mesh + wa - 3ashan y3ml deduction ml score law a7tmal n5sar mesh bas y7otot b -ve wa 5alas
    if player:
        element = 1
        opp = 2
        
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
    
def fill_the_gaps(list):
    final_list=[]
    for i in range(len(list)-1):
        final_list.append(list[i][2])
        gap=list[i+1][2]-list[i][2]
        if gap >1:
            for j in range(gap-1):
                final_list.append(None)
       # final_list.append(list[i+1][2])
    final_list.append(list[-1][2])

    return final_list
def heuristic2(board,player):
    
    score=0
    centrecolumn=get_column(board,3)

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



    if player:
        score += 3*count_2
        
    else:
        score += 3*count_3

  
    
    #horizontally
    for i in range (6):
        row= get_row(board,i)
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

        # print("horizontal score"+str(score))
    # vertically

    for i in range(7):
        column = get_column(board, i)
        for j in range(3):
            ex = column
            #232313
            ex = ex % 10 ** (6 - j)
            window = ex // 10 ** (2 - j)
            # assuming mazimizing 2
            empty, count_2, count_3 = get_count(window,4)
            list = [empty, count_2, count_3]
            score += get_score(list, player)

    #diagonally +ve
    for i in range(3):
     for j in range(4):
        diagonal = get_diagonal(board,i,j,1)
        empty, count_2, count_3 = get_count(diagonal,4)
        list = [empty, count_2, count_3]
        score += get_score(list, player)

    #diagonally -ve
    for i in range(3):
     for j in range(4):
        diagonal = get_diagonal(board,i,6-j,-1)
        empty, count_2, count_3 = get_count(diagonal,4)
        list = [empty, count_2, count_3]
        score += get_score(list, player)
    return score


def minimax(board,depth,maximizing_player,tree,not_none=True):
    if not_none:
        if depth==0 or is_terminal(board):
            Heuristic=heuristic2(board,True)
            node=str(depth)+"  "+str(Heuristic)
            tree[depth].append(str(node))
            return None,Heuristic
            
        columns = get_available_columns(board)
        if maximizing_player:
            value=-math.inf
            list_columnss=list_available_columns(columns)
            best_column = random.choice(list_columnss)
            list_Available_Columns=list_available_columns(columns)
            for column in list_Available_Columns:
                if column == 7:
                    # if column is full
                    minimax(None,depth-1,False,tree,False)
                else:
                    row= get_next_empty_row(board,column)
                    new_board=insert_piece(board,row,column,1)
                    count_nodes(new_board)
                    new_value=minimax(new_board,depth-1,False,tree)[1]
                    if new_value>value:
                        value=new_value
                        best_column=column
            node="c."+str(best_column)+" d."+str(depth)+" v."+str(value)
            tree[depth].append(str(node))     
            return best_column,value
        else:
            value = math.inf
            list_columnss = list_available_columns(columns)
            best_column = random.choice(list_columnss)
            list_Available_Columns=list_available_columns(columns)
            for column in list_Available_Columns:
                if column == 7:
                      # if column is full
                    minimax(None, depth - 1, True,tree,False)
                else:
                    row = get_next_empty_row(board, column)
                    new_board = insert_piece(board, row, column, 2)
                    count_nodes(new_board)
                    new_value = minimax(new_board, depth - 1, True,tree)[1]
                    if new_value < value:
                        value = new_value
                        best_column = column
            node="c."+str(best_column)+" d."+str(depth)+" v."+str(value)
            tree[depth].append(str(node))  
            return best_column, value
    else:
        if depth==0 :
            node=str(depth)+" none"
            tree[depth].append(str(node))
            return None,None
        for column in range(7):
                
                minimax(None, depth - 1, True,tree,False)
               
        node=str(depth)+" none"
        tree[depth].append(str(node))    
        return None, None




def minimax_pruning(board,depth,alpha,beta,maximizing_player,p_ID,tree,not_none=True):
    
    if depth==0 or is_terminal(board):
        Heuristic=heuristic2(board,True)
        node=[str(depth),str(Heuristic),str(p_ID)]
        tree[depth].append(node)
        return None,Heuristic
    columns = get_available_columns(board)
    if maximizing_player:
        value=-math.inf
        list_columnss=list_available_columns(columns)
        best_column = random.choice(list_columnss)
        list_Available_Columns=list_available_columns(columns)
        for column in list_Available_Columns:
            if column == 7:
               continue
            else:
                row= get_next_empty_row(board,column)
                new_board=insert_piece(board,row,column,1)
                count_nodes(new_board)
                new_value=minimax_pruning(new_board,depth-1,alpha,beta,False,(p_ID*7+column),tree)[1]
                if new_value>value:
                    value=new_value
                    best_column=column
                alpha=max(alpha,value)
                if alpha>=beta:
                    
                    break
        node=[str(depth),str(value),str(p_ID)]
        tree[depth].append(node)     
        return best_column,value
    else:
        value = math.inf
        list_columnss = list_available_columns(columns)
        best_column = random.choice(list_columnss)
        list_Available_Columns=list_available_columns(columns)
        for column in list_Available_Columns:
            if column == 7:
                 continue
            else:
                row = get_next_empty_row(board, column)
                new_board = insert_piece(board, row, column, 2)
                count_nodes(new_board)
                new_value = minimax_pruning(new_board, depth - 1,alpha,beta, True,(p_ID*7+column),tree)[1]
                if new_value < value:
                    value = new_value
                    best_column = column
                beta = min(beta,value)
                if alpha >=beta:
                 
                    break
        node=[str(depth),str(value),str(p_ID)]
        tree[depth].append(node)  
        return best_column, value






def int_into_2D(board):
    list_board_2D=[[]in range(6)]
    for i in range(6):
        list_board_2D.append(int_to_oneD(get_row(board,5-i)))

# 9221333,1111111,1111111,1111111,1444989,1234567
# 1111111,1111111,1111111,1111111,1111111,1111111
state=322133311111111111111111111111111111111111
state1=111111111111111111111111111111111111111111
state3=922133311111111111111111111114449894214567
# print_board(state3)
# av=get_available_columns(state1)
# print(list_available_columns(av))

#minmax(av)
#print("avv")

# print(av)
# depth=3


 #print(aux_minimax(state,depth,True,True))



# print(ID)
# print(is_terminal(state3))


#print(is_terminal(state))
#print(list_available_columns(av))
#print(get_row(state,0))
# av2=list_available_columns(av)
# row=get_next_empty_row(state,av2[0])
# i=get_next_empty_row(state,0)
# # print(i)
# insert_piece(state,1,1,1)
# row,column=get_I_J()
# print("row"+str(row))
# print("column"+str(column))column
