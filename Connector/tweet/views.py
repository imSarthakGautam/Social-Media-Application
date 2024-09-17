from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm

from django.shortcuts import get_object_or_404, redirect
#get_obj-or_404 : To retrieve an object from the database or raise a 404 Not Found error if the object does not exist.
#redirect :To perform an HTTP redirect to another URL.


# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    # '-' : in descending order, so tweet has queryset of Tweet object, sorted
    return render(request, 'tweet_list.html', {'tweets':tweets})

def tweet_create(request):
    if request.method =='POST':
        form= TweetForm(request.POST, request.FILES)

        if form.is_valid():
            tweet=form.save(commit='false')
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form= TweetForm()
    return render(request, 'tweet_form.html', {'form':form})

def tweet_edit(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method=='POST':
        form=form= TweetForm(request.POST, request.FILES, instance=tweet)

        if form.is_valid():
            tweet=form.save(commit='false')
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

    else :
        form = TweetForm(instance=Tweet)
    return render(request, 'tweet_form.html', {'form':form})


from django.shortcuts import get_object_or_404, redirect

def tweet_delete(request, tweet_id):
    # Retrieve the tweet object, ensuring it belongs to the current user
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    
    if request.method=='POST':
        # Delete the tweet
        tweet.delete()
    
        # Redirect to the tweet list after deletion
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'form':form})


