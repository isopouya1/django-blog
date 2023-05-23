
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Blog , Category , User
# Create your views here.

def home(request,page=1):
    blog_list = Blog.objects.Published()
    pageinetoir = Paginator(blog_list,3)
    blogs = pageinetoir.get_page(page)
    context = {
        'blogs':blogs,
    }
    return render(request,'index.html',context)


def detail(request,pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog':blog
    }
    return render(request,'post.html',context)

def category(request,slug,page=1):
    category = Category.objects.get(slug=slug,is_active = True)
    blog_list = category.blogs.Published()
    pageinetoir = Paginator(blog_list,3)
    blogs = pageinetoir.get_page(page)
    context = {
             "category":category,
             "blogs":blogs
    }     
    return render(request,'category.html',context)

def author_page(request,name):
    user = User.objects.get(username = name)
    blogs = user.blogs.all()
    context= {
        'blogs': blogs
    }
    return render(request,"author.html",context)