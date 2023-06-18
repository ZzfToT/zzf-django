from django.http import JsonResponse
import json
from myapp.models.post import Post

def index(request):
    try:
        tagCollection = Post.objects.values("tags").distinct()
        categoryCollection = Post.objects.values("categories").distinct()

        return JsonResponse({
            status_code : 200,
            tags: tagCollection,
            categories: categoryCollection,
            })

    except Exception:
        return JsonResponse({
                status_code: 500
            })
