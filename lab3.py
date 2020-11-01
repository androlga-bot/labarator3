import math
from math import cos as cos
from math import sin as sin

x1 = -12
y1 = -17
t = 0
all_values = []
pixel = []


while t <= 5 * math.pi:#создания списка точек, которые принадлежат прямой
    x = round(t * sin(t) , 1)
    y = round(t* cos(t) , 1)
    pixel.append(x)
    pixel.append(y)
    all_values.append(tuple(pixel))
    pixel.clear()
    t += 0.1
    

with open("test.bmp","w+b") as f:
    f.write(b'BM')
    f.write((154).to_bytes(4,byteorder="little"))
    f.write((0).to_bytes(2,byteorder="little"))
    f.write((0).to_bytes(2,byteorder="little"))
    f.write((122).to_bytes(4,byteorder="little"))
    f.write((108).to_bytes(4,byteorder="little"))
    f.write((270).to_bytes(4,byteorder="little"))
    f.write((310).to_bytes(4,byteorder="little"))
    f.write((1).to_bytes(2,byteorder="little"))
    f.write((32).to_bytes(2,byteorder="little"))
    f.write((3).to_bytes(4,byteorder="little"))
    f.write((32).to_bytes(4,byteorder="little"))
    f.write((2835).to_bytes(4,byteorder="little"))
    f.write((2835).to_bytes(4,byteorder="little"))
    f.write((0).to_bytes(4,byteorder="little"))
    f.write((0).to_bytes(4,byteorder="little"))
    f.write(b'\x00\x00\xFF\x00')
    f.write(b'\x00\xFF\x00\x00')
    f.write(b'\xFF\x00\x00\x00')
    f.write(b'\x00\x00\x00\xFF')
    f.write(b' niW')
    f.write((0).to_bytes(36,byteorder="little"))
    f.write((0).to_bytes(4,byteorder="little"))
    f.write((0).to_bytes(4,byteorder="little"))
    f.write((0).to_bytes(4,byteorder="little"))


    for i in range(310):#движение по у
        x1 = -12
        
        for j in range(270):#движение по х
            if (x1, y1) in all_values:#если точка есть в списке точек принадлежащих линии 
                f.write(b'\x00\x00\x00\xFF')#то пиксель этой точки черный
            else:
                f.write(b'\xFF\xFF\xFF\xFF')#иначе белый

            x1 = round(x1 + 0.1, 1)

        y1 = round(y1 + 0.1,1)

f.close()
