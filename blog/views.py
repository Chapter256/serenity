from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def EditComment(request, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    form = CommentForm(instance = comment)
    if request.user.username == comment.name:
        if request.method == "POST":
            form = CommentForm(request.POST, request.FILES, instance = comment)
            if form.is_valid():
                form.save(commit = False)
                form.save()
            post = get_object_or_404(Post, id = comment.post.id)
            messages.info(request, 'Your comment has been successfully edited!')
            return redirect('post_detail', slug=post.slug)
        return render(
            request,
            'edit_comment.html',
            {
                'form': form
            }
        )

def DeleteComment(request, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    form = CommentForm(instance = comment)
    if request.user.username == comment.name:
        if request.method == "POST":
            comment.delete()
            post = get_object_or_404(Post, id = comment.post.id)
            messages.info(request, 'Your comment has been successfully deleted!')
            return redirect('post_detail', slug=post.slug)
        return render(
            request,
            'delete_comment.html',
            {
                'form': form
            }
        )