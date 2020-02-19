from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserBrowserData(BaseModel):
    ip_address = models.CharField(max_length=200)
    user_browser = models.CharField(max_length=200)
    user_content_type = models.CharField(max_length=200)
    user_query_string = models.CharField(max_length=200)


