# Personal Finance Tracker

#### Video Demo: [URL to Your YouTube Demonstration]
#### CS50P Final Project

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A command-line application for tracking personal finances with powerful analytics, built for Harvard's CS50P course.

## Features

### Transaction Management
- Add income/expense transactions with custom categories
- View all transactions in a clean, sorted table
- Automatic date detection (defaults to current date)

### Financial Insights
- Real-time balance calculation (Income vs Expenses)
- Spending breakdown by category
- Basic financial analytics

### Data Handling
- Automatic CSV storage (`transactions.csv`)
- Data persistence between sessions
- Input validation for all fields

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/finance-tracker.git
cd finance-tracker
python project.py
 Usage
The program features an intuitive menu system:
Add Transaction:
Record new income or expenses
Categorize transactions (e.g., Food, Rent)
Add optional descriptions
View Transactions:
See all records in chronological order
Clean tabular display with formatting
View Balance:
Instant financial summary
Separates income and expenses
Shows net balance
Spending by Category:
Visualize expense distribution
Sorted by highest spending
Exit:

Automatically saves all data
Preserves transaction history

File Structure
.
├── project.py            # Main application logic
├── test_project.py       # Unit tests (pytest)
├── transactions.csv      # Auto-generated transaction data
├── requirements.txt      # Dependencies (pytest)
└── README.md             # Documentation
 Testing
The project includes comprehensive unit tests:

bash
pytest test_project.py -v

Tests cover:
Transaction loading/saving
Balance calculations
Category-based analytics
Edge cases (empty files, negative values)

Design Choices
CSV Storage:
Simple, human-readable format
No database required

Easy data portability

Functional Structure:

Modular functions for each feature

Clear separation of concerns

Easy to maintain/extend

User Experience:

Input validation prevents crashes

Clean terminal formatting

Intuitive menu navigation


