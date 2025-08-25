# from django.db import models
# from datetime import date

# class Person(models.Model):
#     # Field types + options
#     first_name = models.CharField("person's first name", max_length=30, blank=False)
#     last_name = models.CharField(max_length=30, null=False)
#     birth_date = models.DateField(default=date.today, help_text="Ngày sinh của người")
#     email = models.EmailField(unique=True)
#     shirt_size = models.CharField(
#         max_length=1,
#         choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")],
#         default="M"
#     )
    
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
# # Quick Example + Using Models + Fields + Field Types + Field Options

# # Many-to-One
# class Manufacturer(models.Model):
#     name = models.CharField(max_length=100)

# class Car(models.Model):
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#     model_name = models.CharField(max_length=100)
#     year = models.IntegerField()

# # Many-to-Many + Extra fields
# class Topping(models.Model):
#     name = models.CharField(max_length=50)

# class Pizza(models.Model):
#     name = models.CharField(max_length=50)
#     toppings = models.ManyToManyField(Topping, through="PizzaTopping")

# class PizzaTopping(models.Model):
#     pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#     topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
#     extra_cheese = models.BooleanField(default=False)
