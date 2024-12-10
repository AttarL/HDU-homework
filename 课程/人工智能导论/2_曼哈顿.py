import time
time1=time.time()
def move(direction, index):
    if direction == 'up':
        return index - 3 if index >= 3 else None
    elif direction == 'down':
        return index + 3 if index <= 5 else None
    elif direction == 'left':
        return index - 1 if index % 3 != 0 else None
    elif direction == 'right':
        return index + 1 if index % 3 != 2 else None
    else:
        return None

def create(array1, array2):
    p = array1[:]
    p.insert(0, array2)
    for i in close:
        if i[0] == p[0]:
            return False
    open.append(p)
    return True

def show(lst):
    for j in range(len(lst)):
        if j % 3 == 0:
            print('\t')
        print(lst[j], end=' ')
    print('\t')

def hx(current):
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    distance = 0
    for i in range(len(current)):
        if current[i] != 0:
            current_row, current_col = i // 3, i % 3
            goal_index = goal.index(current[i])
            goal_row, goal_col = goal_index // 3, goal_index % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def parity(array):
    num = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] == 0 or array[j] == 0:
                continue
            if array[i] > array[j]:
                num += 1
    return num % 2

if __name__ == "__main__":
    start = [1, 2, 3, 4, 0, 8, 6, 7, 5]
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    # 如果初态和终态的逆序奇偶性不同则无解
    if parity(start) != parity(goal):
        print('该始末状态的8数码无解')
        exit()

    open = []
    close = []
    creatpoint = serchpoint = step = 0
    open.append([start])

    while True:
        if start == goal:
            print('初始状态即为解!')
            break

        if len(open) == 0:
            print('未找到解')
            break

        open.sort(key=lambda x: hx(x[0]))
        this = open.pop(0)
        serchpoint += 1
        close.append(this)

        if this[0] == goal:
            print('搜索成功')
            print('共创建{}个结点，共搜索{}个结点，共{}步'.format(creatpoint, serchpoint, len(this) - 1))
            for i in this[::-1]:
                show(i)
            time2 = time.time()
            print(time2 - time1)
            exit()

        zero_index = this[0].index(0)

        # 尝试上移
        if zero_index > 2:
            node = this[0].copy()
            target_index = move('up', zero_index)
            if target_index is not None:
                node[zero_index], node[target_index] = node[target_index], node[zero_index]
                if create(this, node):
                    creatpoint += 1

        # 尝试下移
        if zero_index < 6:
            node = this[0].copy()
            target_index = move('down', zero_index)
            if target_index is not None:
                node[zero_index], node[target_index] = node[target_index], node[zero_index]
                if create(this, node):
                    creatpoint += 1

        # 尝试左移
        if zero_index % 3 != 0:
            node = this[0].copy()
            target_index = move('left', zero_index)
            if target_index is not None:
                node[zero_index], node[target_index] = node[target_index], node[zero_index]
                if create(this, node):
                    creatpoint += 1

        # 尝试右移
        if zero_index % 3 != 2:
            node = this[0].copy()
            target_index = move('right', zero_index)
            if target_index is not None:
                node[zero_index], node[target_index] = node[target_index], node[zero_index]
                if create(this, node):
                    creatpoint += 1
