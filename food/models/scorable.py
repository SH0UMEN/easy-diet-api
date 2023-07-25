from django.db import models


class Scorable:
	def get_scores_count(self):
		return self.scores.count()

	def get_score(self):
		return self.scores.aggregate(avg=models.Avg('value'))['avg'] or 0
