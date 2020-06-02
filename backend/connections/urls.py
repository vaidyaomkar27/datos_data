from django.urls import path, include
from connections.views import DataSourceApiView

app_name = 'connections'

urlpatterns = [
    path(
        'data-source/',
        DataSourceApiView.as_view()
    )
]