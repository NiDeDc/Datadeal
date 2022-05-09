import csv


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


AllData = []
sn = 0
f1 = open("../Datadeal/v.txt", 'r')
f2 = open("../Datadeal/k.txt", 'r')
byt1 = f1.readlines()
byt2 = f2.readlines()
for i in range(len(byt1)):
    fra = frameData()
    fra.sn = sn
    sn += 1
    nk = byt2[i]
    nv = byt1[i]
    if len(nv) < 8:
        continue
    nk = nk[:-1]
    nv = nv[:-1]
    nk = nk.strip("[]")
    nv = nv.strip("[]")
    k_list = nk.split(',')
    v_list = nv.split(',')
    num = len(v_list) // 8
    fra.num = num
    fra.timestamp = int(float(v_list[6].strip()))
    for j in range(num):
        carD = CarData()
        index = j * 8
        carD.id = int(k_list[j])
        carD.lane = int(v_list[index].strip("[ "))
        carD.position = int(v_list[index + 1])
        carD.range.append(int(v_list[index + 3][2:]))
        carD.range.append(int(v_list[index + 4][1:-1]))
        carD.type = int(v_list[index + 5])
        carD.speed = float(v_list[index + 7].strip("] "))
        if carD.speed >= 0:
            carD.direction = 0
        else:
            carD.direction = 1
        fra.CarData.append(carD)
    AllData.append(fra)
