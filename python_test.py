with open("/dev/hidg0", "wb+") as keyboard:
    send_keys = [0] * 8
    write_buf = [0] * 8
    write_buf[2] = 0xb
    write_buf[3] = 0xc
    keyboard.write(bytearray(write_buf))
    keyboard.write(bytearray(send_keys))

