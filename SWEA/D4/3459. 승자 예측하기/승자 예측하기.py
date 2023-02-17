test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())
    flag = 0
    N//=2
    N+=1
    while N > 1:
        if flag:
            N = (N+1)//2
        else:
            N//=2
        flag = 1-flag
    if flag:
        print(f"#{tc} Alice")
    else:
        print(f"#{tc} Bob")

# T = int(input())
# 
# for tc in range(1, T + 1):
#     N = int(input())
#     Alice = []
#     Bob = []
#     cnt = 2
#     plu = 3
#     s = Bob
# 
#     for i in range(1, N + 1):
#         if i <= cnt:
#             s.append(i)
#         else:
#             cnt = cnt + plu
#             plu += 1
#             if s == Bob:
#                 s = Alice
#             else:
#                 s = Bob
#             s.append(i)
#     answer = ""
#     if N in Alice:
#         answer = 'Alice'
#     else:
#         answer = 'Bob'
# 
#     print("#" + str(tc) + " " + answer)

# 시간초과 다시 풀기