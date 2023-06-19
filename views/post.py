from django.http import JsonResponse
import json
from myapp.models.post import Post
import os
from django.core.exceptions import ObjectDoesNotExist

path = "/home/zzf/markdown"

def index(request):
    try:
        query_post_title = request.GET.get('title')
        post = Post.objects.get(title=query_post_title)
        with open (os.path.join(path, post.mdfile), mode="r", encoding="utf-8") as rf:
            content = rf.read()
        obj = {
                "status_code": 200,
                "title" : post.title,
                "date": post.create_date,
                "category":post.category,
                "tags":post.tags,
                "content":content,
                }
        return JsonResponse(obj)

    except ObjectDoesNotExist:
        return JsonResponse({
            "status_code": 404,
            })
    except Exception as e:
        return JsonResponse({
            "status_code": 500,
            })
