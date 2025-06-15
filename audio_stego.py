import wave

def encode_audio(audio_path, message, output_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    message += '###END###'
    bits = ''.join([format(ord(i), '08b') for i in message])

    for i in range(len(bits)):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(bits[i])

    modified_audio = wave.open(output_path, 'wb')
    modified_audio.setparams(audio.getparams())
    modified_audio.writeframes(bytes(frame_bytes))
    audio.close()
    modified_audio.close()
    print(f"[+] Message encoded into {output_path}")

def decode_audio(audio_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    bits = [str(byte & 1) for byte in frame_bytes]
    chars = [chr(int(''.join(bits[i:i+8]), 2)) for i in range(0, len(bits), 8)]
    decoded_msg = ''.join(chars)
    return decoded_msg.split('###END###')[0]