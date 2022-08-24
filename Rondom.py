import random

pos = [3521.8, 3524]
speed = [36, 39.6]
pos_ = [2, 2.2]
msg = []
for i in range(500):
    cur_pos = random.uniform(pos[0], pos[1])
    cur_speed = random.uniform(speed[0], speed[1])
    sig_str = "1{ \"command\": 1, \"id\": \"{84fed2e8-758b-4b77-a464-7bf75598aa58}\", \"info\": \"波音738\", \"pos\": " \
              + str(cur_pos) + ", \"pressure\": 0, \"sn\": 0, \"speed\": " + str(cur_speed) \
              + ", \"time\": \"1970-01-01 08:00:00:000\", " \
                "\"type\": 0, \"way\": \"AH\", \"x_direct\": 1, \"y_direct\": 0 }"
    msg.append(sig_str)
    pos[0] = pos[0] - pos_[0]
    pos[1] = pos[1] - pos_[1]
for i in range(len(msg)):
    print(msg[-1 - i])
