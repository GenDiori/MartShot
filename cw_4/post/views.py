from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post
from django.core.files.storage import FileSystemStorage

def index(request):
    return redirect('threads_list')

def threads_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        Thread.objects.create(name=name, description=description)
        return redirect('threads_list')

    threads = Thread.objects.all()
    return render(request, 'threads/list.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.POST.get('author')
        picture = request.FILES.get('picture')

        if picture:
            fs = FileSystemStorage()
            filename = fs.save(picture.name, picture)

        Post.objects.create(title=title, description=description, author=author, picture=filename, thread=thread)
        return redirect('thread_detail', id=thread.id)

    return render(request, 'threads/detail.html', {'thread': thread, 'posts': posts})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('threads_list')

def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == "POST":
        thread.name = request.POST.get('name')
        thread.description = request.POST.get('description')
        thread.save()
        return redirect('thread_detail', id=thread.id)
    return render(request, 'threads/edit.html', {'thread': thread})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.author = request.POST.get('author')

        if request.FILES.get('picture'):
            fs = FileSystemStorage()
            filename = fs.save(request.FILES['picture'].name, request.FILES['picture'])
            post.picture = filename

        post.save()
        return redirect('thread_detail', id=post.thread.id)

    return render(request, 'posts/edit.html', {'post': post})
