from django.db import models
from django.utils import timezone

# Create your models here.

class ScoreEntry(models.Model):
    team = models.ForeignKey('auth.User')
    score = 0.0
    is_last_valid = False
    # ? dates ?
    created_date = models.DateTimeField(default = timezone.now)

    def is_last_valid_score_of_team(self):
        return is_last_valid

    def set_last_valid_score_of_team(self, is_last):
        self.is_last_valid = is_last
        self.save()

    def __str__(self):
        return self.team.name + " " + str(self.created_date)
