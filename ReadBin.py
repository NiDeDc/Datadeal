import struct

file = open('data4_27.bin', 'rb')
offSet = 2
data = file.read()
version, ttype = struct.unpack('2h', data[offSet:offSet+4])
offSet += 4
msgId, length = struct.unpack('2I', data[offSet: offSet + 8])
ll = length + 16
offSet += 8
cType, dev, ch = struct.unpack('3h', data[offSet: offSet + 6])
offSet += 6
sensor, data_length, Timestamp = struct.unpack('2IQ', data[offSet:offSet+16])
bag_num = len(data) // ll
cc = 6
