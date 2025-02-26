"""
Реалізувати функцію nested_parentheses(incoming). Функція отримує рядок, який складається тільки зі знаків "(" або ")"
Рядок вважається таким, що містить коректно вкладені скобки, якщо для кожної скобки "(" існує відповідна ")".
Функція повертає булевську змінну, яка показує, чи містить вхідний рядок тільки правильно вкладені скобки - True,
чи ні - False. Приклад результату виконання функції відповідно до різних варіантів вхідних рядків:
    incoming = "((())(())())" => True
    incoming = "" => True
    incoming = "(((())))" => True
    incoming = "())" => False
    incoming = "(()()(())" => False
"""

def nested_parentheses(incoming):
    for i in incoming:
        if i != "(" and i != ")":
            print("Only '(' and ')' symbols should be in your string!")
            break
    else:
        print(incoming.count("(") == incoming.count(")"))

if __name__ == "__main__":
    usr_str = input("Write your string here: ")
    nested_parentheses(usr_str)