import re

print("🤖 AI Calculator Ready! Type 'exit' to stop.")

def normalize(text):
    text = text.lower()
    text = text.replace("plus", "+")
    text = text.replace("add", "+")
    text = text.replace("minus", "-")
    text = text.replace("subtract", "-")
    text = text.replace("multiplied by", "*")
    text = text.replace("multiply", "*")
    text = text.replace("times", "*")
    text = text.replace("into", "*")
    text = text.replace("divided by", "/")
    text = text.replace("divide", "/")
    return text

def extract_expression(text):
    # Normalize common math expressions
    text = normalize(text)

    # Pattern 1: 2 * 3
    match = re.search(r'(-?\d+\.?\d*)\s*([+\-*/])\s*(-?\d+\.?\d*)', text)
    if match:
        return match.groups()

    # Pattern 2: + 2 and 3
    match = re.search(r'([+\-*/])\s*(-?\d+\.?\d*)\s*(and|with)?\s*(-?\d+\.?\d*)', text)
    if match:
        op, num1, _, num2 = match.groups()
        return num1, op, num2

    return None

def calculate(expression):
    result = extract_expression(expression)
    if not result:
        return "❌ Sorry, I couldn't understand that."

    num1, op, num2 = result
    try:
        num1 = float(num1)
        num2 = float(num2)

        if op == '+':
            return f"✅ Answer: {num1 + num2}"
        elif op == '-':
            return f"✅ Answer: {num1 - num2}"
        elif op == '*':
            return f"✅ Answer: {num1 * num2}"
        elif op == '/':
            return f"✅ Answer: {num1 / num2 if num2 != 0 else '❌ Cannot divide by zero'}"
    except Exception as e:
        return f"❌ Error: {e}"

# Input Loop
while True:
    user_input = input("\n🧾 Your question: ")
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Exiting. Goodbye!")
        break
    print(calculate(user_input))
