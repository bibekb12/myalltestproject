from django.urls import path
from library.swagger import schema_view

urlpatterns = [
    path(
            "",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
]