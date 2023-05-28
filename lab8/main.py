def p1():
    from PIL import Image

    image = Image.open("lab8-1.jpg")
    image.show()
    area = (0, 0, 200, 200)
    cropped_img = image.crop(area)
    cropped_img.show()
    cropped_img.save("new_img.jpg")

def p2():
    from PIL import Image

    a = {"день рождения": "dr.jpg", "8 марта": "8m.jpg", "23 февраля": "23f.jpg"}

    holiday = input("Введите название праздника: ")
    if holiday not in a:
        print("Открытка не найдена")
    else:
        card_file = a[holiday]
        card_image = Image.open(card_file)
        card_image.show()

def p3():
    from PIL import Image, ImageDraw, ImageFont

    name = input("Введите имя получателя: ")
    image = Image.open("lab8-1.jpg")

    text_area = (0, 0, 200, 200)

    draw = ImageDraw.Draw(image)
    text = f"{name}, поздравляю!"

    font_size = 60
    font_type = "arial_bold.ttf"
    font = ImageFont.truetype(font_type, font_size)
    draw.text((400, 1000), text, font=font, fill=(0, 0, 0))
    image.show()
    image.save("new3.png")
p1()
p2()
p3()