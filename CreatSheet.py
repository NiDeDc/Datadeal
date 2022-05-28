import csv

MileRange = [4043, 4744.3]
sensorRange = [[104, 244], [2, 143], [3 ,145], [0, 140]]
sensorDiff = []
for i in sensorRange:
    sensorDiff.append(i[1] - i[0])
sensorNum = max(map(abs, sensorDiff))
MileData = [MileRange[0]]
sensorData = [[sensorRange[0][0]], [sensorRange[1][0]], [sensorRange[2][0]], [sensorRange[3][0]]]
for i in range(sensorNum):
    MileData.append(MileRange[0] + (i+1) * (MileRange[1] - MileRange[0]) / sensorNum)
    for j in range(len(sensorData)):
        sensor_value = round(sensorRange[j][0] + (i+1) * sensorDiff[j] / sensorNum)
        sensorData[j].append(sensor_value)
with open('sheet.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for i in range(len(sensorData)):
        singleSensorData = sensorData[i]
        for j in range(len(MileData)):
            pp = [1, i+1, singleSensorData[j], i+1, MileData[j]]
            csvwriter.writerow(pp)


