from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
from django.shortcuts import render



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.reply = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = post.author
            new_comment.save()
    else:
        comment_form = CommentForm()
    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'comments': comments,
        'new-comment': new_comment,
        'comment_form': comment_form,

    }    
    
    return render(request, template, context)


def category(request):
    cat = Category.objects.all()
    return render(request, 'blog/category.html', {'cat': cat})

def tags(request):
    tags = Tags.objects.all()
    return render(request, 'blog/tags.html', {'tag': tags})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    post = Post.objects.filter()
    return render(request, 'blog:post_detail.html', {'category': category, 'posts': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog/post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm1(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = RegistrationForm1(request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username = username, password = password)
            
#         if user is not None:
#             login(request, user)
#             messages.success(request,'Successfully Loggedin')
#             return redirect('blog:/') 
#         else:
#             messages.error(request,'Sorry Try again')   
#      else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
#     return render(request, 'blog/login.html')


def logout(request):
        # if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'Successfully Loggedout')
        return redirect('/')

def edit(request, pk):
    form = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = RegistrationForm1(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.published_date = timezone.now()
            form.save()
            return redirect('blog/post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update.html', {'form': form})

def update(request):
    username = models.CharField(max_length=100)
    email = models.TextField()
    password = models.CharField(max_length=50)
    form = RegistrationForm1(request.POST)
    return render(request,'blog/edit.html', {'form': form})  

