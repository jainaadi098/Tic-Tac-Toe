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
        if turn==1:  
            print("\n\n\nPlayer 1 Turn\n")
            
            n=int(input("Enter :"))
            ch="X"
            while True:
                if n in used1 or n in used2:
                    n=int(input("Enter :"))
                else:
                    break
            change(n,ch)
            used1.append(n)
            for i in line:
                n1=i[0]
                n2=i[1]
                n3=i[2]
                if n1 in used1 and n2 in used1 and n3 in used1:
                    print("\n\n\nPlayer 1 Wins\n\n\n")
                    return False
            display_board()
            turn=2
        if len(used1)+len(used2)==9:
            print("\n\n\nTie\n\n\n")
            break 
        if turn==2:  
            print("\n\n\nPlayer 2 Turn\n")
            
            n=int(input("Enter :"))
            ch="O"
            while True:
                if n in used1 or n in used2:
                    n=int(input("Enter :"))
                else:
                    break
            change(n,ch)
            used2.append(n)
            
            for i in line:
                n1=i[0]
                n2=i[1]
                n3=i[2]
                if n1 in used2 and n2 in used2 and n3 in used2:
                    print("\n\n\nPlayer 2 Wins\n\n\n")
                    return False
            display_board()
            turn=1
        
        if len(used1)+len(used2)==9:
            print("\n\n\nTie\n\n\n")
            break


def p2c():
    
    turn=random.randint(1,2)
    
    while True:
        if turn==1:  
            print("\n\n\nPlayer 1 Turn\n")
            
            n=int(input("Enter :"))
            ch="X"
            while True:
                if n in used1 or n in used2:
                    n=int(input("Enter :"))
                else:
                    break
            change(n,ch)
            used1.append(n)
            for i in line:
                n1=i[0]
                n2=i[1]
                n3=i[2]
                if n1 in used1 and n2 in used1 and n3 in used1:
                    print("\n\nPlayer 1 Wins\n\n")
                    return False
            display_board()
            turn=2
        if len(used1)+len(used2)==9:
            print("\n\n\nTie\n\n\n")
            break  
        if turn==2: 
            print("\n\n\nComputer Turn\n")
            
            n=random.randint(1,9)
            ch="O"
            while True:
                if n in used1 or n in used2:
                    # print("\nRElol\n")
                    n=random.randint(1,9)
                else:
                    break
            
            change(n,ch)
            used2.append(n)
            print("Enter :",n)
            for i in line:
                n1=i[0]
                n2=i[1]
                n3=i[2]
                if n1 in used2 and n2 in used2 and n3 in used2:
                    print("\n\nComputer Wins\n\n")
                    return False
            display_board()
            turn=1
        
        if len(used1)+len(used2)==9:
            print("\n\n\nTie\n\n\n")
            break

# def c2c():
    
#     turn=random.randint(1,2)
    
#     while True:
#         if turn==1:  
#             print("\n\n\Computer 1 Turn\n")
            
#             n=random.randint(1,9)
#             ch="X"
#             while True:
#                 if n in used1 or n in used2:
#                     # print("\nRElol\n")
#                     n=random.randint(1,9)
#                 else:
#                     break
#             change(n,ch)
#             used1.append(n)
#             for i in line:
#                 n1=i[0]
#                 n2=i[1]
#                 n3=i[2]
#                 if n1 in used1 and n2 in used1 and n3 in used1:
#                     print("\n\Computer 1 Wins\n\n")
#                     return False
#             display_board()
#             turn=2
#         if len(used1)+len(used2)==9:
#             print("\n\n\nTie\n\n\n")
#             break  
#         if turn==2: 
#             print("\n\n\nComputer 2 Turn\n")
            
#             n=random.randint(1,9)
#             ch="O"
#             while True:
#                 if n in used1 or n in used2:
#                     # print("\nRElol\n")
#                     n=random.randint(1,9)
#                 else:
#                     break
            
#             change(n,ch)
#             used2.append(n)
#             print("Enter :",n)
#             for i in line:
#                 n1=i[0]
#                 n2=i[1]
#                 n3=i[2]
#                 if n1 in used2 and n2 in used2 and n3 in used2:
#                     print("\n\nComputer 2 Wins\n\n")
#                     return False
#             display_board()
#             turn=1
        
#         if len(used1)+len(used2)==9:
#             print("\n\n\nTie\n\n\n")
#             break


def main():
    print("""
        Select Mode :
        1. Player to Player
        2. Player to Computer """)
    mode=int(input("Enter :"))
    display_board()
    print("\n\n\n")
    if mode==1:
        p2p()
    if mode==2:
        p2c()


while True:
    main()
    display_board()
    
    print("Do you want to play again? (y/n)")
    ans=input()
    
    if ans=='n':
        print("Thanks for playing!")
        break
    else:
        board=[[" 1 ",' 2 ',' 3 '],[' 4 ',' 5 ',' 6 '],[' 7 ',' 8 ',' 9 ']]  
        used1.clear()
        used2.clear()