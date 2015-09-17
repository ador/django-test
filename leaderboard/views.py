from django.shortcuts import render
from django.utils import timezone
from .models import Submission, BubiParticipant
from leaderboard.tasks import *

# Create your views here.


def submission_list(request):
    entries = Submission.objects.filter(submission_date__lte=timezone.now()).order_by('submission_date')
    res = add.delay(3,-2)
    status = str(res.state)
    resultval = res.get()
    return render(request, 'leaderboard/leaderboard.html', {'submissions': entries, 'lenof': resultval, 'status': str(status)})
