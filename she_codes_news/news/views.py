#Create your views here
#request --> response
#request handler
#action


from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    #use the name we called the parth in urlpattern to get the url path
    success_url = reverse_lazy('news:index')
    
    #overriding form_valid which is on generic.CreateView
    def form_valid(self, form):
        #set author to user logged in
        form.instance.author = self.request.user
        return super().form_valid(form)



