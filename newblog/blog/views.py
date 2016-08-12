from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


from .models import Post
from .forms import PostCreateForm


def post_list(request):
    list = Post.objects.all()
    context = {'list': list}
    template = 'post_list.html'
    return render(request, template, context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    template = 'post_detail.html'
    return render(request, template, context)


def post_new(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostCreateForm()
    return render(request, 'post_new.html', context={'form': form})


def edit_post(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostCreateForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostCreateForm(instance=post)
    return render(request, 'post_new.html', context={'form': form})


def post_delete(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts')



