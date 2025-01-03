from func import *

def read_hex_file(file_path):
    # Open the file in binary read mode
    with open(file_path, 'rb') as file:
        hex_data = file.read()
    return hex_data

def write_hex_file(file_path, hex_data):
    # Open the file in binary write mode
    with open(file_path, 'wb') as file:
        file.write(hex_data)

def updateCARbalance(carfile, newbalance):
        # Convert the number to hexadecimal and remove the '0x' prefix
        hex_value_no_prefix = hex(newbalance)[2:]
        
        # Ensure the hexadecimal string is 8-length
        hex_value_no_prefix = hex_value_no_prefix.zfill(8)

        # Reverse the hexadecimal string by pairs of 2 characters
        reversed_hex_value = reverse_hex_pairs(hex_value_no_prefix)
        
        # Convert the hexadecimal string to bytes
        new_hex_value = bytes.fromhex(reversed_hex_value)

        ba_ofst = 0xD5DC    # New bank balance (current amount of money)
        # Read the original hex file
        original_hex_data = read_hex_file(carfile)
    
        # Update the hex data
        updated_hex_data = update_hex_data(original_hex_data, ba_ofst, new_hex_value)
    
        # Write the updated hex data back to the file
        write_hex_file(carfile, updated_hex_data)