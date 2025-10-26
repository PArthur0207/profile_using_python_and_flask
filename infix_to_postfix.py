from linked_list import LinkedList

class InfixToPostfix:
    def __init__(self):
        self.operators = set("(+-*/^)")
        self.operator = set("+-*^/")
        self.values = {
            "^": 3,
            "*": 2,
            "/": 2,
            "+": 1,
            "-": 1,
            "(": 0,
            ")": 0
        }
    def get_infix(self, expression):    
        valid_characters= set("QWERTYUIOPASDFGHJKLZXCVBNM0123456789qwertyuiopasdfghjklzxcvbnm+-*^/() ")

        for_paranthesis = []

        for character in expression:
            if character not in valid_characters:
                return f"{character} is an invalid input, please change it"
            elif character == "(":
                for_paranthesis.append(character)
            elif character == ")":
                if for_paranthesis is None:
                    return "Invalid Input. Missing an opening parenthesis '('"
                for_paranthesis.pop()
            
        if for_paranthesis:
            return "Invalid Input. Missing a closing parenthesis ')'"
        
        previous = ""
        expression = expression.replace(" ", "")
        for character in expression:
            if character in self.operator:
                if previous in self.operator or previous == "" or previous == "(":
                    return f"Invalid Input. Missed place operator '{character}'"
            elif character == "(":
                if previous not in ("", "(") and previous not in self.operator:
                    return "Invalid Input missing operator before '('"
            elif character == ")":
                if previous in self.operator or previous == "(" or previous == "":
                    return "Invalid Input. Misplaced )"
            else:
                if previous not in ("", "(", "+", "-", "/", "*", "^"):
                    return "Invalid Input. Operands cannot be next to each other"
            previous = character
        
        if previous in self.operator:
            return "Invalid Input. Cannot end in an operation"
            
        return expression
    
    def convert(self, expression):
        ll = LinkedList()
        checker = expression
        original_expression = self.get_infix(checker)
        output = ""
        
        if "invalid" in original_expression or "Invalid" in original_expression:
            return original_expression
        
        expression = original_expression.replace(" ", "")

        for item in expression:
            if item in self.operators:
                if item == "(":
                    ll.insert_at_beginning(item)
                elif item == ")":
                    while ll.head.data and ll.head.data != "(":
                        output += ll.remove_at_beginning()
                    if ll.head.data and ll.head.data == "(":
                        ll.remove_at_beginning()
                    print("Hi")
                else:
                    while ll.head and self.values[ll.head.data] >= self.values[item]:
                        output += ll.remove_at_beginning()
                    ll.insert_at_beginning(item)
            else:
                output += item

        while ll.head:
            output += ll.remove_at_beginning()

        return output