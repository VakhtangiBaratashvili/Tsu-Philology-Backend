from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from jwt_auth.serializers import UserSerializer
from rest_framework import status
import jwt
from rest_framework.exceptions import AuthenticationFailed
from jwt_auth.models import User
from .models import Post
# Create your views here.

class AddPostView(APIView):
    
    def post(self, request):
        title = request.data['title']
        description = request.data['description']
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        post = Post(title=title, description=description, user=user)
        post_serializer = PostSerializer(post)
        post.save()
        return Response(post_serializer.data, status=status.HTTP_201_CREATED)
    
class GetAllPostsView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class GetAllPostsByUserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        posts = Post.objects.filter(user=payload['id'])
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)