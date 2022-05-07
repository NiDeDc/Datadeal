import csv
import struct

filename = 'dataa.csv'
bin_data = []
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        row[0:7] = map(int, row[0:7])
        data_pack = struct.pack('i4Bqi', row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        if row[6] > 0:
            for i in range(7, 7 + row[6]):
                car_data = row[i][1:-1].split(',')
                car_data[2:5] = map(int, car_data[2:5])
                car_data[6:10] = map(int, car_data[6:10])
                # cc = car_data[1][2:-1]
                # pp = bytes(car_data[1][2:-1], encoding='utf8')
                single_data = struct.pack('Q', int(car_data[0])) + bytes(car_data[1][2:-1], encoding='utf8') + struct.pack('b', car_data[2]) + \
                              struct.pack('IIf', car_data[3], car_data[4], float(car_data[5])) + \
                              struct.pack('b', car_data[6]) + struct.pack('I', car_data[7]) + \
                              struct.pack('bb', car_data[8], car_data[9])
                data_pack += single_data
        bin_data.append(data_pack)
    kk = 5
