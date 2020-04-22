from PIL import Image


def decode_image(file_location):

    encoded_image = Image.open("images/encoded_sample.png")
    # print(encoded_image.getdata())
    pix = list(encoded_image.getdata())
    # print(pix[0])
    # for i in range(len(pix)):
    #     r = list(pix[i])[0]
    #     print(r)



    red_channel = encoded_image.split()[0]
    # print(red_channel.getdata())

    x_size = encoded_image.size[0]


    y_size = encoded_image.size[1]
    # print(y_size)

    decoded_image = Image.new("RGB", encoded_image.size)

    pixels = decoded_image.load()


    #TODO: Fill in decoding functionality

    for x in range(x_size):
        for y in range(y_size):
            # cords = x, y = x, y
            pix = red_channel.getpixel((x, y))
            # print(pix)
            pix = bin(pix)
            # print(pix)
            # print(x,y)
            pix = list(pix)
            # print(pix[3])
            p = int(pix[-1])
            # print(p)
            if p == 1:
                print(1)
                pixels[x,y] = (0,0,0)
            else:
                print(0)
                pixels[x,y] = (255,255,255)

    decoded_image.save("images/decoded_image.png")


print(decode_image("images/encoded_sample.png"))

if __name__ == "__main__":
    pass
