from typing import Any, Optional
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(
        self, 
        email: str,
        password: Optional[str], 
        **extra_fields: Any):
        
        if not email:
            raise ValueError("The email must be set")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name: str, email: str, password: Optional[str], **extra_fields: Any):

        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )

        user.is_customer = False
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user