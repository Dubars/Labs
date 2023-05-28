def p1():
    from PIL import Image
    img = Image.open("Simpsons.png")
    img.show()
    width, height = img.size
    print(width, height)
    a = img.format
    print(a)
    b = img.mode
    print(b)
def p2():
    from PIL import Image
    img = Image.open("Simpsons.png")
    img.show()

    new_size = (img.width // 3, img.height // 3)
    img.thumbnail(new_size)
    img.show()
    img.save("Simpsons_2.png")

    mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    mirror_img.show()
    mirror_img.save("Simpsons_mirror.png")

    rotate_img = img.rotate(180)
    rotate_img.show()
    rotate_img.save("Simpsons_rotate.png")
def p3():
    from PIL import Image, ImageFilter
    filename = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in filename:
        with Image.open(file) as i:
            i.load()
            b = i.filter(ImageFilter.FIND_EDGES)
            b.show()
            b.save("new" + file)
def p4():
    from PIL import Image
    back = Image.open("Simpsons4.jpg")
    fore = Image.open("New.png")
    back.show()
    back.paste(fore, (100, 0), fore)
    back.show()
    back.save("New_Simpsons.png")
p1()
p2()
p3()
p4()