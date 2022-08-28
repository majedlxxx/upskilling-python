from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    author = serializers.CharField(required=False)
    
    
'''
Serializers are used to transform python objects into more universal data types eg: json
p = Post.objects.first()
s = PostSerializer(p)
s.data # will return the post's data as json
instead of passing the post "p" to the serializer we can send a queryset containing many posts and that will return an array of dictionaries each dictionary representing a post but you will have to set the many flag to True
s = PostSerializer(Post.objects.all(), many=True)
s.data # will return array of dictionaries.
'''