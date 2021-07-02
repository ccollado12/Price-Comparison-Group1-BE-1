from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Post
from django.http import HttpResponse

# Create your views here.

def index(request):
    shelf = Comment.objects.all()
    return render(request, 'comment/library.html', {'shelf' : shelf})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    create_comment = None

    if request.method == 'POST':
        comment_form = Comment(data=request.POST)
        if comment_form.is_valid():

            create_comment = comment_form.save(commit=False)
            create_comment.post = post
            create_comment.save()
    else:
        comment_form = Comment()

    return render(request, {'post' : post,
                            'comments' : comments,
                            'create_comment': create_comment})

def update_comment(request, comment_id):
    comment_id = int(comment_id)
    try:
        comment_sel = Comment.objects.get(id = comment_id)
    except Comment.DoesNotExist:
        return redirect('index')
    
def delete_comment(request, comment_id):
    comment_id = int(comment_id)
    try:
        comment_sel = Comment.objects.get(id = comment_id)
    except Comment.DoesNotExist:
        return redirect('index')
    comment_sel.delete()
    return redirect('index')


