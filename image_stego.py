from PIL import Image

def encode_image(input_image_path, message, output_image_path):
    img = Image.open(input_image_path)
    binary_msg = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'

    if img.mode != 'RGB':
        img = img.convert('RGB')

    pixels = list(img.getdata())
    encoded_pixels = []
    msg_index = 0

    for pixel in pixels:
        r, g, b = pixel
        if msg_index < len(binary_msg):
            r = (r & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            g = (g & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            b = (b & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        encoded_pixels.append((r, g, b))

    img.putdata(encoded_pixels)
    img.save(output_image_path)
    print(f"[+] Message encoded into {output_image_path}")

def decode_image(stego_image_path):
    img = Image.open(stego_image_path)
    binary_data = ''
    for pixel in list(img.getdata()):
        for color in pixel[:3]:
            binary_data += str(color & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for byte in all_bytes:
        if byte == '11111110':
            break
        message += chr(int(byte, 2))
    return message