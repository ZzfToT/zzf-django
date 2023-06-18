from django.http import JsonResponse
import json
from myapp.models.post import Post


def index(request):
    try:
        postlist = Post.objects.values("title", "create_date").order_by("-create_date")[:6]
        postlist = list(postlist)
        return JsonResponse({
            "status_code": 200,
            "postlist": postlist
        })

    except Exception:
        return JsonResponse({
            "status_code": 500
        })
