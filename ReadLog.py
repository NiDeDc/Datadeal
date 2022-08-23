import re


class CarData:
    def __init__(self):
        self.id = 0
        self.lane = 0
        self.speed = 0
        self.position = 0
        self.range = []
        self.type = 0
        self.plate = '鄂A1V21A       '
        self.edge = 0
        self.direction = 0


class frameData:
    def __init__(self):
        self.sn = 0
        self.ip = [192, 168, 1, 100]
        self.timestamp = 0
        self.num = 0
        self.CarData = []


with open('log/newlog', encoding='GBK') as f:
    lo = f.readlines()
# 将每帧 推送的 k 和 v 存储
k_total = []
v_total = []
for row in lo:
    valid_row = re.findall(r'推送的k为|推送的v为', row)

    if len(valid_row) != 0:
        k_v_push = eval(row.split('为')[-1].split('\n')[0])
        if isinstance(k_v_push[0], list):
            v_total.append(k_v_push)
        else:
            k_total.append(k_v_push)
allData = []
for i in range(len(k_total)):
    fra = frameData()
    fra.sn = i
    fra.num = len(k_total[i])
    for j in range(len(k_total[i])):
        if j == 0:
            fra.timestamp = v_total[i][j][5]
        curV = v_total[i][j]
        carC = CarData()
        carC.id = k_total[i][j]
        if curV[0] < 4:
            if curV[0] == 0:
                carC.lane = 9
            else:
                carC.lane = 4 - curV[0]
        else:
            carC.lane = curV[0]
        carC.speed = curV[6]
        carC.position = int(curV[1])
        carC.type = curV[4]
        fra.CarData.append(carC)
    allData.append(fra)
