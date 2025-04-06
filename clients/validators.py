import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _



@deconstructible
class StrongPasswordValidator(RegexValidator):
    regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>/?\[\]\\|`~]).{8,50}$"



@deconstructible
class AllowedEmailValidator:
    
    ALLOWED_EMAIL_DOMAINS = {
        "gmail.com", "mail.com", "yandex.ru", "mail.ru"
    }
    MAX_LENGTH = 100

    def __call__(self, value: str):
        if len(value) > self.MAX_LENGTH:
            raise ValidationError(
                _("Длина email не должна превышать %(max_length)d символов."),
                params={"max_length": self.MAX_LENGTH},
            )
        
        match = re.match(r"^[\w\.-]+@([\w\.-]+)$", value)
        if not match:
            raise ValidationError(_("Некорректный email."))

        domain = match.group(1).lower()
        if domain not in self.ALLOWED_EMAIL_DOMAINS:
            raise ValidationError(
                _("Данный домен %(domain)s не разрешен."),
                params={"domain": domain},
            )
        import re

@deconstructible
class UsernameValidator:
    def __call__(self, value: str):
        if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]{2,29}$", value):
            raise ValidationError(
                _("Имя пользователя должно быть от 3 до 30 символов и содержать только латинские буквы," 
                " цифры или подчёркивания. Первый символ — буква или подчёркивание.")
            )
