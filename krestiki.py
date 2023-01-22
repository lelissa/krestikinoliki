field=[['-','-','-'],
       ['-','-','-'],
       ['-','-','-']]
print(field)
field = [['-'] * 3 for _ in range(3)]
print(field)

field=[['-','-','-'],
       ['-','-','-'],
       ['-','-','-']]
print(field)
field = [['-'] * 3 for _ in range(3)]
print(field)

num = '  a b c'
print(num)

for row, i in zip(field, num.split()):
    print(f"{i} {' '.join(str(j) for j in row)}")

def show_field(f):
    print('  0 1 2')
    for i in range(len(f)):
        print(str(i)+' '+' '.join(f[i]))


def users_input(f):
    while True:
        place=input('Введите координаты :').split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y

count=0
while True:
    if count%2==0:
            user='x'
    else:
            user = 'o'
    show_field(field)
    if count<9:
        x, y = users_input(field)
        field[x][y]=user
    if count==9:
        print ('Ничья')
        break
    count+=1

def win_1v(f,user):
    def check_line(a1, a2, a3, user):
        if a1 ==user and a2 == user and a3 == user:
            return True
        return False
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
            check_line(f[0][n], f[1][n], f[2][n], user) or \
            check_line(f[0][0], f[1][1], f[2][2], user) or \
                     check_line(f[2][0], f[1][1], f[0][2], user):
                        return True
    return False

count=0
while True:
    if count%2==0:
            user='x'
    else:
            user = 'o'
    show_field(field)
    if count<9:
        x, y = users_input(field)
        field[x][y]=user
    if count==9:
        print ('Ничья')
        break
    if win_1v(field,user):
            print(f"Выйграл {user}")
            break
    count+=1

def win_2v(f,user):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(f[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

def win_3v(f,user):
    f_list=[]
    for l in f:
        f_list+=l
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p)))==3:
            return True
    return False