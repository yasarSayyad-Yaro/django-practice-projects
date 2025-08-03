from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm,userRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')

# def tweet_list(request):
#     tweets=Tweet.objects.all().order_by('-created_at')

#     return render(request,'tweet_list.html',{'tweets':tweets})

def tweet_list(request):
    query = request.GET.get('q','').strip()
    if query:
        tweets = Tweet.objects.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
        ).order_by('-created_at')
    else:
        tweets = Tweet.objects.all().order_by('-created_at')

    return render(request, 'tweet_list.html', {
        'tweets': tweets,
        'query': query,
    })


@login_required
def tweet_create(request):
    if request.method=="POST":
       form=TweetForm(request.POST,request.FILES)
       if form.is_valid():
           tweet=form.save(commit=False)
           tweet.user=request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form=TweetForm()

    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id, user=request.user)
    if request.method == 'POST':
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

    if request.method=="POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confim_deletion.html',{'tweet':tweet})


def register(request):
    if request.method=='POST':
       form=userRegistrationForm(request.POST)
       if form.is_valid():
           user=form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(request,user)
           return redirect('tweet_list')

    else:
        form=userRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

def home(request):
    query=request.GET.get('q','').stript()
    if query:
        tweets=Tweet.objects.filter(
            Q(text_icontains=query) | Q(user_username_icontain=query)
        ).order_by('-created_at')
    else:
        tweets=Tweet.objects.all().order_by('-created_at')

    return render(request,'home.html',{
        'tweets':tweets,
        'query':query,
    })

def landing_page(request):
    return render(request,'landing_page.html')