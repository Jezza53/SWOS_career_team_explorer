from func import *

def updateCARfile(carfile, offset, hex_value):
    # Convert the hexadecimal string to bytes
    new_hex_value = bytes.fromhex(hex_value)

    # Read the original hex file
    original_hex_data = read_hex_file(carfile)
    
    # Update the hex data
    updated_hex_data = update_hex_data(original_hex_data, offset, new_hex_value)
    
    # Write the updated hex data back to the file
    write_hex_file(carfile, updated_hex_data)

def updateCARbalance(carfile, newbalance):
    # Bank Balance Offset
    ba_ofst = 0xD5DC    

    # Convert the number to hexadecimal and remove the '0x' prefix
    hex_value_no_prefix = hex(newbalance)[2:]
    
    # Ensure the hexadecimal string is 8-length
    hex_value_no_prefix = hex_value_no_prefix.zfill(8)

    # Reverse the hexadecimal string by pairs of 2 characters (needed for correct balance conversion)
    reversed_hex_value = reverse_hex_pairs(hex_value_no_prefix)

    updateCARfile(carfile, ba_ofst, reversed_hex_value)