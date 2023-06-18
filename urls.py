from django.urls import path
from myapp.views import post, latest_post, postlist

urlpatterns = [
        path('post/', post.index, name="post_index"),
        path('latestpost/', latest_post.index, name="latest_post_index"),
        path('tagsandcates/', postlist.index, name="postlist_index")
]

