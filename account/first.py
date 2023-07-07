dec_num = 123456
bin_str = bin(dec_num)[2:] # [2:] to remove the "0b" prefix
hex_str = hex(int(bin_str, 2))[2:] # [2:] to remove the "0x" prefix
print(hex_str)
