from django.http import JsonResponse, HttpResponse
from myapp.models import Post

def index(request):
    try:
        query_tag = request.GET.get("tag")
        postlist = Post.objects.filter(tags__icontains=query_tag).values("title", "create_date").order_by("-create_date")
        post_time_dict = {}
        if len(postlist) == 0:
            return HttpResponse(status=404)

        for post in postlist:
            year = post["create_date"].year
            if year not in post_time_dict:
                post_time_dict[year] = [post]
            else:
                post_time_dict[year].append(post)


        return JsonResponse({
                "statsu_code":200,
                "postTimeDict": post_time_dict
            })

    except Exception as e:
        print(e)
        return HttpResponse(status=500)
