from django.urls import path
from myapp.views import post

urlpatterns = [
        path('post/', post.index, name="post_index"),
]

