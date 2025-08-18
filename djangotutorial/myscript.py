import os
import django
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotutorial.settings")  # sửa tên project nếu khác
django.setup()

from polls.models import Question, Choice

q = Question.objects.get(pk=1)

q.choice_set.create(choice_text="Not much", votes=0)
q.choice_set.create(choice_text="The sky", votes=0)
c = q.choice_set.create(choice_text="Just hacking again", votes=0)

print(c.question)
print(q.choice_set.all())
print(q.choice_set.count())

current_year = timezone.now().year
print(Choice.objects.filter(question__pub_date__year=current_year))

q.choice_set.filter(choice_text__startswith="Just hacking").delete()
