
import mmap
import struct

ORDER_FORMAT = "i d i"
ORDER_SIZE = struct.calcsize(ORDER_FORMAT)


def create_buffer(size=1024):
    buffer = mmap.mmap(-1, size)
    return buffer


def write_order(buffer, order_id, price, quantity):
    data = struct.pack(ORDER_FORMAT, order_id, price, quantity)
    buffer.seek(0)
    buffer.write(data)


def read_order(buffer):
    buffer.seek(0)
    data = buffer.read(ORDER_SIZE)
    return struct.unpack(ORDER_FORMAT, data)


def main():
    buffer = create_buffer()
    write_order(buffer, 1, 100.5, 10)

    order = read_order(buffer)
    print("Order ID:", order[0])
    print("Price:", order[1])
    print("Quantity:", order[2])

    buffer.close()


if __name__ == "__main__":
    main()
