import email
from mimetypes import init
from django.db import models
from pymongo import HASHED
import hashlib
# Create your models here.
class User:

    def __init__(self,User)
        self.User = 

    email = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)

    if password.length >= 8:
        HASHED