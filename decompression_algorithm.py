from PIL import Image as image


compressed_img = image.open("./out/frame0000.png")

n = 0
fin_arr = []
bin_arr = []
for data in list(compressed_img.getdata()):
    if (len(bin_arr) == 8):
        bits = "".join(bin_arr)
        fin_arr.append(chr(int(bits[:8], 2)))
        bin_arr = []
    if data != (0, 0, 0, 0):
        if data == (0, 0, 0, 255):
            bin_arr.append("0")
        elif data == (255, 255, 255, 255):
            bin_arr.append("1")
    # input(f"{bin_arr} <-- len: {len(bin_arr)}")
print("".join(fin_arr))