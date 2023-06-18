from django.http import JsonResponse
import json
from myapp.models.post import Post


def index(request):
    try:
        postlist = Post.objects.all().order_by("-create_date")
        postlist = [ {"title": item.title, "time": item.create_date} for item in postlist]
        return JsonResponse({
            "status_code": 200,
            "postlist": postlist
        })

    except Exception:
        return JsonResponse({
            "status_code": 500
        })
