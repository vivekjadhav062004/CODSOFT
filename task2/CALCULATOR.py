import sys

def get_user_value(message):
    """Handles inputs gracefully, allowing for a quick exit."""
    while True:
        entry = input(f"💬 {message}").strip().lower()
        
        if entry in ['exit', 'quit', 'bye']:
            print("👋 See you next time!")
            sys.exit()
            
        try:
            return float(entry)
        except ValueError:
            print("🤔 That doesn't look like a number. Let's try that again.")

def run_assistant():
    print(" Welcome back! I'm ready to help you with some math.")
    
    # We use a dictionary to map words/symbols to actual functions
    # This is much cleaner than a long list of if/elif statements
    operations = {
        'add': lambda a, b: a + b,
        'subtract': lambda a, b: a - b,
        'multiply': lambda a, b: a * b,
        'divide': lambda a, b: a / b if b != 0 else "Error: Division by zero"
    }

    aliases = {
        '+': 'add', 'plus': 'add', 'sum': 'add',
        '-': 'subtract', 'minus': 'subtract', 'sub': 'subtract',
        '*': 'multiply', 'x': 'multiply', 'times': 'multiply',
        '/': 'divide', 'div': 'divide', 'share': 'divide'
    }

    while True:
        val1 = get_user_value("First number: ")
        
        print("\nWhat should we do? (+, -, *, /)")
        choice = input("Action: ").strip().lower()
        
        # Resolve the alias (e.g., '+' becomes 'add')
        action = aliases.get(choice, choice)
        
        if action not in operations:
            print(f"⚠️ I'm not sure how to '{choice}' yet. Let's start over.")
            continue

        val2 = get_user_value("Second number: ")
        
        print("—" * 20)
        result = operations[action](val1, val2)
        
        if isinstance(result, str):
            print(f"❌ {result}")
        else:
            # Formatting the result to look clean
            print(f"✅ Result: {val1} {choice} {val2} = {result:g}")
        print("—" * 20)

if __name__ == "__main__":
    try:
        run_assistant()
    except KeyboardInterrupt:
        print("\n\nForced exit. Goodbye!")
