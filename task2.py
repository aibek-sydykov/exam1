## Задание 2
# Вам дана функция:
# def divide(a, b):
# 	return a/b
# Напишите декоративную функцию, которая будет обрамлять функцию divide 
# и будет проверять являются ли оба аргумента числами. 
# И не является ли аргумент **b** нулём

# type(a) == int and type(b)==int
# b != 0


def decorator(function_to_decorate):
    def wrapper(arg1, arg2):
        if arg2 == 0:
            return 'На ноль делить нельзя!'
        elif type(arg1) == int and type(arg2) == int:
            return f'Ваш результат: {function_to_decorate(arg1, arg2)}'
        else:
            return 'Присутствует ошибка. Проверьте ваши значенияю'
    return wrapper

@decorator
def divide(a, b):
	return a/b

print(divide(1, 10))
