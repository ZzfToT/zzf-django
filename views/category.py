from django.http import JsonResponse
import json
from myapp.models import Post

def index(request):
    try:
        query_category = request.GET.get("category")
        postlist = Post.objects.filter(category__iexact=query_category).values("title", "create_date").order_by("-create_date")
        if len(postlist) == 0:
            return JsonResponse({
                "status_code": 404
                })
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
        return JsonResponse({
            "status_code": 200
            })

