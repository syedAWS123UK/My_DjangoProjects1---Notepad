from django.apps import AppConfig



# or from notepad import something



class NotepadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notepad_app'
