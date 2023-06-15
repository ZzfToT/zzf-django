from django.http import JsonResponse
import json
from myapp.models.post import Post
import os

path = "/home/zzf/markdown"

def index(request):
    try:
        query_post_title = request.GET.get('title')
        print("query_content", query_post_title)
        post = Post.objects.get(title=query_post_title)
        if post:
            #with open (os.path.join(path, post.mdfile), mode="r", encoding="utf-8") as rf:
            content = post.mdfile
            obj = {
                    "status_code": 200,
                    "title" : post.title,
                    "year": post.create_date,
                    "categories":post.categories,
                    "tags":post.tags,
                    "content":content,
                    }
            return JsonResponse(obj)
        else:
            return JsonResponse({
                "status_code": 404,
                })

    except Exception as e:
        print(e)
        return JsonResponse({
            "status_code": 500,
            })