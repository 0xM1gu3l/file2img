# How should this be:
# 1. It would get every byte and convert to binary
# 2. for the binary number, we assign the black dot for 1 and the white dot for 0
# 3. We make a sequence where in the video it should be
# 4. For information retrieve we should pass the length of the binary + the video.

from PIL import Image as img
from util.get_bytes_from_file import getBytesFromFile

i = 0
h = 0
nf = 0
n = 0
by = getBytesFromFile()
abl = len(by)

frame = img.new("RGBA", (3840, 2160), None)

for binary in by:
    bl = len(binary)
    # print(binary)
    for bit in binary:
        n += 1
        # print(binary)
        bit = int(bit)
        # print(bit)
        if (i == frame.width):
            if (i == frame.width and h == frame.height - 1 ):
                frame.save(f"./out/frame000{nf}.png", "png")
                frame = img.new("RGBA", (3840, 2160), None)
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
    if (n == abl):
        print("skipping add separator...")
    else:
        if (i == frame.width):
            i = 0
            h += 1
        print(f"{i} | {h}")
        frame.putpixel((i, h), (155, 155, 155, 255))
        i += 1
# exif = frame.getexif()
# exif.update((271, "Hello World"))
# print(exif.get_ifd(271))

frame.save(f"./out/frame000{nf}.png", "png")
print(f"File output at: ./out/frame000{nf}.png")
print(f"Encoding of the original file: {list(by)[1]}")