# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serialzer = SnippetSerializer(snippets,many=True)
#         return JsonResponse(serialzer.data,safe=False)
#     elif request.method =='POST':
#         data = JSONParser().parse(request)
#         serialzer = SnippetSerializer(data=data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return JsonResponse(serialzer.data,status= 201)
#         return JsonResponse(serialzer.errors, status = 400)
    
# @csrf_exempt
# def snippet_detail(request,pk):
#     """ Retrive, update or delete a code snippet
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status= 404)
    
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
    
#     elif request.method =='PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status = 400)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status = 204)

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

# @api_view(['GET','POST'])
# def snippet_list(request, format= None):
#     """
#     list all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets,many= True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk, format=None):
#     """ Retrive, update or delete a code snippet
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serialzer = SnippetSerializer(snippet)
#         return Response(serialzer.data)
#     elif request.method == 'PUT':
#         serialzer = SnippetSerializer(snippet, data= request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class SnippetList(APIView):
#     """list all snippets or create a new snippet"""
#     def get(self, request, format= None):
#         snippets = Snippet.objects.all()
#         serial = SnippetSerializer(snippets,many= True)
#         return Response(serial.data)
    
#     def post(self,request, format= None):
#         serial = SnippetSerializer(data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data,status=status.HTTP_201_CREATED)
#         return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class SnippetDetail(APIView):
#     """Retrive ,update or delete a snippet instance"""
#     def get_object(self,pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#     def get(self,request,pk,format= None):
#         snippet= self.get_object(pk)
#         return Response(snippet.data)

#     def put(self,request,pk,format= None):
#         snippet= self.get_object(pk)
#         serial = SnippetSerializer(snippet,data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk,format= None):
#         snippet= self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
#     def get(self,request, *args, **kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer, UserSerializer
# from rest_framework import generics
# from django.contrib.auth.models import User
# from rest_framework import permissions
# from snippets.permissions import IsOwnerOrReadOnly
# class SnippetList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
#     queryset= Snippet.objects.all()
#     serializer_class= SnippetSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset= User.objects.all()
#     serializer_class= UserSerializer

from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    this viewset automatically provides 'list' and 'retrive' actions.
    """
    queryset= User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    this viewset automatically provides 'list','create','retrive','update' and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True)
    def highlight(self,request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlight)
    
    def get_renderer_context(self):
        context= super().get_renderer_context()
        if self.action == 'highlight':
            context['renderer']= renderers.StaticHTMLRenderer()
        return context
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)