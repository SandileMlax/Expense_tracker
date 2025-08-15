import datetime  # For getting today's date
import matplotlib.pyplot as plt  # For optional visualization

# Global dictionary to store expenses (category -> total amount)
expenses = {}

# Function to add an expense
def add_expense():
    """Ask the user for expense amount and category, then store it."""
    while True:
        amount = input("Enter expense amount (or 'done' to finish): ")

        # Exit loop if user types 'done'
        if amount.lower() == 'done':
            break

        # Validate if amount is a number
        try:
            amount = float(amount)  # Convert to decimal number
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        # Ask for expense category
        category = input("Enter category (e.g., food, transport, bills): ").lower()

        # Add to dictionary
        if category in expenses:
            expenses[category] += amount  # Add to existing total
        else:
            expenses[category] = amount  # Create new category

        print(f"Expense of R{amount} for '{category}' added successfully!\n")

# Function to show summary of expenses
def show_summary(budget):
    """Display the total expenses and compare with budget."""
    total_spent = sum(expenses.values())  # Add up all expenses
    print("\n------ EXPENSE SUMMARY ------")
    for category, amount in expenses.items():
        print(f"{category.capitalize()}: R{amount:.2f}")

    print(f"Total Spent: R{total_spent:.2f}")

    # Compare with budget
    if total_spent > budget:
        print(f"You are OVER budget by R{total_spent - budget:.2f}")
    else:
        print(f"You are UNDER budget by R{budget - total_spent:.2f}!!!")

# Optional: Create a bar chart visualization
def create_chart():
    """Generate a bar chart of expenses."""
    if not expenses:
        print("No expenses to display in chart.")
        return

    categories = list(expenses.keys())
    amounts = list(expenses.values())

    plt.bar(categories, amounts, color=['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightseagreen'])
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (R)")
    plt.show()

# Main Program
print("Welcome to the Personal Expense Tracker!")
name = input("Enter your name: ")
budget = float(input("Enter your daily budget: "))
date_today = datetime.date.today()

print(f"\nHello {name}! Today is {date_today}. Let's track your expenses.\n")

# Add expenses
add_expense()

# Show summary
show_summary(budget)

# Ask if user wants to see a chart
see_chart = input("\nDo you want to see a chart of your expenses? (yes/no): ").lower()
if see_chart == 'yes':
    create_chart()

print("\nThank you for using the Expense Tracker! Goodbye!")
