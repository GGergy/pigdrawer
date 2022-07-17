from PIL import Image


for i in range(1, 50):
    im = Image.open('D:\python programm\pig draw\pig' + str(i) + '.jpg')
    im = im.resize((25, 25))
    im.save('D:\python programm\pig draw\pig' + str(i) + '.jpg')
