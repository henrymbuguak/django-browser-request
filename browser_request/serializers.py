from .models import UserBrowserData
from rest_framework import serializers


class UserRequestDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserBrowserData
        fields = ['ip_address', 'user_browser', 'user_content_type', 'user_query_string']

