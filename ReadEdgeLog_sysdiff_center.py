import os
from datetime import datetime
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dir_path = "./EdgeLog"
file_list = os.listdir(dir_path)
cache_log = [[], []]
put_cache_log = [[], []]
cal_log = [[], []]
send_log = [[], []]
map_log = [[], []]
txt_log = []
for file in file_list:
    print(f"正在读取{file}...")
    file_control = open(os.path.join(dir_path, file), 'r', encoding='GBK')
    txt_list = file_control.readlines()
    file_control.close()
    for sin_list in txt_list:
        if "时间对齐" in sin_list:
            str_list = sin_list.split(' ')
            timestamp = int(datetime.strptime(str_list[0] + str_list[1], '%Y-%m-%d%H:%M:%S.%f').timestamp() * 1000)
            num = int(str_list[2].strip('\n').split(':')[1])
            cache_log[0].append(timestamp)
            cache_log[1].append(num)
        elif "放入" in sin_list:
            str_list = sin_list.split(' ')
            timestamp = int(datetime.strptime(str_list[0] + str_list[1], '%Y-%m-%d%H:%M:%S.%f').timestamp() * 1000)
            diff = int(str_list[9])
            put_cache_log[0].append(timestamp)
            # diff += 500
            put_cache_log[1].append(diff)
        elif "数据形状" in sin_list:
            str_list = sin_list.split(' ')
            timestamp = int(datetime.strptime(str_list[0] + str_list[1], '%Y-%m-%d%H:%M:%S.%f').timestamp() * 1000)
            diff = int(str_list[2].strip('\n').split(' ')[-1])
            cal_log[0].append(timestamp)
            # if diff < -9000:
            #     print(timestamp)
            # if timestamp <= 1660068691023:
            #     diff += 10131
            cal_log[1].append(diff)
        elif "轨迹计算结束" in sin_list:
            str_list = sin_list.split(' ')
            timestamp = int(datetime.strptime(str_list[0] + str_list[1], '%Y-%m-%d%H:%M:%S.%f').timestamp() * 1000)
            diff = int(str_list[11])
            send_log[0].append(timestamp)
            # diff += 75
            send_log[1].append(diff)
            # if diff < -9000:
            #     print(timestamp)
        elif "join" in sin_list:
            str_list = sin_list.split(' ')
            timestamp = int(datetime.strptime(str_list[0] + str_list[1], '%Y-%m-%d%H:%M:%S.%f').timestamp() * 1000)
            diff = int(str_list[14])
            map_log[0].append(timestamp)
            # if diff < -9000:
            #     print(timestamp)
            map_log[1].append(diff)
        else:
            pass
start_str = datetime.fromtimestamp(put_cache_log[0][0] / 1000).strftime('%Y-%m-%d %H:%M:%S')
end_str = datetime.fromtimestamp(put_cache_log[0][-1] / 1000).strftime('%Y-%m-%d %H:%M:%S')
# y_max = put_cache_log[1][-1]
# y_min = put_cache_log[1][0]
# x_max = put_cache_log[0][-1]
# x_min = put_cache_log[0][0]
# k = (y_max - y_min) / (x_max - x_min)
# for i in range(len(put_cache_log[0])):
#     if i != 0:
#         put_cache_log[1][i] -= k * (put_cache_log[0][i] - put_cache_log[0][0]) + put_cache_log[1][0]
#         put_cache_log[1][i] += 75
# for i in range(len(send_log[0])):
#     if i != 0:
#         send_log[1][i] -= k * (send_log[0][i] - send_log[0][0]) + send_log[1][0]
#         send_log[1][i] += 25
print(sum(put_cache_log[1]) / len(put_cache_log[1]))
print(max(put_cache_log[1]))
print(sum(send_log[1]) / len(send_log[1]))
print(max(send_log[1]))
print(sum(cache_log[1]) / len(cache_log[1]))
print(max(cache_log[1]))
for i in range(3):
    ax = plt.subplot(3, 1, i + 1)
    plt.sca(ax)
    if i == 0:
        plt.plot(put_cache_log[0][1:], put_cache_log[1][1:])
        # plt.plot(put_cache_log[0], put_cache_log[1])
        plt.title('放入缓冲区时间差曲线  T1-T0(ms)')
        plt.ylabel('时间差/ms')
        plt.xlabel('时间轴/ms')
        plt.ylim(0, 1000)
    elif i == 1:
        plt.plot(cache_log[0], cache_log[1])
        plt.title('时间对齐缓冲区大小曲线(个)')
        plt.ylabel('缓冲区数量/个')
        plt.xlabel('时间/ms')
        plt.ylim(0, 20)
    elif i == 2:
        plt.plot(send_log[0][1:], send_log[1][1:])
        # plt.plot(send_log[0], send_log[1])
        plt.title('计算结束时间差曲线  T2-T0(ms)')
        plt.ylabel('时间差/ms')
        plt.xlabel('时间轴/ms')
        plt.ylim(0, 1000)
    elif i == 3:
        plt.plot(cal_log[0], cal_log[1])
        plt.title('合帧结束开始计算的时间差曲线')
        plt.ylabel('时间差/ms')
        plt.xlabel('时间轴/ms')
    elif i == 4:
        plt.plot(map_log[0], map_log[1])
        # plt.ylim(-1000, 1000)
        plt.title('数据映射时间差曲线')
        plt.ylabel('时间差/ms')
        plt.xlabel('时间轴/ms')
plt.subplots_adjust(left=0.044, bottom=0.056, right=0.992, top=0.930, wspace=0.200, hspace=0.718)
plt.suptitle(f'时间段 ： {start_str} 至 {end_str}')
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()
