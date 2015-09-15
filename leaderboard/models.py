from django.db import models
from django.utils import timezone

# Create your models here.

class BubiParticipant(models.Model):
    auth_user = models.ForeignKey('auth.User')
    first_email = "alma@iizz.com" # fake example
    more_emails = []
    submissions = []

class Submission(models.Model):
    submittedDataString = ""
    team = models.ForeignKey('leaderboard.BubiParticipant')
    submission_date = models.DateTimeField(default = timezone.now)
    evaluated_date = models.DateTimeField(blank = True, null = True)
    is_valid = False
    score = 0.0

    def is_last_valid_score_of_team(self):
        return is_last_valid

    def set_last_valid_score_of_team(self, is_last):
        self.is_last_valid = is_last
        self.save()

    def __str__(self):
        return self.team.name + " " + str(self.created_date)

