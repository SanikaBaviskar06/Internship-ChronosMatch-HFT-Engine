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

The latest recorded test run passed all 9 tests.

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

The order insertion benchmark was executed on Python 3.13.14.

| Orders | Total Time (ms) | Average Add Latency (µs) |
|---:|---:|---:|
| 1,000 | 0.737 | 0.737 |
| 5,000 | 3.446 | 0.689 |
| 10,000 | 5.043 | 0.504 |

These results represent one benchmark run on the development machine. Actual performance may vary depending on hardware and system conditions.