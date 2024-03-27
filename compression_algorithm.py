# How should this be:
# 1. It would get every byte and convert to binary
# 2. for the binary number, we assign the black dot for 1 and the white dot for 0
# 3. We make a sequence where in the video it should be
# 4. For information retrieve we should pass the length of the binary + the video.

from PIL import Image as img
from get_bytes_from_file import getBytesFromFile

i = 0
h = 0
nf = 0
by = getBytesFromFile()
abl = len(by.replace(" ", ""))
print(abl)
print(by.split(" "))

frame = img.new("RGBA", (3840, 2160), None)

for binary in by.split(" "):
    bl = len(binary)
    print(bl)
    # print(binary)
    for bit in binary:
        # print(binary)
        bit = int(bit)
        # print(bit)
        if (i == frame.width):
            # print(f"{i} | {h}")
            if (i == frame.width and h == frame.height - 1 ):
                frame.save(f"./out/frame000{nf}.png", "png")
                nf += 1
                i = 0
                h = 0
            else:
                i = 0
                h += 1
        # print(f"W: {i} | H: {h}")
        r_0_1 = bit
        if r_0_1 == 0:
            # print("O bit é 0")
            frame.putpixel((i, h), (0, 0, 0, 255))
        if r_0_1 == 1:
            # print("O bit é 1")
            frame.putpixel((i, h), (255, 255, 255, 255))
        i += 1
frame.save(f"./out/frame000{nf}.png", "png")