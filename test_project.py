import pytest
import os
from project import load_transactions, view_balance, view_spending_by_category

@pytest.fixture
def sample_transactions():
    return [
        {"date": "2023-01-01", "amount": 1000.00, "category": "Salary", "description": "Monthly pay"},
        {"date": "2023-01-02", "amount": -50.00, "category": "Food", "description": "Groceries"},
        {"date": "2023-01-03", "amount": -20.00, "category": "Transport", "description": "Bus fare"},
        {"date": "2023-01-04", "amount": -30.00, "category": "Food", "description": "Restaurant"}
    ]

def test_load_transactions(tmp_path):
    """Test loading transactions from a file"""
    test_file = tmp_path / "test_transactions.csv"
    test_file.write_text(
        "date,amount,category,description\n"
        "2023-01-01,1000.00,Salary,Monthly pay\n"
        "2023-01-02,-50.00,Food,Groceries\n"
    )

    transactions = load_transactions(test_file)
    assert len(transactions) == 2
    assert transactions[0]["category"] == "Salary"
    assert transactions[1]["amount"] == -50.00

def test_view_balance(sample_transactions):
    """Test balance calculation"""
    income, expenses, balance = view_balance(sample_transactions)
    assert income == 1000.00
    assert expenses == -100.00
    assert balance == 900.00

def test_view_spending_by_category(sample_transactions):
    """Test spending by category calculation"""
    spending = view_spending_by_category(sample_transactions)
    assert spending["Food"] == 80.00
    assert spending["Transport"] == 20.00
    assert "Salary" not in spending  # Should only include expenses
