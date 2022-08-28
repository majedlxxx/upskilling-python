from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from post.models import Post
from django.http import JsonResponse
from post.serializers import PostSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_posts(request):
    user = request.user
    my_posts = Post.objects.filter(author=user)

    # processed_posts = []
    # for post in my_posts:
    #     processed_posts.append({
    #         "author": post.author.username,
    #         "title": post.title,
    #         "content": post.content
    #     })
    
    # return JsonResponse({"posts": processed_posts})
    
    #We can use a Post Serializer with many=True argument to get the same results
    posts_serializer = PostSerializer(my_posts, many=True)
    return JsonResponse({"posts": posts_serializer.data})
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_post(request):
    post_serializer = PostSerializer(data=request.data)
    if not post_serializer.is_valid():
        return JsonResponse({
            "errors": post_serializer.errors
        },  status=400)
    title = post_serializer.validated_data['title']
    content = post_serializer.validated_data['content']
    new_post = Post(title=title, content=content, author=request.user)
    new_post.save()
    return JsonResponse({"message":"Created successfully"}, status=201)
    