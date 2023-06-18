from django.urls import path
from myapp.views import post, latest_post, tagsandcates, postlist_all

urlpatterns = [
        path('post/', post.index, name="post_index"),
        path('latestpost/', latest_post.index, name="latest_post_index"),
        path('tagsandcates/', tagsandcates.index, name="tagsandcates_index"),
        path('postlistall/', postlist_all.index, name="postlist_all_idnex"),
]

