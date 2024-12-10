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
def create(array1,array2):
    p=array1[:]
    p.insert(0,array2)
    for i in close:
        if i[0] == p[0]:
            return False
    open.append(p)
    return True

#打印
def show(list):
    for j in range(len(list)):
        if j % 3 == 0:
            print('\t')
        print(list[j], end=' ')
    print('\t')

#估计函数，与目标结点对比，返回当前数码与目标数码相同位置的个数
def hx(current):
    count=0
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    for i in range(len(current)):
        if current[i]==goal[i]:
            count+=1
    return count

def parity(array):
    num = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] == 0 or array[j] == 0:
                continue
            if array[i] < array[j]:
                num += 1
    return num%2


if __name__=="__main__":

    #orgin=input(">>").split()
    #start=[int(x) for x in orgin]
    start=[1,2,3,4,0,8,6,7,5]
    goal=[1,2,3,8,0,4,7,6,5]
    # 如果初态和终态的逆序奇偶性不同则无解
    if parity(start) != parity(goal):
        print('该始末状态的8数码无解')
        exit()
    open=[]
    close=[]
    creatpoint=serchpoint=step=0
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
            serchpoint+=1
            close.append(this)
            if this[0]==goal:
                print('搜索成功')
                print('共创建{}个结点，共搜索{}个结点,共{}步'.format(creatpoint,serchpoint,len(this)-1))
                for i in this[::-1]:
                    show(i)
                time2 = time.time()
                print(time2 - time1)
                exit()

            #上
            if this[0].index(0)>2 :
                node=this[0].copy()
                a=this[0].index(0)
                b=move('up',a)
                node[a],node[b]=node[b],node[a]
                create(this, node)
                creatpoint += 1

            #下
            if this[0].index(0) < 6 :
                node = this[0].copy()
                a = this[0].index(0)
                b = move('dowm', a)
                node[a],node[b]=node[b],node[a]
                create(this, node)
                creatpoint += 1

            #左
            if this[0].index(0) != 0 and this[0].index(0) != 3 and this[0].index(0) != 6:
                node = this[0].copy()
                a = this[0].index(0)
                b = move('left', a)
                node[a],node[b]=node[b],node[a]
                create(this, node)
                creatpoint += 1

            #右
            if this[0].index(0) != 2 and this[0].index(0) != 5 and this[0].index(0) != 8:
                node = this[0].copy()
                a = this[0].index(0)
                b = move('right', a)
                node[a],node[b]=node[b],node[a]
                create(this, node)
                creatpoint += 1

            #对与目标数码结点相同个数最多的数码结点放到open表最前面
            for i in range(len(open)-1):
                for j in range(i+1,len(open)):
                    if hx(open[i][0])<hx(open[j][0]):
                        open[i],open[j]=open[j],open[i]


