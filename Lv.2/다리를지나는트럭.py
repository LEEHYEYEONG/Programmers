from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    current = 0
    num = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while len(truck_weights):
        answer += 1
        current_truck = truck_weights.popleft()
        # 다리 위로 올라갈 수 있는 경우 
        if (weight >= current + current_truck or weight >= current - num[0] + current_truck):
            num.append(current_truck)
            current = current - num.popleft() + current_truck
        else:
            truck_weights.insert(0, current_truck)
            num.append(0)
            current -= num.popleft() 
            
    return answer + bridge_length

print(solution(bridge_length=100, weight=100, truck_weights=[10,10,10,10,10,10,10,10,10,10]))