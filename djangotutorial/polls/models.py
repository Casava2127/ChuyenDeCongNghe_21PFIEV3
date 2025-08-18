from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# Ở đây, mỗi mô hình được biểu diễn bởi một lớp con django.db.models.Model. Mỗi mô hình có một số biến lớp, mỗi biến đại diện cho một trường cơ sở dữ liệu trong mô hình.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    

# In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.
# Question.objects.all()
# from polls.models import Question, Choice
