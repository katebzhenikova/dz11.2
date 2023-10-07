def to_uppercase(input_string):
    """
    PC принимает на вход строку и возвращает ее со всеми заглавными буквами
    """
    uppercase_string = input_string.upper()
    return uppercase_string


def title_words(input_string):
    """
    Делает заглавными первые буквы каждого слова
    в строке
    """
    words = input_string.title()
    return words

# print(title_words('мир во всем мире'))
