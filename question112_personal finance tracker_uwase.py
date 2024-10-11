
undo_stack = []
transaction_queue = []
expenses = []
def add_transaction(amount, description):
    transaction_queue.append((amount, description))
    print(f"Expense added: {description} of amount ${amount}")

def process_transactions():
    while transaction_queue:
        transaction = transaction_queue.pop(0)
        expenses.append((transaction))
        undo_stack.append((transaction))

def undo_last_transaction():
    if undo_stack:
        transaction = undo_stack.pop()
        expenses.remove((transaction))
    else:
        print("No transactions to undo.")    

add_transaction(50000, "money")
add_transaction(70000, "transport")
add_transaction(80000,"dressing")
add_transaction(300000,"leisure")
process_transactions()
print(expenses)  
undo_last_transaction()
print(expenses)  