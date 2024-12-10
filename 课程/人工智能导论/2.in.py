def count_inversions(state):
    # Flatten the state into a 1D list and ignore the 0
    flat_list = [num for row in state for num in row if num != 0]
    inversions = 0

    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                inversions += 1

    return inversions

# 测试逆序数计算
initial_state = [[1, 2, 3],
                 [8, 0, 4],
                 [7, 6, 5]]

inversions = count_inversions(initial_state)
print("Inversions:", inversions)
