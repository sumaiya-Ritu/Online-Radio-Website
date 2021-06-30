from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from main.models import *


def home(request):
    if request.method == "GET":
        comments = Comment.objects.all().order_by('-date')
        # comment_is_liked = False
        # if comment.like.filter(id=request.user.id).exists():
        #     comment_is_liked = True
        context = {
            "comments": comments,
        }
        return render(request, 'main/home.html', context)

    elif request.method == 'POST':
        if request.user.is_authenticated:
            body = request.POST["body"]
            comment = Comment(content = body, author = request.user)
            comment.save()
            messages.success(request, 'Commented successfully!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            return redirect('/login')


def reply(request, id):
    if request.user.is_authenticated:
        if request.method == "GET":
            comment = Comment.objects.get(id=id)
            context = {
                "comment": comment
            }
            return render(request, "main/reply.html", context)

        elif request.method == "POST":
            body = request.POST["body"]
            reply = Reply(content = body, author = request.user, comment_id=id)
            reply.save()
            messages.success(request, 'Replied successfully!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return redirect('/login')


def like_comment(request):
    comment = Comment.objects.get(id=request.POST["comment_id"])
    is_liked = False
    if comment.like.filter(id=request.user.id).exists():
        comment.like.remove(request.user)
        is_liked = False

    else:
        comment.like.add(request.user)
        is_liked = True
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def like_reply(request):
    reply = Reply.objects.get(id=request.POST["reply_id"])
    is_liked = False
    if reply.like.filter(id=request.user.id).exists():
        reply.like.remove(request.user)
        is_liked = False

    else:
        reply.like.add(request.user)
        is_liked = True
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))