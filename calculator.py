def calculate(expression):
    """Evaluates a mathematical expression in string format."""
    try:
        #
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

while True:
    print("\nAdvanced Calculator")
    print("Enter a mathematical expression (or type 'exit' to quit):")
    user_input = input("Expression: ")
    
    if user_input.lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break
    
    result = calculate(user_input)
    print("Result:", result)
    