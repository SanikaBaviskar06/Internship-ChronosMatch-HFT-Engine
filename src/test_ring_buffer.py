
from ring_buffer import RingBuffer


def test_ring_buffer():
    ring = RingBuffer(capacity=3)

    try:
        ring.write(1, 100.5, 10)
        ring.write(2, 101.0, 20)
        ring.write(3, 102.5, 15)
        ring.write(4, 103.0, 25)

        orders = ring.read_all()

        assert len(orders) == 3
        assert orders[0][0] == 2
        assert orders[-1][0] == 4

        print("Ring Buffer Test Passed!")

    finally:
        ring.close()


if __name__ == "__main__":
    test_ring_buffer()
