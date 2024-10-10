from collections import deque

class PersonalFinanceTracker:
    def __init__(self):
        self.transaction_stack = []  
        self.transaction_queue = deque()  
        self.expense_history = []  

    def add_expense(self, amount, description):
        """Add a new expense and put it in the queue."""
        transaction = {"amount": amount, "description": description}
        self.transaction_queue.append(transaction)
        self.expense_history.append(transaction)
        print(f"Expense added: {description} of amount ${amount}")

    def process_transaction(self):
        """Process the next transaction in the queue."""
        if self.transaction_queue:
            transaction = self.transaction_queue.popleft()
            self.transaction_stack.append(transaction)  
            print(f"Processed transaction: {transaction['description']} of amount ${transaction['amount']}")
        else:
            print("No transactions to process.")

    def undo_last_transaction(self):
        """Undo the last processed transaction."""
        if self.transaction_stack:
            transaction = self.transaction_stack.pop()
            self.transaction_queue.appendleft(transaction)  
            print(f"Undo transaction: {transaction['description']} of amount ${transaction['amount']}")
        else:
            print("No transactions to undo.")

    def view_expense_history(self):
        """View the history of all expenses."""
        print("Expense history:")
        for expense in self.expense_history:
            print(f"{expense['description']}: ${expense['amount']}")


if __name__ == "__main__":
    finance_tracker = PersonalFinanceTracker()

    
    finance_tracker.add_expense(50000, "clothes")
    finance_tracker.add_expense(20000, "Gas")
    finance_tracker.add_expense(30000,"food")
    finance_tracker.add_expense(7000,"transport")
    finance_tracker.process_transaction()  
    finance_tracker.process_transaction()  
    finance_tracker.undo_last_transaction()  
    
    finance_tracker.view_expense_history()
