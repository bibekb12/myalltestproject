# from django.urls import path
# from snippets import views
# from rest_framework.urlpatterns import format_suffix_patterns

# # urlpatterns = [
# #     path('snippets/',views.snippet_list),
# #     path('snippets/<int:pk>', views.snippet_detail),
# # ]

# urlpatterns = [
#     path('snippets/',views.SnippetList.as_view()),
#     path('snippets/<int:pk>', views.SnippetDetail.as_view()),
#     path('users/',views.UserList.as_view()),
#     path('users/<int:pk>/',views.UserDetail.as_view()),

# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

# from rest_framework import renderers
# from snippets.views import api_root, SnippetViewSet, UserViewSet

# snippet_list = SnippetViewSet.as_view({
#     'get':'list',
#     'post':'create'
# })

# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrive',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight= SnippetViewSet.as_view({
#     'get':'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list= UserViewSet.as_view({
#     'get':'list'
# })

# user_detail= UserViewSet.as_view({
#     'get':'retrive'
# })

# urlpatterns = format_suffix_patterns([
#     path('',api_root),
#     path('snippets/',snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/',snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/',user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets.swagger import schema_view

from snippets import views

router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
