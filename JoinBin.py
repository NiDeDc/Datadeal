import os

filePath = os.getcwd()
newFileName = ''
newFile = None
files = os.listdir(filePath)
for file in files:
    if os.path.isfile(os.path.join(filePath, file)) and file.endswith('.bin') \
            and file.split('_')[0][0] == 'D' and file.split('_')[1][0] == 'C':
        if newFileName == '':
            newFileName = file
            newFilePath = os.path.join(filePath, 'new')
            if not os.path.exists(newFilePath):
                os.makedirs(newFilePath)
                print('makedir', newFilePath)
            if os.path.exists(os.path.join(newFilePath, newFileName)):
                os.remove(os.path.join(newFilePath, newFileName))
                print('remove file', os.path.join(newFilePath, newFileName))
            newFile = open(os.path.join(newFilePath, newFileName), 'ab+')
            print("open newFile", newFilePath, newFileName)
        else:
            if file.split('_')[0] != newFileName.split('_')[0] \
                    or file.split('_')[1] != newFileName.split('_')[1]:
                newFile.close()
                newFileName = file
                newFilePath = os.path.join(filePath, 'new')
                if not os.path.exists(newFilePath):
                    os.makedirs(newFilePath)
                    print('makedir', newFilePath)
                if os.path.exists(os.path.join(newFilePath, newFileName)):
                    os.remove(os.path.join(newFilePath, newFileName))
                    print('remove file', os.path.join(newFilePath, newFileName))
                newFile = open(os.path.join(newFilePath, newFileName), 'ab+')
                print("open newFile", newFilePath, newFileName)
        curFile = open(os.path.join(filePath, file), 'rb')
        print('open curFile', file)
        data = curFile.read()
        newFile.write(data)
        curFile.close()
        print("close", file)
if newFile is not None:
    newFile.close()
    print("close", newFileName)
