from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Message, Comment
from login_app.models import User

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        # newest messages first
        'all_messages': Message.objects.all().order_by('-created_at'),
    }
    return render(request, 'wall_app/wall.html', context)

def post_message(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method != 'POST':
        return redirect('/wall')
    
    if len(request.POST['message'].strip()) == 0:
        messages.error(request, "Message cannot be empty.")
        return redirect('/wall')
    
    Message.objects.create(
        message = request.POST['message'],
        user    = User.objects.get(id=request.session['user_id']),
    )
    return redirect('/wall')

def post_comment(request, msg_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method != 'POST':
        return redirect('/wall')
    
    if len(request.POST['comment'].strip()) == 0:
        messages.error(request, "Comment cannot be empty.")
        return redirect('/wall')
    
    Comment.objects.create(
        comment = request.POST['comment'],
        user    = User.objects.get(id=request.session['user_id']),
        message = Message.objects.get(id=msg_id),
    )
    return redirect('/wall')

def delete_message(request, msg_id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    msg = Message.objects.get(id=msg_id)
    
    # ✅ SENSEI BONUS: فقط صاحب الرسالة + خلال 30 دقيقة
    if msg.user.id != request.session['user_id']:
        messages.error(request, "You can only delete your own messages.")
        return redirect('/wall')
    
    time_limit = timezone.now() - timedelta(minutes=30)
    if msg.created_at < time_limit:
        messages.error(request, "You can only delete messages within 30 minutes.")
        return redirect('/wall')
    
    msg.delete()
    return redirect('/wall')