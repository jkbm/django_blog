from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm,CommentForm
import string

# Create your views here.
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(published_date__lte=timezone.now(), post = post).order_by('-published_date')
    tags = post.tags.replace(',','').split()
    print (tags)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'tags' : tags})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.edited_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_unpublished(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_unpublished.html', {'posts': posts})

def post_comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.published_date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_comment.html', {'form' : form})

def post_tags(request, tag):
    posts = Post.objects.filter(tags__icontains=tag).order_by('published_date')


    return render(request, 'blog/post_list.html', {'posts' : posts,})


