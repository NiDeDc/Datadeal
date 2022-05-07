import csv
import numpy as np
from collections import defaultdict
import os


class RoadEncoder(object):
    def __init__(self, filepath='CodingSheet.csv', lanes=4):
        self.LaneData = [[] for x in range(lanes)]  # 映射数组
        self.MilData = [[] for x in range(lanes)]  # 里程数组
        self.CurTimestamp = 0
        self.EncodDict = defaultdict(list)
        self.SingleFrame = 50
        self.LoadCodingSheet(filepath)

    def LoadCodingSheet(self, filepath):
        csv_file = open(filepath, "r", encoding='utf_8_sig')
        reader = csv.reader(csv_file)
        for item in reader:
            self.EncodDict['-'.join(item[0:3])].append('-'.join(item[3:5]))
            lane = int(item[3]) - 1
            mil = float(item[4])
            self.MilData[lane].append(mil)
        for i in range(len(self.MilData)):
            self.MilData[i].sort()
            row = self.SingleFrame
            col = len(self.MilData[i])
            self.LaneData[i] = np.zeros((row, col))
        pass

    def CodingData(self, data1, data2):
        for j in range(len(data1)):
            dev = 1
            ch = j+1
            for z in range(len(data1[j])):
                key_sensor = '-'.join(map(str, [dev, ch, z]))
                val_mil = self.EncodDict.get(key_sensor)
                if val_mil is not None:
                    for val_iterator in val_mil:
                        val_mil_list = val_iterator.split('-')
                        lane = int(val_mil_list[0]) - 1
                        mil = float(val_mil_list[1])
                        index = self.MilData[lane].index(mil)
                        lane_data = self.LaneData[lane]
                        lane_data[:, index] = data1[j][:, i]
        for h in range(len(data2)):
            dev = 1
            ch = h + 1
            for z in range(len(data1[h])):
                key_sensor = '-'.join(map(str, [dev, ch, z]))
                val_mil = self.EncodDict.get(key_sensor)
                if val_mil is not None:
                    for val_iterator in val_mil:
                        val_mil_list = val_iterator.split('-')
                        lane = int(val_mil_list[0]) - 1
                        mil = float(val_mil_list[1])
                        index = self.MilData[lane].index(mil)
                        lane_data = self.LaneData[lane]
                        lane_data[:, index] = data1[h][:, i]


def LoadingData(filedir):
    files = os.listdir(filedir)
    joint_data = None
    for files in files:
        single_data = LoadSingleFile(filedir + '/' + files)
        if single_data is not None:
            if joint_data is not None:
                if joint_data.shape[0] == single_data.shape[0]:
                    joint_data = np.hstack((joint_data, single_data))
                else:
                    joint_data = None
                    break
            else:
                joint_data = single_data
        else:
            joint_data = None
            break
    return joint_data


def LoadSingleFile(path):
    try:
        col = int(os.path.split(path)[1].split('_')[2][1:])
        bin_file = np.fromfile(path, dtype=np.float32)
        size = len(bin_file)
        row = int(size / col)
        data_array = bin_file.reshape((row, col))
        data_array_t = data_array.T
        return data_array_t
    except:
        return None


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    r = RoadEncoder()
    D1ChData = [[] for x in range(4)]  # 光栅数组
    D2ChData = [[] for x in range(2)]
    for i in range(len(D1ChData)):
        filepath1 = 'C:/Users/NiDeDc/Desktop/高速编码/滤波1/1/' + str(i + 1)
        D1ChData[i].append(LoadingData(filepath1))
    for i in range(len(D2ChData)):
        filepath2 = 'C:/Users/NiDeDc/Desktop/高速编码/滤波1/2/' + str(i + 1)
        D2ChData[i].append(LoadingData(filepath2))
    r.CodingData(D1ChData, D2ChData)
    pass
