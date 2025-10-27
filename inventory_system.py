import json
from datetime import datetime

# Global variable for stock data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    if logs is None:
        logs = []

    # Input validation
    if not item:
        print("Error: Item name cannot be empty")
        return False
    
    if not isinstance(item, str):
        print(f"Error: Item name must be a string, got {type(item).__name__}")
        return False
        
    if not isinstance(qty, int):
        print(f"Error: Quantity must be an integer, got {type(qty).__name__}")
        return False

    try:
        stock_data[item] = stock_data.get(item, 0) + qty
        log_message = f"{str(datetime.now())}: Added {qty} of {item}"
        logs.append(log_message)
        return True
    except Exception as error:
        print(f"Error adding item: {error}")
        return False


def remove_item(item, qty):
    if not isinstance(item, str):
        print(f"Error: Item name must be a string, got {type(item).__name__}")
        return False
        
    if not isinstance(qty, int):
        print(f"Error: Quantity must be an integer, got {type(qty).__name__}")
        return False

    try:
        if item not in stock_data:
            print(f"Error: Item '{item}' not found in inventory")
            return False
            
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        return True
    except KeyError:
        print(f"Error: Item '{item}' not found in inventory")
        return False
    except ValueError as error:
        print(f"Error removing item: {error}")
        return False


def get_qty(item):
    if not isinstance(item, str):
        print(f"Error: Item name must be a string, got {type(item).__name__}")
        return 0
        
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r", encoding='utf-8') as file_handle:
            stock_data = json.loads(file_handle.read())
        return True
    except FileNotFoundError:
        print(f"File {file} not found. Starting with empty inventory.")
        return False
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file}")
        return False
    except Exception as error:
        print(f"Error loading data: {error}")
        return False


def save_data(file="inventory.json"):
    try:
        with open(file, "w", encoding='utf-8') as file_handle:
            file_handle.write(json.dumps(stock_data))
        return True
    except IOError as error:
        print(f"Error saving to {file}: {error}")
        return False
    except Exception as error:
        print(f"Error saving data: {error}")
        return False


def print_data():
    print("Items Report")
    print("-" * 20)
    if not stock_data:
        print("No items in inventory")
        return
        
    for item_name, quantity in stock_data.items():
        print(f"{item_name} -> {quantity}")


def check_low_items(threshold=5):
    result = []
    for item_name, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item_name)
    return result


def main():
    operation_logs = []
    
    print("Testing valid operations:")
    add_item("apple", 10, operation_logs)
    add_item("banana", 5, operation_logs)
    add_item("orange", 3, operation_logs)
    
    print("\nTesting invalid operations:")
    add_item(123, "ten")  
    add_item("", 5) 
    add_item("test", "invalid") 
    
    remove_item("apple", 3)
    remove_item("nonexistent", 1)  
    
    print(f"\nApple stock: {get_qty('apple')}")
    print(f"Banana stock: {get_qty('banana')}")
    print(f"Low items: {check_low_items()}")
    
    if save_data():
        print("Data saved successfully")
    
    if load_data():
        print("Data loaded successfully")
    
    print_data()
    
    print("\nOperation Logs:")
    for log_entry in operation_logs:
        print(log_entry)
    
    print('eval removed - using direct print')  


if __name__ == "__main__":
    main()