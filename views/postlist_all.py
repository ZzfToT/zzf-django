from django.http import JsonResponse, HttpResponse
import json
from myapp.models.post import Post

def index(request):
    try:
        postlist = Post.objects.values("title", "create_date").order_by("-create_date")
        post_time_dict = {}
        for post in postlist:
            year = post["create_date"].year
            if year not in post_time_dict:
                post_time_dict[year] = [post]
            else:
                post_time_dict[year].append(post)

        return JsonResponse({
            "status_code": 200,
            "postTimeDict": post_time_dict
            })

    except Exception:
        return HttpResponse(status=500)
