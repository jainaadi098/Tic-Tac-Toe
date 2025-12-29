import random

used1=[]
used2=[]

board=[[" 1 ",' 2 ',' 3 '],[' 4 ',' 5 ',' 6 '],[' 7 ',' 8 ',' 9 ']]                
 
def display_board():
    for i in board:
        print(i)


def change(n,ch):
    i=(n-1)%3
    j=(n-1)//3
    board[j][i]=f' {ch} '

line=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def p2p():
    turn=random.randint(1,2)
    
    while True:
        if turn==1:  # Player X
            print("Player 1 Turn")
            display_board()
            n=int(input("Enter :"))
            ch="X"
            
            change(n,ch)
            used1.append(n)
            for i in line:
                n1=i[0]
                n2=i[1]
                n3=i[2]
                if n1 in used1 and n2 in used1 and n3 in used1:
                    print("Player 1 Wins")
                    return False
            
            turn=2
            
        if turn==2:  # Player X
            print("Player 2 Turn")
            display_board()
            n=int(input("Enter :"))
            ch="O"
            
            change(n,ch)
            used2.append(n)
            
            for i in line:
                n1=i[0]
                n2=i[1]
                n3=i[2]
                if n1 in used2 and n2 in used2 and n3 in used2:
                    print("Player 2 Wins")
                    return False
            
            turn=1


while True:
    p2p()
    display_board()
    print("Do you want to play again? (y/n)")
    ans=input()
    if ans=='n':
        break
    else:
        board=[[" 1 ",' 2 ',' 3 '],[' 4 ',' 5 ',' 6 '],[' 7 ',' 8 ',' 9 ']]  
        used1.clear()
        used2.clear()