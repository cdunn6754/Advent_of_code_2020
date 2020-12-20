data = [20,0,1,11,6,3]

# data = [0,3,6]

last_spoken = {num: idx + 1 for idx, num in enumerate(data)}
curr_turn = len(data) + 1
while curr_turn <= 30000000:
    last_number = data[-1]
    last_spoken_turn = last_spoken.get(last_number)
    prev_turn = curr_turn - 1
    if last_spoken_turn is not None:
        data.append(prev_turn - last_spoken_turn)
    else:
        data.append(0)
    last_spoken[last_number] = prev_turn
    curr_turn += 1

print(data[-1])
