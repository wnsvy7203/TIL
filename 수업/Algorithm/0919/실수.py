import struct
a = 9.187500
bits, = struct.unpack('I', struct.pack('f', a))

print(f'{bits:032b}')
