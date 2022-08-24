import os
from datetime import datetime
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dir_path = "./ReceiveLog"
file_list = os.listdir(dir_path)
ch_log = [[[], []], [[], []], [[], []], [[], []]]
for file in file_list:
    print(f"正在读取{file}...")
    file_control = open(os.path.join(dir_path, file), 'r', encoding='utf-8')
    txt_list = file_control.readlines()
    file_control.close()
    for sin_list in txt_list:
        if "receive" in sin_list:
            str_list = sin_list.split(' ')
            channel = int(str_list[4].split('-')[1].strip(','))
            diff = int(str_list[13])
            timestamp = int(datetime.strptime(' '.join(str_list[0:2]), '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000)
            ch_log[channel][0].append(timestamp)
            ch_log[channel][1].append(diff)
            pass
start_str = datetime.fromtimestamp(ch_log[0][0][0] / 1000).strftime('%Y-%m-%d %H:%M:%S')
end_str = datetime.fromtimestamp(ch_log[0][0][-1] / 1000).strftime('%Y-%m-%d %H:%M:%S')
for i in range(len(ch_log)):
    plt.plot(ch_log[i][0], ch_log[i][1], label=f"ch{i}")
    # plt.plot(put_cache_log[0], put_cache_log[1])
plt.title('各通道接收时间差(ms)')
plt.ylabel('时间差/ms')
plt.xlabel('时间轴/ms')
plt.ylim(-2000, 2000)
plt.subplots_adjust(left=0.044, bottom=0.056, right=0.992, top=0.930, wspace=0.200, hspace=0.718)
plt.suptitle(f'时间段 ： {start_str} 至 {end_str}')
plt.legend()
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()
pass
