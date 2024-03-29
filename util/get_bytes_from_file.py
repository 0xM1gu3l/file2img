def getBytesFromFile():
    fp = input("Drag n' Drop the file here: ")
    
    with open(fp, 'rb') as f:
        content = f.read()

    # Convert each byte to its binary representation and join them with a space for clarity.
    binary_array = [format(byte, '08b') for byte in content]

    return binary_array