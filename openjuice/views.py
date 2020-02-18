from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Domain, Topic


class IndexView(generic.ListView):
    template_name = 'openjuice/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'openjuice/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'openjuice/results.html'


def domains(request):
    ds = get_list_or_404(Domain)
    return render(request, 'openjuice/domains.html', {
        'domain_list': ds
    })


def domain(request, code):
    d = get_object_or_404(Domain, code=str(code).lower())
    return render(request, 'openjuice/domain.html', {
        'domain': d
    })


def topics(request):
    ts = get_list_or_404(Topic)
    return render(request, 'openjuice/topics.html', {
        'topic_list': ts
    })


def topic(request, code):
    topic = get_object_or_404(Topic, code=str(code).lower())
    return render(request, 'openjuice/topic.html', {
        'topic': topic
    })


def search_topics(request):
    try:
        topic = request.GET.get('topic', '')
        topics = Topic.objects.filter(name__icontains=topic)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist")
    return render(request, 'openjuice/topic_search_results.html', {
        'topics': topics,
        'not_found_message': 'No topics were found that match the search criteria'
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'openjuice/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('openjuice:results', args=(question.id,)))
