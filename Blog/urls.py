from django.urls import path
from Blog.views import (
create_blog_view,
detail_blog_view,
edit_blog_view,
)

app_name = 'Blog'

urlpatterns = [
    path('create/',create_blog_view, name="create"),
    path('<slug>/',detail_blog_view, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit"),

]