from django.http import HttpResponse
from .models import UserBrowserData
import datetime

from rest_framework import viewsets
from .serializers import UserRequestDataSerializer


def get_client_request_data(request):
    """
    Get the User Request
    """
    ip_address = request.META.get('REMOTE_ADDR')
    user_browser = request.headers['User-Agent']
    user_query_string = request.META.get('QUERY_STRING')
    user_content_type = request.headers['CONTENT_TYPE']

    user_data = UserBrowserData.objects.create(
        ip_address=request.META.get('REMOTE_ADDR'),
        user_browser=request.headers['User-Agent'],
        user_content_type=request.headers['CONTENT_TYPE'],
        user_query_string=request.META.get('QUERY_STRING'),
    )
    user_data.save()

    now = datetime.datetime.now()
    html = "<html><body>Hello and welcome to M-power test. It is now %s.</body></html>" % now
    return HttpResponse(html)


class VisitorViewSet(viewsets.ModelViewSet):
    """
    An endpoint that allows user request data to view or edited
    """
    queryset = UserBrowserData.objects.all().order_by('-created_at')
    serializer_class = UserRequestDataSerializer


