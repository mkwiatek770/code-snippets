import struct


if __name__ == '__main__':
    values = (42, 99.99, b'string')
    packed = struct.pack('if6s', *values)
    print(packed)

    # unpack
    print(struct.unpack('if6s', packed))
