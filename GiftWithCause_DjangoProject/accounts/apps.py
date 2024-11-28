from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GiftWithCause_DjangoProject.accounts'

    def ready(self):
        import GiftWithCause_DjangoProject.accounts.signals
