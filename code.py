import os.path
from random import choice
from PIL import Image
PIGS = 50
REAL = 7
PIG_SIZE = 25

def transparency(im1, filename2):
    k = 0.5
    try:
        im2 = Image.open(filename2)
    except:
        raise Exception('кто-то удалил свиней')
    w, h = im1.size
    img = Image.new('RGB', (w, h), 'black')
    pixels1 = im1.load()
    pixels2 = im2.load()
    pixels3 = img.load()
    for i in range(w):
        for g in range(h):
            r = k * pixels1[i, g][0] + (1 - k) * pixels2[i, g][0]
            gr = k * pixels1[i, g][1] + (1 - k) * pixels2[i, g][1]
            b = k * pixels1[i, g][2] + (1 - k) * pixels2[i, g][2]
            pixels3[i, g] = (int(r), int(gr), int(b))
    return img


def pig_draw(filename, save_name):
    img = Image.open(filename)
    img = img.resize((PIGS * PIG_SIZE, PIGS * PIG_SIZE))
    pict = Image.new('RGB', img.size, 'black')
    n = [i for i in range(1, REAL * REAL + 1)]
    for i in range(PIGS):
        for g in range(PIGS):
            pig_id = choice(n)
            n.remove(pig_id)
            if len(n) == 0:
                n = [i for i in range(1, REAL * REAL + 1)]
            slc = img.crop((i * PIG_SIZE, g * PIG_SIZE, i * PIG_SIZE + PIG_SIZE, g * PIG_SIZE + PIG_SIZE))
            part = transparency(slc, 'pig' + str(pig_id) + '.jpg')
            pict.paste(part, (i * PIG_SIZE, g * PIG_SIZE))
    pict.save(save_name)
    pict.show()


print('gergy product®')
while True:
    print('переместите изображение, которое хотите нарисовать на свиньях (рекомедуемый формат - jpg)')
    name = input('введите имя этого изображения с указанием расширения ')
    if not os.path.isfile(name):
        print('программа не нашла этого файла')
    else:
        sv = input('под каким именем хотите сохранить картинку(с указанием расширения)? ')
        print('картинка создается...')
        pig_draw(name, sv)
        break
print('картинка успешно создана')
