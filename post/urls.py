from django.urls import path
from .views import HomePageView, UsuariosView, UpdatePageView, DeletePageView
from post.views import CreateView, DetailPageView

urlpatterns= [
    path("", HomePageView.as_view(), name = "post"),
    path("usuarios", UsuariosView.as_view(), name="usuarios"),
    path("post/create", CreateView.as_view(), name="create"),
    path("post/detail/<int:pk>", DetailPageView.as_view(), name="detail"),
    path("post/detail/<int:pk>/update", UpdatePageView.as_view(), name="update"),
    path("post/detail/<int:pk>/delete", DeletePageView.as_view(), name="delete")

]