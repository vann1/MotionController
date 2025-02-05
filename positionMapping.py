from pyModbusTCP.client import ModbusClient
from address_enum import READ_ADDRESSES
import atexit
import struct

def convert_16bit_twos_complement(binary_data):
    # Assuming 'binary_data' is a bytes object containing the 16-bit integer
    # '>h' means big-endian ('>') short ('h') which is 16 bits in 2's complement
    number = struct.unpack('>h', binary_data)[0]
    return number


def cleanup():
    print("cleanup func executed!")
    client_left.close()
    client_right.close()

SERVER_IP_LEFT = '192.168.0.211'  
SERVER_IP_RIGHT = '192.168.0.212'
SERVER_PORT = 502  
client_left = ModbusClient(SERVER_IP_LEFT, port=SERVER_PORT)
client_right = ModbusClient(SERVER_IP_RIGHT, port=SERVER_PORT)

def get_motor_pos(client):
    return client.read_holding_registers(READ_ADDRESSES.pfeedback.value, 2)

def main():
    atexit.register(cleanup)
    while(True):
        user_input = input("Press 'r' to read motor position values or 'x' to exit: ").lower()
        if (user_input == 'x'):
            break
        if (user_input == 'r'):
            motor1pos = get_motor_pos(client_left)
            motor2pos = get_motor_pos(client_right)

            ### return registers list or None if fail
            desimaaliluku = motor1pos[0] # desimaalit
            kokonaisluku = motor1pos[1] # kokonaisluku

            print("Motor 1 kokonaisluku: " + kokonaisluku)
            print("Motor 1 desimaaliluku: " + desimaaliluku)

            ## Pitää tutkia minkälaisessa datamuodossa tuo on että 
            ## miten se muuutetaan 2twos complementista normaaliin muoton

            print("Motor 1 position: " + motor1pos[1])
            print("Motor 2 position: " + motor2pos[1])


if __name__ == "__main__":
    main()