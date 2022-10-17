math_expression = ''


def init(user_expression):
    global math_expression
    # здесь проверка и обработка данных пользователя
    math_expression = user_expression


def evaluate(user_expression):
    init(user_expression)
    return eval(math_expression)
