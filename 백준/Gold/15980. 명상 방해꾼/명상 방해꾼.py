N, M = map(int, input().split())
birds = []

for _ in range(N):
    direction, sound = input().split()
    birds.append((direction, sound))

def bird(bird_idx):
    total_effect = [0] * M
    for i, (direction, chirping) in enumerate(birds):
        if i == bird_idx:
            continue
        effect = 1 if direction == 'R' else -1
        for j in range(M):
            total_effect[j] += effect if chirping[j] == '1' else 0
    return max(abs(sum(total_effect[:i+1])) for i in range(M))

result = (0, float('inf'))
for i in range(N):
    current_disturbance = bird(i)
    if current_disturbance < result[1]:
        result = (i + 1, current_disturbance)

print(result[0])
print(result[1])
