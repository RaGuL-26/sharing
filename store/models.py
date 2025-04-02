from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, dob=None, user_type=None):
        if not email:
            raise ValueError('Enter a valid email')
        if not username:
            raise ValueError('Enter a correct username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            dob=dob,
            user_type=user_type
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, dob=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            dob=dob,
            user_type = User.BUYER
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    BUYER = 'buyer'
    SELLER = 'seller'
    USER_TYPES = [
        (BUYER, 'Buyer'),
        (SELLER, 'Seller'),
    ]

    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15)
    dob = models.DateField(null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default=BUYER)

    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
