from django.shortcuts import render
from .models import Tweet
from django.contrib import messages
from .forms import TweetForm,UserRegistrationForm,CommentForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.signing import TimestampSigner
from django.core.signing import BadSignature, SignatureExpired
# Create your views here.

def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets= Tweet.objects.all().order_by('-created_at')
    comment_form = CommentForm()
    return render(request,'tweet_list.html',{'tweets':tweets,'form': comment_form})
@login_required(login_url='login')
def tweet_create(request):
    if request.method == "POST":
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.user =request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form =TweetForm()
    return render(request,'tweet_form.html',{'form':form})
@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == "POST":
         form=TweetForm(request.POST,request.FILES,instance=tweet)
         if form.is_valid():
             tweet=form.save(commit=False)
             tweet.user=request.user
             tweet.save()
             return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)    
    return render(request,'tweet_form.html',{'form':form})
@login_required
def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confrim_delete.html',{'tweet':tweet})

from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False  # Require email confirmation
            user.save()
            
            # Redirect to custom "confirm your email" page
            return redirect('email_confirmation_sent')
         
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tweet_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    if request.method == "POST":
        auth_logout(request)  # now calling the real Django logout function
        return render(request, 'registration/logout.html')
    
def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Tweet.objects.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
        )

    return render(request, 'search_results.html', {'results': results, 'query': query})

@login_required(login_url='login')
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)  # Unlike
    else:
        tweet.likes.add(request.user)     # Like

    return redirect('tweet_list')  # Redirect to home

@login_required(login_url='login')
def add_comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tweet = tweet
            comment.user = request.user
            comment.save()
    return redirect('tweet_list')


signer = TimestampSigner()

def confirm_email(request, token):
    try:
        username = signer.unsign(token, max_age=60*60*24)  # 24 hours
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        return redirect('login')  # Redirect to login after confirmation
    except (BadSignature, SignatureExpired, User.DoesNotExist):
        return redirect('error_page')
    
def email_confirmation_sent(request):
    return render(request, 'registration/email_confirmation_sent.html')

def test_message(request):
    messages.warning(request, "This is a test warning!")
    return render(request, 'registration/login.html')