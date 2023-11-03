from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import (
    require_safe,
    require_POST,
    require_http_methods,
)
from .models import Review, Comment, Reply
from .forms import ReviewForm, CommentForm, ReplyForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    reply_form = ReplyForm()
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
        'reply_form': reply_form,

    }
    return render(request, 'community/detail.html', context)

@login_required
@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment_form.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)

@login_required
@require_POST
def like(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked':is_liked,
        'likes_count':review.like_users.count()
    }
    return JsonResponse(context)

@login_required
@require_POST
def like_comment(request,review_pk,comment_pk):

    comment = get_object_or_404(Comment,pk=comment_pk)

    if request.user in comment.like_users.all():
        comment.like_users.remove(request.user)
        is_liked = False
    else:
        comment.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked':is_liked,
        'likes_count':comment.like_users.count()
    }
    return JsonResponse(context)


@login_required
@require_POST
def create_reply(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    reply_form = ReplyForm(request.POST)
    if reply_form.is_valid():
        reply = reply_form.save(commit=False)
        reply.comment = comment
        reply.user = request.user
        reply_form.save()
        return redirect('community:detail', review.pk)
    context = {
        'reply_form': reply_form,
        'review': review,
        'replys': comment.reply_set.all(),
    }
    return render(request, 'community/detail.html', context)


@login_required
@require_POST
def like_reply(request,review_pk,comment_pk, reply_pk):
    reply = get_object_or_404(Reply, pk=reply_pk)

    if request.user in reply.like_users.all():
        reply.like_users.remove(request.user)
        is_liked = False
    else:
        reply.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked':is_liked,
        'reply_likes_count':reply.like_users.count()
    }
    return JsonResponse(context)