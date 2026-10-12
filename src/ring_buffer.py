
import mmap
import struct

CAPACITY = 10
ORDER_FORMAT = "i d i"
ORDER_SIZE = struct.calcsize(ORDER_FORMAT)


class RingBuffer:
    def __init__(self, capacity=CAPACITY):
        self.capacity = capacity
        self.buffer = mmap.mmap(
            -1, capacity * ORDER_SIZE
        )
        self.write_index = 0
        self.count = 0

    def write(self, order_id, price, quantity):
        position = self.write_index * ORDER_SIZE
        data = struct.pack(
            ORDER_FORMAT, order_id, price, quantity
        )

        self.buffer.seek(position)
        self.buffer.write(data)

        self.write_index = (
            self.write_index + 1
        ) % self.capacity

        self.count = min(self.count + 1, self.capacity)

    def read_all(self):
        orders = []
        start = (self.write_index - self.count) % self.capacity

        for i in range(self.count):
            index = (start + i) % self.capacity
            self.buffer.seek(index * ORDER_SIZE)
            data = self.buffer.read(ORDER_SIZE)
            orders.append(struct.unpack(ORDER_FORMAT, data))

        return orders

    def close(self):
        self.buffer.close()


def main():
    ring = RingBuffer(capacity=3)

    ring.write(1, 100.5, 10)
    ring.write(2, 101.0, 20)
    ring.write(3, 102.5, 15)
    ring.write(4, 103.0, 25)

    for order in ring.read_all():
        print(order)

    ring.close()


if __name__ == "__main__":
    main()
