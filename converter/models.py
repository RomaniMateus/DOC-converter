from django.db import models

from django_project.settings import BASE_DIR


class Document(models.Model):
    doc_path = models.FilePathField(path=f"{BASE_DIR}/media")
