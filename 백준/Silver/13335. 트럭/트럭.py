n, w, l = map(int, input().split())

trucks = list(map(int, input().split()))
bridge = [0 for _ in range(w)]
ans = 0

while bridge:
    ans += 1
    bridge.pop(0)

    if trucks:
        if sum(bridge) + trucks[0] <= l:
            truck = trucks.pop(0)
            bridge.append(truck)
        else:
            bridge.append(0)

print(ans)