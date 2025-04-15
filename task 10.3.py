from PIL import Image, ImageDraw, ImageFont
import os
os.makedirs("именные открытки", exist_ok=True)
cards = {"День Бабаевского шоколада": "открытки/бабаевский шоколад.jpg", "День хинкалей в виде мопсов": "открытки/мопсы-хинкали.jpg", "День правила буравчика": "открытки/правило буравчика.jpg", "День принцессы": "открытки/принцесса.jpg", "День тигрового рулета": "открытки/тигровый рулет.jpg"}
k=1
print("Список праздников:")
for key in cards:
    print(str(k), key)
    k+=1
day = input("Выберите праздник из списка и введите его название: ")

if day in cards:
    card = Image.open(cards[day])
    name = input("Введите имя человека, которого хотите поздравить: ")+ ", поздравляю!"
    shrift = ImageFont.truetype("XI20.ttf", 100)
    draw = ImageDraw.Draw(card)
    match day:
        case "День Бабаевского шоколада":
            text_position = (50,1200)
            for sdvig in range(-4, 5):
                draw.text((text_position[0] + sdvig, text_position[1]), name, font=shrift, fill="#FFFFFF")
                draw.text((text_position[0], text_position[1] + sdvig), name, font=shrift, fill="#FFFFFF")
            draw.text(text_position, name, font=shrift, fill="#8B4513")

        case "День хинкалей в виде мопсов":
            text_position = (650, 1300)
            for sdvig in range(-4, 5):
                draw.text((text_position[0] + sdvig, text_position[1]), name, font=shrift, fill="#191970")
                draw.text((text_position[0], text_position[1] + sdvig), name, font=shrift, fill="#191970")
            draw.text(text_position, name, font=shrift, fill="#FFFFFF")

        case "День правила буравчика":
            text_position = (80, 1160)
            for sdvig in range(-4, 5):
                draw.text((text_position[0] + sdvig, text_position[1]), name, font=shrift, fill="#003636")
                draw.text((text_position[0], text_position[1] + sdvig), name, font=shrift, fill="#003636")
            draw.text(text_position, name, font=shrift, fill="#faffff")

        case "День принцессы":
            text_position = (80, 530)
            for sdvig in range(-4, 5):
                draw.text((text_position[0] + sdvig, text_position[1]), name, font=shrift, fill="#FF1493")
                draw.text((text_position[0], text_position[1] + sdvig), name, font=shrift, fill="#FF1493")
            draw.text(text_position, name, font=shrift, fill="#FFFFFF")

        case "День тигрового рулета":
            text_position = (650, 340)
            for sdvig in range(-4, 5):
                draw.text((text_position[0] + sdvig, text_position[1]), name, font=shrift, fill="#422000")
                draw.text((text_position[0], text_position[1] + sdvig), name, font=shrift, fill="#422000")
            draw.text(text_position, name, font=shrift, fill="#FFDEAD")
    card.save("именные открытки/"+day + name + ".png")
    card.show()
else: print("Праздника пока нет в списке, выберите другой(")