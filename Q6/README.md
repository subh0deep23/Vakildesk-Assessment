# Find Duplicate in Array Using O(1) Extra Space

This project demonstrates how to find a duplicate number in an array containing n+1 integers where each integer is between 1 and n. The algorithm uses **O(1) extra space** and **O(n) time complexity** by applying the Floyd's Tortoise and Hare (Cycle Detection) method.

## Project Overview

The `findDuplicate` function detects the duplicate number by interpreting the array as a linked list and finding the cycle that corresponds to the duplicate value.

## Algorithm

1. **Phase 1: Cycle Detection** – Use two pointers (`slow` and `fast`). `slow` moves by one step, and `fast` moves by two steps. If they meet, a cycle is detected.
2. **Phase 2: Finding the Cycle Start (Duplicate)** – Reset `slow` to the start of the list, and move both pointers one step at a time until they meet again. The meeting point is the duplicate number.

## Installation

1. **Clone the repository or download the files**.
   
   It’s recommended to use a virtual environment, even though no external dependencies are required.

2. **Set up a virtual environment** (optional):
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
Run the script:

bash

    python find_duplicate.py

Example

Given an array: [1, 3, 4, 2, 2], the function will return the duplicate number 2.
Input

python

nums = [1, 3, 4, 2, 2]

Output

bash

2

How It Works

    The array can be treated as a linked list where each element points to the index of the next element.
    The duplicate element creates a cycle in this linked list.
    The Tortoise and Hare algorithm (also used for detecting cycles in linked lists) is applied to find the cycle, which corresponds to the duplicate element.

Requirements

    Python 3.x
    No additional libraries or packages are required.

Migrations

No database migrations are required for this project.
Notes

    This approach guarantees that we solve the problem in O(1) extra space without modifying the input array.
 ```

**Run the script**:
    ```bash
    python find_duplicate.py
    ```

### Key Components:

- **Script**: Implements the algorithm for detecting the duplicate number in an array using O(1) extra space.
- **Requirements.txt**: Empty, as no additional libraries are needed.
- **README.md**: Contains the description, installation steps, example usage, and explanation of the algorithm.

By following the steps in the `README.md`, you can set up the environment and run the project successfully.
