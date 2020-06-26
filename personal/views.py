from django.shortcuts import render
from Blog.models import BlogPost
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
# Create your views here.
from operator import attrgetter
from Blog.views import get_blog_queryset

BLOG_POSTS_PER_PAGE = 2

def home_screen_view(request):
    context = {}

    query =""
    if request.GET:
        query = request.GET.get('q','')
        context['query'] = str(query)
    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts']= blog_posts


    '''context = {'some_str': " some string passed to the view ",
               'some_nbr': 12345,
               }'''
    '''list_of_values = []
    list_of_values.append("first")
    list_of_values.append("second")
    list_of_values.append("third")
    list_of_values.append("fourth")
    context['list_of_values'] = list_of_values
    questions = Question.objects.all()
    context['questions'] = questions'''

    #pagination

    page= request.GET.get('page',1)
    blog_posts_paginator= Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger :
        blog_posts= blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage :
        blog_posts= blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, "personal/home.html", context)
