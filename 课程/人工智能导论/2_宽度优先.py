import time
time1=time.time()
#修改索引，方便接下来交换
def move(str,index):
    if str=='up':
        return index-3
    if str=='dowm':
        return index+3
    if str=='left':
        return  index-1
    if str=='right':
        return index+1

#生成新的结点并且记录路径
def path(array1,array2):
    p=array1[:]
    p.insert(0,array2)
    for i in close:
        if i[0] == p[0]:
             return False
    open.append(p)
    return True

#打印
def out(list):
    for j in range(len(list)):
        if j % 3 == 0:
            print('\t')
        print(list[j], end=' ')
    print('\t')

#判断8数码逆序的奇偶性
#若两个状态的逆序奇偶性相同，则可相互到达，否则不可相互到达
def issolution(array):
    num = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] == 0 or array[j] == 0:
                continue
            if array[i] < array[j]:
                num += 1
    return num%2

if __name__=="__main__":
    # orgin=input(">>").split()    #自行输出8数码初始状态
    # start=[int(x) for x in orgin]
    start=[1, 2, 3, 4, 0, 8, 6, 7, 5]
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    #如果初态和终态的逆序奇偶性不同则无解
    if issolution(start) != issolution(goal):
        print('该始末状态的8数码无解')
        exit()
    open=[]
    close=[]
    creatp=serchp=step=0
    open.append([start])
    while 1:
        if start==goal:
            print('初始状态即为解!')
            break
        if len(open)==0:
            print('未找到解')
            break
        else:
            this=open.pop(0)
            #print(this)
            if len(this)>9*8*7*6*5*4*3*2:
                break
            serchp+=1
            close.append(this)
            #print(close)
            if this[0]==goal:
                print('搜索成功')
                print('共创建{}个结点，共搜索{}个结点,共{}步'.format(creatp,serchp,len(this)-1))
                for i in this[::-1]:
                    out(i)
                time2=time.time()
                print(time2-time1)
                exit()

            #上，下，左，右扩展结点

            if this[0].index(0)>2 :
                node=this[0].copy()
                a=this[0].index(0)
                b=move('up',a)
                node[a],node[b]=node[b],node[a]
                path(this, node)
                creatp += 1

            if this[0].index(0) < 6 :
                node = this[0].copy()
                a = this[0].index(0)
                b = move('dowm', a)
                node[a],node[b]=node[b],node[a]
                path(this, node)
                creatp += 1


            if this[0].index(0) != 0 and this[0].index(0) != 3 and this[0].index(0) != 6:
                node = this[0].copy()
                a = this[0].index(0)
                b = move('left', a)
                node[a],node[b]=node[b],node[a]
                path(this, node)
                creatp+= 1


            if this[0].index(0) != 2 and this[0].index(0) != 5 and this[0].index(0) != 8:
                node = this[0].copy()
                a = this[0].index(0)
                b = move('right', a)
                node[a],node[b]=node[b],node[a]
                path(this, node)
                creatp += 1

