from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Homepage(models.Model):
    banner_title = models.CharField(max_length=200, default='')    
    banner_button_text = models.CharField(max_length=200, default='')
    banner_button_link = models.CharField(max_length=200, default='/')
    banner_pic = models.ImageField(
        upload_to='polls/static/assets/homepage/'
    )