from PIL import Image as image


compressed_img = image.open("./out/frame0000.png")

bin_arr = []  # This will temporarily hold the binary strings for each byte.
fin_bytes = bytearray()  # Using a bytearray for efficient bytes collection.

for data in list(compressed_img.getdata()):
    if data == (155, 155, 155, 255):  # Marker for separation
        if bin_arr:  # Ensure bin_arr is not empty
            bits = ''.join(bin_arr)
            # Convert the binary string directly to a byte and add to fin_bytes
            fin_bytes.append(int(bits, 2))
            bin_arr = []  # Reset for the next byte
    elif data == (0, 0, 0, 255):
        bin_arr.append("0")
    elif data == (255, 255, 255, 255):
        bin_arr.append("1")

# Writing the decompressed binary data to a file
with open("output", "wb") as out:
    out.write(fin_bytes)
