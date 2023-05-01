#Brug exceptions til at skrive en funktion, der tager en streng splitter den op og ved hjælp af execeptions undersøger om input består af præcis 3 elementer: Tal Operator Tal. Operator er de klassiske fire regnearter. Husk at du ikke må dele med 0.
#Udvid programmet, så du kan operere på flere tal.


def operate(input_string):
    try:
        elements = input_string.split()
        if len(elements) != 3:
            raise ValueError("Input should contain three elements: number operator number")
        
        num1 = float(elements[0])
        num2 = float(elements[2])
        operator = elements[1]
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator")
        
        return result
    
    except (ValueError, ZeroDivisionError) as e:
        print("Error:", e)
        return None
    
print(operate("5 + 3"))
print(operate("7 / 0"))
print(operate("2 ^ 3"))
print(operate("10 - 3"))