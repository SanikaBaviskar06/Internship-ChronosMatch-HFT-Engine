# ChronosMatch: High-Frequency Trading Engine

## Project Overview

ChronosMatch is a Python-based high-frequency trading simulation developed as part of the Infotact Solutions Python Development Internship.

It demonstrates market order processing and matching using Python data structures.

## Features

- Circular buffer using `mmap` and `struct`
- Asynchronous market simulation using `asyncio`
- BUY and SELL order processing
- Price-time priority order matching
- Partial order quantity handling
- Input validation and trade history
- Automated testing using `pytest`
- Performance benchmarking
- Order management using `heapq`

## Technologies Used

- Python 3.13
- asyncio
- mmap
- struct
- heapq
- pytest
- Git and GitHub

## Project Structure

## Project Structure

```text
src/
├── ring_buffer.py
├── market_simulator.py
├── matching_engine.py
├── test_ring_buffer.py
├── test_matching_engine.py
└── benchmark.py
```

## How to Run

Run these commands from the project root directory:

```bash
python -m pytest src/ -v
python src/benchmark.py
```

## Testing

## Testing

The project includes automated tests for the ring buffer and matching engine.

Latest test run: **13 tests passed** using `pytest`.

Run the tests with:

```bash
python -m pytest src/ -v
```

## Performance Optimization

The matching engine uses `heapq` for efficient order management. The benchmark measures order insertion performance for different order counts.

## Learning Outcomes

- Python programming and data structures
- Order matching logic
- Testing and debugging
- Performance benchmarking
- Git and GitHub version control

## Disclaimer

This is an educational trading simulation. It does not connect to a real stock exchange or execute real financial trades.

## Benchmark Results

## Benchmark Results

The order insertion benchmark was executed using Python 3.13.14.

| Orders | Total Time (ms) | Average Add Latency (µs) |
|---:|---:|---:|
| 1,000 | 0.560 | 0.560 |
| 5,000 | 2.726 | 0.545 |
| 10,000 | 6.115 | 0.611 |

These results represent a single benchmark run on the development machine. Actual performance may vary depending on hardware and system conditions. The benchmark measures order insertion latency, not the performance of the entire trading engine.