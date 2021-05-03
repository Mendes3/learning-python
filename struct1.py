# used during networking by networking devices
# to convert any integer or float to bytes
from struct import *

packed_data = pack('iif', 6, 8, 3.7)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# to unpack the bytes to actual data
original_data = unpack('iif',b'\x06\x00\x00\x00\x08\x00\x00\x00\xcd\xccl@')
print(original_data)
original_data = unpack('iif',packed_data)
print(original_data)

