
import asyncio
import random
import time


async def generate_orders(total_orders=1000):
    start_time = time.perf_counter()

    for order_id in range(1, total_orders + 1):
        price = round(random.uniform(90, 110), 2)
        quantity = random.randint(1, 100)

        order = {
            "order_id": order_id,
            "price": price,
            "quantity": quantity,
        }

        if order_id <= 5:
            print(order)

        await asyncio.sleep(0)

    elapsed = time.perf_counter() - start_time

    print("Total orders:", total_orders)
    print("Elapsed seconds:", round(elapsed, 4))

    if elapsed > 0:
        print("Orders per second:", int(total_orders / elapsed))


async def main():
    await generate_orders(1000)


if __name__ == "__main__":
    asyncio.run(main())
