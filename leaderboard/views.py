from django.shortcuts import render
from django.utils import timezone
from .models import Submission, BubiParticipant

# Create your views here.

def submission_list(request):
    entries = Submission.objects.filter(submission_date__lte=timezone.now()).order_by('submission_date')
    return render(request, 'leaderboard/leaderboard.html', {'submissions': entries})
