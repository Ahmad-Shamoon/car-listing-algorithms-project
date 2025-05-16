# 🚗 Car Listing Management System

This is a **command-line Python project** built for the **Advanced Algorithms** course. It simulates a simple car listing system that allows users to add, delete, update, sort, and filter car records based on different attributes.

## 📌 Features

- View all car listings
- Add a new car
- Delete a car by index
- Update a car's information
- Sort listings by:
  - Price
  - Year
- Filter listings by:
  - Brand
  - Type (e.g., sedan, SUV, etc.)

## 📊 Dataset

Initially pre-filled with 5 car records containing the following attributes:

- `id` (int)
- `brand` (str)
- `model` (str)
- `price` (float)
- `year` (int)
- `type` (str)

## 🧠 Algorithms & Data Structures

- **Data Structure Used**: List of dictionaries (to store car records efficiently)
- **Sorting Algorithm**: Custom implementation using Python’s built-in `sorted()` with lambda (efficient and readable)
- **Filtering**: Performed using list comprehensions for clean and fast filtering by specific attributes

## 🛠️ Technologies

- **Language**: Python 3.x
- **Libraries**: Only built-in libraries (`sys`, `os`), no external dependencies

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmad-Shamoon/car-listing-algorithms-project.git
   cd car-listing-algorithms-project
