import csv
import struct

file = open('data4_27.bin', 'rb')
data = file.read()
with open('data4_27.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    i = 0
    while i < len(data):
        sn, ip1, ip2, ip3, ip4, t, s = struct.unpack('i4Bqi', data[i: i + 20])
        i = i + 20
        pp = [sn, ip1, ip2, ip3, ip4, t, s]
        for j in range(s):
            car_id = struct.unpack('Q', data[i: i + 8])[0]
            pp.append(car_id)
            i = i + 8
            car_plate = data[i: i + 16]
            car_plate = str(car_plate, encoding='utf8')
            pp.append(car_plate)
            i = i + 16
            car_typ = struct.unpack('b', data[i: i+1])[0]
            pp.append(car_typ)
            i = i + 1
            scope1, scope2, speed = struct.unpack('IIf', data[i: i+12])
            pp.append(scope1)
            pp.append(scope2)
            pp.append(speed)
            i = i + 12
            car_way = struct.unpack('b', data[i: i+1])[0]
            pp.append(car_way)
            i = i + 1
            mil = struct.unpack('I', data[i: i+4])[0]
            pp.append(mil)
            i = i + 4
            edge, direction = struct.unpack('bb', data[i:i+2])
            pp.append(edge)
            pp.append(direction)
            i = i + 2
        csvwriter.writerow(pp)

