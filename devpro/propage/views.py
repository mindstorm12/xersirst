from django.http import HttpResponse, Http404, HttpResponseRedirect

import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404


from .models import Projex, Choice

from django.views import generic

class IndexView(generic.ListView):
    template_name = 'propage/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Projex.objects.order_by('-pub_date')[:5]


def detail(request, question_id):
    try:
        question = Projex.objects.get(pk=question_id)
    except Projex.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'propage/developer_bio.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Projex, pk=question_id)
    return render(request, 'propage/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Projex, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'propage/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('propage:results', args=(question.id,)))


def current_datetime(request):
    now = datetime.datetime.now()

    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)




def IviView(request):
    return render(request, 'propage/bootstrap_test.html')


def About(request):
    return render(request, 'propage/about.html')

def Game_rab(request):
    return render(request, 'propage/rollaball_web/roll_a_ball.html')
