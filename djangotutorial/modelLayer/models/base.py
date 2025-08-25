from django.db import models

class Author(models.Model):
    # Automatic primary key field -> id
    name = models.CharField(max_length=100, verbose_name="Tên tác giả")
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["name"]  # Meta option
        verbose_name = "Tác giả"
        verbose_name_plural = "Các tác giả"

    def __str__(self):
        return self.name

    def age(self):
        import datetime
        if self.birth_date:
            return datetime.date.today().year - self.birth_date.year
        return None
