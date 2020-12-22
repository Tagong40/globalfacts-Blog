from django.shortcuts import render, redirect
from .models import Category, Post, commet
from django.shortcuts import get_object_or_404
import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Max
from .forms import CommetForm


def index(request):
    popular = Post.objects.order_by('-hit_count_generic__hits')[:3]
    posts = Post.objects.all()
    video = Post.objects.filter(tags=4)[0:3]
    recent = Post.objects.filter(title__contains="u")[0:4]
    header1 = Post.objects.filter(header=True)[0:1]
    header2 = Post.objects.filter(header=True)[1:3]
    post3 = Post.objects.order_by('-date')[0:3]
    post = Post.objects.order_by('-date')[3:10]
    all_cate = Category.objects.all()
    footer = Category.objects.filter(id=9)[0:5]
    f_count = Post.objects.filter(category__title__startswith="Business").distinct().count()

    footer1 = Category.objects.filter(id=2)[0:5]
    f1_count = Post.objects.filter(category__title__startswith="Faith & Science").distinct().count()

    footer2 = Category.objects.filter(id=6)[0:5]
    f2_count = Post.objects.filter(category__title__startswith="Arts").distinct().count()

    footer3 = Category.objects.filter(id=7)[0:5]
    f3_count = Post.objects.filter(category__title__startswith="Sunday Facts").distinct().count()


    paginator = Paginator(post,4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {'all_cate':all_cate,'header1':header1,'header2':header2,'post3':post3,'post':paginated_queryset,'recent':recent,'video':video, 'page_request_var':page_request_var,
               'footer':footer,'f_count':f_count,'footer1':footer1, 'f1_count':f1_count,'footer2':footer2,
               'f2_count':f2_count,'footer3':footer3,'f3_count':f3_count,'popular':popular}
    template = 'index.html'
    return render(request, template, context)



def indexDetail(request, slug): 
    video = Post.objects.filter(tags=4)[0:3]
    recent = Post.objects.order_by("-date")[6:9]
    all_cate = Category.objects.all()
    post = get_object_or_404(Post, slug=slug)
    news = Post.objects.filter(title=post, id__gt=post.id).order_by("id")[0:1]
    news2 = Post.objects.filter(title=post, id__gt=post.id).order_by("id")[1:2]
    message = commet.objects.filter(post=post, status=True)
    c_msg = message.count()
    popular = Post.objects.order_by('-hit_count_generic__hits')[:3]
    
    if request.method == "POST":
        form = CommetForm(request.POST)
        if form.is_valid():
            form.instance.post = post
            form.save()
    else:
        form = CommetForm()
    context = {'post':post,'all_cate':all_cate,'news':news,'news2':news2,'recent':recent,'video':video,
               'form':form,'message':message,'c_msg':c_msg,'popular':popular}
    template = 'single.html'

    return render(request, template, context)




def category(request, slug):
    video = Post.objects.filter(tags=4)[0:3]
    news = Post.objects.filter(tags=3)[0:3]
    d = get_object_or_404(Category, slug=slug)
    cate = Post.objects.filter(category=d)
    all_cate = Category.objects.all()
    paginator = Paginator(cate,6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    template = 'category.html'
    return render(request, template,{'all_cate':all_cate,'d':d,'cate':paginated_queryset ,'video':video,'news':news,'page_request_var': page_request_var})