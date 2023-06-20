from django.http import JsonResponse, HttpResponse
from myapp.models.post import Post

def index(request):
    try:
        tags = set()
        categoryDict = {}
        for post in Post.objects.all():
            if post.category not in categoryDict:
                categoryDict[post.category] = 1
            else:
                categoryDict[post.category] += 1
            for tag in post.tags:
                tags.add(tag)
        tags = list(tags)

        return JsonResponse({
            "status_code": 200,
            "tags": tags,
            "categoryDict": categoryDict
            })

    except Exception:
        return HttpResponse(status=500)
