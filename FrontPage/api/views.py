from  rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import User_Activity
from .Serializer import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = User_Activity.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = User_Activity.objects.all()
    serializer_class = PostSerializer
