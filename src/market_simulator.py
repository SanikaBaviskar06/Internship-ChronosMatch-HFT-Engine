
import asyncio
import random

from ring_buffer import RingBuffer


async def generate_orders(ring, total_orders=1000):
    for order_id in range(1, total_orders + 1):
        price = round(random.uniform(90, 110), 2)
        quantity = random.randint(1, 100)

        ring.write(order_id, price, quantity)

        await asyncio.sleep(0)

    print("Generated orders:", total_orders)

    orders = ring.read_all()
    print("Orders stored in buffer:", len(orders))

    for order in orders[:5]:
        print(order)


async def main():
    ring = RingBuffer(capacity=100)

    try:
        await generate_orders(ring, total_orders=1000)
    finally:
        ring.close()


if __name__ == "__main__":
    asyncio.run(main())
