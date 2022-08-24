import os

filepath = "E:/ZMQDemo/log"
newFileNmae = "newlog"
newFilePath = os.path.join(filepath, newFileNmae)
newFile = open(newFilePath, 'ab+')
files = os.listdir(filepath)
size = len(files)
for i in range(size):
    cur_file = open(os.path.join(filepath, files[size - 1 - i]), 'r')
    data = cur_file.read()
    newFile.write(bytes(data, encoding='GBK'))
    cur_file.close()
newFile.close()

