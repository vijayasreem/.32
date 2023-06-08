from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserManager(models.Manager):
    def create_user(self, username, password):
        user = self.model(
            username=username,
            password=make_password(password)
        )
        user.save(using=self._db)
        return user

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save(update_fields=["password"])

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        return check_password(raw_password, self.password)