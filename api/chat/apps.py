from django.apps import AppConfig


class ChatConfig(AppConfig):
    name = 'api.chat'

    def ready(self):
        import api.chat.signals  # noqa
