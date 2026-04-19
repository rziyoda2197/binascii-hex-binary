import binascii

def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:]

def binary_to_hex(binary_string):
    return hex(int(binary_string, 2))[2:]

# Testlash
hex_string = "123456"
binary_string = "10110010"

print(f"Hex: {hex_string} -> Binary: {hex_to_binary(hex_string)}")
print(f"Binary: {binary_string} -> Hex: {binary_to_hex(binary_string)}")
