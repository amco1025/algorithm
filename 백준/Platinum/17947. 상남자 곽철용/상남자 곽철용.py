# # 주어진 값들 받아오기
# N, M, K = map(int, input().split())
#
# # li 리스트에 주어진 카드 숫자들 입력
# li = [i for i in range(1, 4*N+1)]
#
# # 문제에 주어진 조건에 따라 카드 제거
# for _ in range(M):
#     a, b  = map(int, input().split())
#     li.remove(a)
#     li.remove(b)
#
# # 곽철용이 뽑은 숫자에 따른 곽철용 점수를 point에 저장
# a, b = map(int, input().split())
# point = abs((a%K) - (b%K))
#
# # 뽑은 값 카드 더미에서 제거
# li.remove(a)
# li.remove(b)
#
# # 찾고자 하는 값이 카드의 수가 아니고 수를 k로 나눈 나머지 이므로 카드의 수들을 나머지로 변경
# for i in range(len(li)):
#     li[i] = li[i] % K
#
# # 우선 카드 더미 중 point보다 작거나 같은 수로는 원하는 답을 찾을 수 없으므로 큰수와 작거나 같은 수로 나누어 분리
# big = []
# small = []
#
# # 만약 나머지가 큰 값들이 작은 값보다 많은 경우 절반을 맞추도록 가장 작은 값 부터 뽑아 big에서 small로 이동 시킴
# for i in li:
#     if i > point:
#         big.append(i)
#     else:
#         small.append(i)
#
# big.sort()
#
# if len(big) > len(small):
#     k = len(big) - len(li)//2
#     for _ in range(k):
#         small.append(big.pop(0))
#
#
# # 곽철용을 이길 수 있는 가장 경우의 수가 많은 경우를 찾아야 하므로 큰 리스트에서는 작은 값 부터 작은 리스트에서는 큰 값부터 넣어가며 진행
# big.sort()
# small.sort(reverse=True)
# sm = 0
#
# # 카드를 사용 하였는지 안하였는지 보여주는 리스트
# visited_i = [0] * len(big)
# visited_j = [0] * len(small)
#
#
# # 큰 리스트 값들 중 작은 순서대로 값을 하나씩 넣는다.
# for i in range(len(big)):
#     for j in range(len(small)):
#         # 작은 리스트에서 큰 값 순서대로 하나씩 값을 넣는다.
#         # 만약 사용하지 않은 수라면
#         if visited_j[j] == 0 and visited_i[i] == 0:
#             # 그 차가 곽철용 점수보다 크다면
#             if big[i] - small[j] > point:
#                 # sm을 1추가 그리고 사용했다고 푯히
#                 sm += 1
#                 visited_j[j] = 1
#                 visited_i[i] = 1
#                 break
#
# # 총 수가 곽철용을 제외한 사람의 수보다 크다면 M-1아니라면 SM 출력
# if sm > M-1:
#     print(M-1)
# else:
#     print(sm)

import sys;
input = sys.stdin.readline
N, M, K = map(int, input().split())
card = set(range(1, 4 * N + 1))
for _ in range(M):
    a, b = map(int, input().split())
    card.discard(a)
    card.discard(b)


chul = list(map(int, input().split()))
card.discard(chul[0])
card.discard(chul[1])
chul_score = abs(chul[0] % K - chul[1] % K)
card = list(card)
for i in range(len(card)):
    card[i] %= K
card.sort()
l, r, ans = 0, len(card) // 2, 0

while r < len(card) and ans < M - 1:
    if card[r] - card[l] > chul_score:
        ans, r, l = ans + 1, r + 1, l + 1
    else:
        r += 1

print(ans)