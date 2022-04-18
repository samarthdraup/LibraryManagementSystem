from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    book_id = models.CharField(max_length=50,primary_key=True)
    book_title = models.CharField(max_length=50,unique=True)
    author = models.CharField(max_length=50)
    users = models.ManyToManyField(User, through='Books_log')
    def __str__(self):
        return self.book_title

#-books log--userid,bookid,date issued, date exp,date returned
class Books_log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    date_issued  = models.DateField(auto_now=True)
    date_exp = models.DateField(auto_now=True)
    date_returned = models.DateField(auto_now=True)
    def __str__(self):
        return  str(self.user)

