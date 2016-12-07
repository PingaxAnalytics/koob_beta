# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):

    # Primary Store connection details
    temporaryCredentialsRequestUrl = models.CharField(max_length=254,null=True)
    adminAuthorizationUrl = models.CharField(max_length=254,null=True)
    accessTokenRequestUrl = models.CharField(max_length=254,null=True)
    apiUrl = models.CharField(max_length=254,null=True)
    consumerKey = models.CharField(max_length=254,null=True)
    consumerSecret = models.CharField(max_length=254,null=True)

    # Store details
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    registered_at = models.IntegerField(null=True)
    webstore_url = models.CharField(max_length=254,null=True)
    webstore_platform = models.CharField(max_length=254,null=True)

class Stores(models.Model):
    name = models.CharField(max_length=100)
