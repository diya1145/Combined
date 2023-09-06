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
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'blog/register.html', {'form': form})
    else:
        return render(request, 'blog/register.html', {'form': form})

def user_login(request):    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("/")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = RegisterForm()
        messages.error(request,"Invalid username or password.")
    return render(request, 'blog/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')  

def edit_profile(request, pk):
    # user = User.objects.get(pk = pk)
    user = get_object_or_404(User, pk=pk)
    print('user',user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('/')  # Redirect to the user's profile after editing
    else:
        form = UserForm(instance=request.user)
    return render(request, 'blog/profile_update.html', {'form': form})

def author_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog:author_list.html', {'posts': posts})
