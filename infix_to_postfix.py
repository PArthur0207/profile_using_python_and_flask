from linked_list import LinkedList

def get_infix(expression):
    valid_characters= set("QWERTYUIOPASDFGHJKLZXCVBNM0123456789qwertyuiopasdfghjklzxcvbnm+-*^/() ")
    operators = set("+-*/^")

    for_paranthesis = []

    for character in expression:
        if character not in valid_characters:
            return f"{character} is an invalid input, please change it"
        elif character == "(":
            for_paranthesis.append(character)
        elif character == ")":
            if for_paranthesis is None:
                return "Missing an opening parenthesis '('"
            for_paranthesis.pop()
        
    if for_paranthesis:
        return "Missing a closing parenthesis ')'"
    
    previous = ""
    expression = expression.replace(" ", "")
    for character in expression:
        if character in operators:
            if previous in operators or previous == "" or previous == "(":
                return f"Invalid Input. Missed place operator '{character}'"
        elif character == "(":
            if previous not in ("", "(") and previous not in operators:
                return "Invalid Input missing operator before '('"
        elif character == ")":
            if previous in operators or previous == "(" or previous == "":
                return "Invalid Input. Misplaced )"
        else:
            if previous not in ("", "(") and previous not in operators:
                return "Invalid Input. Operands cannot be next to each other"
        previous = character
    
    if previous in operators:
        return "Invalid Input. Cannot end in an operation"
        
    return expression
    


ll = LinkedList()

operators_used = ["-", "+", "=", "/", "^", "*", "(", ")"]
values = {
"^": 3,
"*": 2,
"/": 2,
"+": 1,
"-": 1,
"(": 0,
")": 0
}

checker = input("Please input your expression here: \n")
original_expression = get_infix(checker)
output = ""

expression = original_expression.replace(" ", "")

for item in expression:
    if item in operators_used:
        if item == "(":
            ll.insert_at_beginning(item)
        elif item == ")":
            while ll.head.data != "(":
                output += ll.remove_at_beginning()
            ll.remove_at_beginning()
        else:
            if ll.head and values[ll.head.data] >= values[item]:
                output += ll.remove_at_beginning()
                ll.insert_at_beginning(item)
            elif ll.head and values[ll.head.data] < values[item]:
                ll.insert_at_beginning(item)
            elif ll.head is None:
                ll.insert_at_beginning(item) 

    else:
        output += item

while ll.head:
    output += ll.remove_at_beginning()

print(f"Infix: {original_expression} \nPostfix: {output}")