from django.db import models
from django.utils import timezone

# Create your models here.

class BubiParticipant(models.Model):
    auth_user = models.ForeignKey('auth.User')
    first_email = "alma@iizz.com" # fake example
    more_emails = []
    submissions = []

    def add_extra_email(self, email):
        # TODO if check_email
        self.more_emails.append(email)
        self.save()

    def add_submission(self, solution_file):
        # TODO create Submission
        self.submissions.append(solution_file)
        self.save()

    def __str__(self):
        return self.first_email

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
        return self.team.auth_user.username + " " + str(self.submission_date)

