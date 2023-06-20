from django.http import JsonResponse, HttpResponse
from myapp.models.post import Post
from django.core.exceptions import ObjectDoesNotExist

path = "/home/zzf/markdown"

def index(request):
    try:
        query_post_title = request.GET.get('title')
        post = Post.objects.get(title=query_post_title)
        obj = {
                "status_code": 200,
                "title" : post.title,
                "date": post.create_date,
                "category":post.category,
                "tags":post.tags,
                "content":post.content
                }
        return JsonResponse(obj)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)
