import os
from datetime import datetime
from matplotlib import pyplot as plt
import copy

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dir_path = "./EdgeLog"
file_list = os.listdir(dir_path)
cache_log = [[], []]
put_cache_log = [[], []]
cal_log = [[], [], []]
send_log = [[], [], []]
map_log = [[], [], []]
for file in file_list:
    print(f"正在读取{file}...")
    file_control = open(os.path.join(dir_path, file), 'r', encoding='utf-8')
    txt_list = file_control.readlines()
    file_control.close()
    for sin_list in txt_list:
        if "时间对齐" in sin_list:
            str_list = sin_list.split('|')
            timestamp = int(datetime.strptime(str_list[0], '%Y-%m-%d %H:%M:%S.%f ').timestamp() * 1000)
            num = int(str_list[2].strip('\n').split(':')[1])
            cache_log[0].append(timestamp)
            cache_log[1].append(num)
        elif "放入" in sin_list:
            str_list = sin_list.split('|')
            timestamp = int(datetime.strptime(str_list[0], '%Y-%m-%d %H:%M:%S.%f ').timestamp() * 1000)
            diff = int(str_list[2].strip('\n').split(' ')[-1])
            put_cache_log[0].append(timestamp)
            put_cache_log[1].append(diff)
        elif "数据形状" in sin_list:
            str_list = sin_list.split('|')
            timestamp = int(datetime.strptime(str_list[0], '%Y-%m-%d %H:%M:%S.%f ').timestamp() * 1000)
            diff = int(str_list[2].strip('\n').split(' ')[-1])
            GPS_time = int(str_list[2].strip('\n').split(' ')[6][3:-1])
            cal_log[0].append(timestamp)
            cal_log[1].append(diff)
            cal_log[2].append(GPS_time)
        elif "数据发送" in sin_list:
            str_list = sin_list.split('|')
            timestamp = int(datetime.strptime(str_list[0], '%Y-%m-%d %H:%M:%S.%f ').timestamp() * 1000)
            diff = int(str_list[2].strip('\n').split(' ')[-1])
            GPS_time = int(str_list[2].strip('\n').split(' ')[3][3:-1])
            send_log[0].append(timestamp)
            send_log[1].append(diff)
            send_log[2].append(GPS_time)
        elif "GPS" in sin_list:
            str_list = sin_list.split('|')
            timestamp = int(datetime.strptime(str_list[0], '%Y-%m-%d %H:%M:%S.%f ').timestamp() * 1000)
            diff = int(str_list[2].strip('\n').split(' ')[-1])
            GPS_time = int(str_list[2].strip('\n').split(' ')[7].strip(','))
            map_log[0].append(timestamp)
            map_log[1].append(diff)
            map_log[2].append(GPS_time)
        else:
            pass
a = copy.deepcopy(cal_log)
b = copy.deepcopy(map_log)
c = copy.deepcopy(send_log)
join_log = [[], []]
last_log = [[], []]
print("开始计算耗时")
for i in range(len(a[2])):
    GPS_flag = a[2][i]
    for j in range(len(b[2])):
        if GPS_flag == b[2][j]:
            join_log[0].append(a[0][i])
            join_log[1].append(a[0][i] - b[0][j])

            break
    for z in range(len(c[2])):
        if GPS_flag == c[2][z]:
            last_log[0].append(a[0][i])
            last_log[1].append(c[0][z] - a[0][i])
            break
start_str = datetime.fromtimestamp(put_cache_log[0][0] / 1000).strftime('%Y-%m-%d %H:%M:%S')
end_str = datetime.fromtimestamp(put_cache_log[0][-1] / 1000).strftime('%Y-%m-%d %H:%M:%S')
for i in range(5):
    ax = plt.subplot(5, 1, i + 1)
    plt.sca(ax)
    if i == 0:
        plt.plot(cache_log[0], cache_log[1])
        plt.title('时间对齐缓冲区大小曲线')
        plt.ylabel('缓冲区数量/个')
        plt.xlabel('时间/ms')
        # plt.ylim(0, 10)
    elif i == 1:
        plt.plot(put_cache_log[0], put_cache_log[1])
        # plt.ylim(-2000, 2000)
        plt.title('放入缓冲区时间差曲线')
        plt.ylabel('时间差/ms')
        plt.xlabel('时间轴/ms')
    elif i == 2:
        plt.plot(map_log[0], map_log[1])
        # plt.ylim(-1000, 1000)
        plt.title('数据映射时间差曲线')
        plt.ylabel('时间差/ms')
        plt.xlabel('时间轴/ms')
    elif i == 3:
        plt.plot(cal_log[0], cal_log[1])
        plt.title('合帧结束开始计算的时间差曲线')
        plt.ylabel('时间差/ms')
        plt.xlabel('时间轴/ms')
    elif i == 4:
        plt.plot(send_log[0], send_log[1])
        # plt.ylim(-1000, 1000)
        plt.title('数据发送时间差曲线')
        plt.ylabel('时间差/ms')
        plt.xlabel('时间轴/ms')
plt.subplots_adjust(left=0.044, bottom=0.056, right=0.992, top=0.930, wspace=0.200, hspace=0.718)
plt.suptitle(f'时间段 ： {start_str} 至 {end_str}')
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()
