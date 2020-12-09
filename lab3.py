import math
from math import cos as cos
from math import sin as sin

t = 0
all_values = []
pixel = []
min_x = []
min_y = []


while t <= 5 * math.pi:#создания списка точек, которые принадлежат прямой
    x = round(t * sin(t) , 1)
    y = round(t* cos(t) , 1)
    pixel.append(x)
    pixel.append(y)
    min_x.append(x)
    min_y.append(y)
    all_values.append(tuple(pixel))
    pixel.clear()
    t += 0.1
    
x_paint = round(min(min_x)) - 2
y_paint = round(min(min_y)) - 2


with open("test.bmp","w+b") as fail:
    fail.write(b'BM')
    fail.write((154).to_bytes(4, byteorder="little"))
    fail.write((0).to_bytes(2, byteorder="little"))
    fail.write((0).to_bytes(2, byteorder="little"))
    fail.write((122).to_bytes(4, byteorder="little"))
    fail.write((108).to_bytes(4, byteorder="little"))
    fail.write((270).to_bytes(4, byteorder="little"))
    fail.write((310).to_bytes(4, byteorder="little"))
    fail.write((1).to_bytes(2, byteorder="little"))
    fail.write((32).to_bytes(2, byteorder="little"))
    fail.write((3).to_bytes(4, byteorder="little"))
    fail.write((32).to_bytes(4, byteorder="little"))
    fail.write((2835).to_bytes(4, byteorder="little"))
    fail.write((2835).to_bytes(4, byteorder="little"))
    fail.write((0).to_bytes(4, byteorder="little"))
    fail.write((0).to_bytes(4, byteorder="little"))
    fail.write(b'\x00\x00\xFF\x00')
    fail.write(b'\x00\xFF\x00\x00')
    fail.write(b'\xFF\x00\x00\x00')
    fail.write(b'\x00\x00\x00\xFF')
    fail.write(b' niW')
    fail.write((0).to_bytes(36, byteorder="little"))
    fail.write((0).to_bytes(4, byteorder="little"))
    fail.write((0).to_bytes(4, byteorder="little"))
    fail.write((0).to_bytes(4, byteorder="little"))


    for add_y in range(310):#движение по у
        x_paint = round(min(min_x)) - 2
        for add_x in range(270):#движение по х
            if (x_paint, y_paint) in all_values:#если точка есть в списке точек принадлежащих линии 
                fail.write(b'\x00\x00\x00\xFF')#то пиксель этой точки черный
            else:
                fail.write(b'\xFF\xFF\xFF\xFF')#иначе белый

            x_paint = round(x_paint + 0.1, 1)

        y_paint = round(y_paint + 0.1,1)

fail.close()
