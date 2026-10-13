
import time
from matching_engine import MatchingEngine


def benchmark():
    order_counts = [1000, 5000, 10000]

    for total_orders in order_counts:
        engine = MatchingEngine()

        start_time = time.perf_counter()

        for i in range(total_orders):
            engine.add_order(i, "BUY", 100, 1)

        end_time = time.perf_counter()

        total_time = end_time - start_time
        avg_latency = (total_time / total_orders) * 1_000_000

        print("\nOrders:", total_orders)
        print("Total Time:", round(total_time * 1000, 3), "ms")
        print("Average Add Latency:", round(avg_latency, 3), "microseconds")


if __name__ == "__main__":
    benchmark()
