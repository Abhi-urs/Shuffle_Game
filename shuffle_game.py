from random import shuffle
my_list=[' ','0',' ']
a=[0,1,2]
shuffle(my_list)
n=''
while n not in a:
    n=int(input('enter ur lucky index number in (0 1 2) : '))
if my_list[n]=='0':
    print("lucky my boy u got it")
    print('shuffled list:',my_list)

else:
    print("luck ledhu bhaya ")
    print('shuffled list:',my_list)