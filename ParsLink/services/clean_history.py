from ParsLink.models import *

def clean_history():
    """
    Функция очитски истории

    Очищает модель History

    clean_elements - переменная, содержит все объекты истории.
    Возвращает сообщение в консоль о успешной очистки истории
    """
    clean_elements = History.objects.all()
    clean_elements.delete()
    return print('succeed')
