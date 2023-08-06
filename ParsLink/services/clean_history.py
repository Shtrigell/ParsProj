from ParsLink.models import *

def clean_history():
    clean_elements = History.objects.all()
    clean_elements.delete()
    return print('succeed')
