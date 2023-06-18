from django.http import JsonResponse
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

        print(post_time_dict)

        return JsonResponse({
            "status_code": 200,
            "postTimeDict": post_time_dict
            })

    except Exception:
        return JsonResponse({
            "status_code": 500
            })

