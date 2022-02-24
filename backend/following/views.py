from django.shortcuts import render
from .models import Following
from django.views import generic

class IndexView(generic.ListView):
    #template_name = 'polls/index.html'
    #context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Following.objects.order_by('following')

class DetailView(generic.DetailView):
    model = Following
    template_name = 'polls/detail.html'

# Create your views here.
def getFollowers():
    # 'service/authors/{AUTHOR_ID}/followers/'
    pass

def getFollowing(author_id):
    following = Following.objects.get(author=author_id)
    return following.following
    # 'service/authors/{AUTHOR_ID}/following/'

def addFollower():
    # 'service/authors/{AUTHOR_ID}/addFollower/'
    pass

def removeFollower():
    # 'service/authors/{AUTHOR_ID}/removeFollower/'
    pass

def addFollowing():
    # 'service/authors/{AUTHOR_ID}/addFollowing/'
    pass

def removeFollowing():
    # 'service/authors/{AUTHOR_ID}/removeFollowing/'
    pass
