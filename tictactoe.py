
list1 = [' ','1 ','|',' ','2 ','|',' ','3']
list2 = [' ','4 ','|',' ','5 ','|',' ','6']
list3 = [' ','7 ','|',' ','8 ','|',' ','9']
list4 = ['--','-','|','--','-','|','--','-']

def grid(list1,list2,list3,list4):

    L1,L2,L3,L4 = '','','',''
    for i in range(0,8):
        L1+=list1[i]
        L4+=list4[i]
        L2+=list2[i]
        L3+=list3[i]
    
    print(' '*40+L1)
    print(' '*40+L4)
    print(' '*40+L2)
    print(' '*40+L4)
    print(' '*40+L3)
    
    
def sortString(str):
    return ''.join(sorted(str))

# ----------------------------------------------------------------------------------

def win_score(lis1,lis2,lis3,lis4,lis5,lis6,lis7,lis8,lis9,player,flag):
    
    score=''
    msg=f'We have a Winner!!!! Congratulation player *** {player} ***.'
    
    if list1[1] == list1[4] == list1[7] == 'X ':
        print(msg)
        flag=False
    elif list1[1] == list1[4] == list1[7] == '0 ':
        print(msg)
        flag=False
           
    if list2[1] == list2[4] == list2[7] == 'X ':
        print(msg)
        flag=False
    elif list2[1] == list2[4] == list2[7] == '0 ':
        print(msg)
        flag=False
    
    if list3[1] == list3[4] == list3[7] == 'X ':
        print(msg)
        flag=False
    elif list3[1] == list3[4] == list3[7] == '0 ':
        print(msg)
        flag=False

    if list1[1] == list2[4] == list3[7] == 'X ':
        print(msg)
        flag=False
    elif list1[1] == list2[4] == list3[7] == '0 ':
        print(msg)
        flag=False
    
    if list1[1] == list2[1] == list3[1] == 'X ':
        print(msg)
        flag=False
    elif list1[1] == list2[1] == list3[1] == '0 ':
        print(msg)
        flag=False
    
    if list1[4] == list2[4] == list3[4] == 'X ':
        print(msg)
        flag=False
    elif list1[4] == list2[4] == list3[4] == '0 ':
        print(msg)
        flag=False
    
    if list1[7] == list2[7] == list3[7] == 'X ':
        print(msg)
        flag=False
    elif list1[7] == list2[7] == list3[7] == '0 ':
        print(msg)
        flag=False
    
    if list3[1] == list2[4] == list1[7] == 'X ':
        print(msg)
        flag=False
    elif list3[1] == list2[4] == list1[7] == '0 ':
        print(msg)
        flag=False
# --------------------------------------------------------------------
    
from IPython.display import clear_output
flag = True

list1 = [' ','1 ','|',' ','2 ','|',' ','3']
list2 = [' ','4 ','|',' ','5 ','|',' ','6']
list3 = [' ','7 ','|',' ','8 ','|',' ','9']
list4 = ['--','-','|','--','-','|','--','-']
print(' \n'*4)
grid(list1,list2,list3,list4)
lista1=''
lista2=''
count=0
player = '1'
while flag:
    
    count+=1
    choice=''
    
    print(' \n'*4)
    print(f'                                                  Player *** {player} *** your turn.')
    
    while choice not in ['1','2','3','4','5','6','7','8','9','q']:
        choice = input('Choose a Number [1 - 9] or "q" to quit: ')
    if choice == 'q':
        clear_output()
        break
    
    if choice    == '1' and player == '1':
        lista1+=choice
        list1[1] ='X '
    elif choice  == '1' and player == '2':
        lista2+=choice
        list1[1] ='0 '
        
    if choice  == '2' and player == '1':
        lista1+=choice
        list1[4] = 'X '
    elif choice  == '2' and player == '2':
        lista2+=choice
        list1[4] = '0 '
        
    if choice  == '3' and player == '1':
        lista1+=choice
        list1[7] = 'X '
    elif choice  == '3' and player == '2':
        lista2+=choice
        list1[7] = '0 '
        
    if choice  == '4' and player == '1':
        lista1+=choice
        list2[1] = 'X '
    elif choice  == '4' and player == '2':
        lista2+=choice
        list2[1] = '0 '
        
    if choice  == '5' and player == '1':
        lista1+=choice
        list2[4] = 'X '
    elif choice  == '5' and player == '2':
        lista2+=choice
        list2[4] = '0 '
        
    if choice  == '6' and player == '1':
        lista1+=choice
        list2[7] = 'X '
    elif choice  == '6' and player == '2':
        lista2+=choice
        list2[7] = '0 '
        
    if choice  == '7' and player == '1':
        lista1+=choice
        list3[1] = 'X '
    elif choice  == '7' and player == '2':
        lista2+=choice
        list3[1] = '0 '
        
    if choice  == '8' and player == '1':
        lista1+=choice
        list3[4] = 'X '
    elif choice  == '8' and player == '2':
        lista2+=choice
        list3[4] = '0 '
        
    if choice  == '9' and player == '1':
        lista1+=choice
        list3[7] = 'X '
    elif choice  == '9' and player == '2':
        lista2+=choice
        list3[7] = '0 '    
    
    if int(choice) > 9 or count == 9:
        flag = False
        
      
    clear_output()
    
    win_score(list1[1],list1[4],list1[7],list2[1],list2[4],list2[7],list3[1],list3[4],list3[7],player,flag)
    print(' \n'*4)
    grid(list1,list2,list3,list4)
    
    
    
    if player == '1':
        player = '2'
    elif player == '2':
        player = '1'  
