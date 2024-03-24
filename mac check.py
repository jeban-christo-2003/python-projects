import uuid

def get_mac_address():
    mac_address = uuid.getnode()
    mac_address = ':'.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

    return mac_address

def main():
    mac_address = get_mac_address()
    print("MAC Address of this PC:", mac_address)

if __name__ == "__main__":
    main()
