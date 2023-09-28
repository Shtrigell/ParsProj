

menu = [{'title':"История", 'url_name': 'history'}
]  # Список меню в хэдэре

class DataMixin():

    def get_user_context(self, **kwargs):

        context = kwargs
        context['menu'] = menu
        return context