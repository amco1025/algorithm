def find_route(land1, land2, index1, index2, visited, n, curr_i1):
    curr_i2 = index2[land1[curr_i1]]
    left_i1, right_i1 = (curr_i1 - 1) % n, (curr_i1 + 1) % n
    left_i2, right_i2 = (curr_i2 - 1) % n, (curr_i2 + 1) % n
     
    while True:
        visited[land1[curr_i1]] = 1
        if left_i1 == right_i1:
            return True
        if land1[left_i1] == land2[left_i2]:
            curr_i1, left_i1, curr_i2, left_i2 = left_i1, (left_i1 - 1) % n, left_i2, (left_i2 - 1) % n
        elif land1[left_i1] == land2[right_i2]:
            curr_i1, left_i1, curr_i2, right_i2 = left_i1, (left_i1 - 1) % n, right_i2, (right_i2 + 1) % n
        elif land1[right_i1] == land2[left_i2]:
            curr_i1, right_i1, curr_i2, left_i2 = right_i1, (right_i1 + 1) % n, left_i2, (left_i2 - 1) % n
        elif land1[right_i1] == land2[right_i2]:
            curr_i1, right_i1, curr_i2, right_i2 = right_i1, (right_i1 + 1) % n, right_i2, (right_i2 + 1) % n
        else:
            return False
 
 
tests = int(input())
for t in range(tests):
    n = int(input())
    land1 = list(map(int, input().split()))
    land2 = list(map(int, input().split()))
    index1 = [0] * (n + 1)
    index2 = [0] * (n + 1)
    i = 0
    for l1 in land1:
        index1[l1] = i
        i += 1
    i = 0
    for l2 in land2:
        index2[l2] = i
        i += 1
    found = False
    visited = [0] * (n + 1)
    for j in range(n):
        if visited[land1[j]] == 1:
            continue
        found = find_route(land1, land2, index1, index2, visited, n, j)
        if found:
            break
    if found:
        print(f"#{t+1} 1")
    else:
        print(f"#{t+1} -1")