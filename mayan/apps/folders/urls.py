from django.conf.urls import url

from .views import FolderView

urlpatterns = [
    url(regex=r"^folder/$", name="folder_view", view=FolderView.as_view()),
]
