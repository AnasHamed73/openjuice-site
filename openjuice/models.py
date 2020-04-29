from django.db import models
from django.utils import timezone
import datetime


class Topic(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=100, unique=True)
    overview = models.TextField(max_length=500, null=False, blank=False)
    # Educational resources: Books, Videos, Lectures, Tutorials
    # Milestone projects
    # Tools (editors, IDEs, environment setup)
    # Discussions


class Domain(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    topics = models.ManyToManyField(Topic)


class BookResource(models.Model):
    topics = models.ManyToManyField(Topic)
    source = models.URLField()
    title = models.CharField(max_length=200, unique=False)
    author = models.CharField(max_length=200, unique=False)
    year = models.IntegerField(unique=False, null=True, blank=True)

    class Meta:
        unique_together = ('title', 'author',)


class CourseResource(models.Model):
    topics = models.ManyToManyField(Topic)
    source = models.URLField()
    title = models.CharField(max_length=200, unique=False)
    organization = models.CharField(max_length=200, unique=False)
    year = models.IntegerField(unique=False)

    class Meta:
        unique_together = ('title', 'organization',)


class Tool(models.Model):
    topics = models.ManyToManyField(Topic)
    source = models.URLField()
    name = models.CharField(max_length=200, unique=False)
    type = models.CharField(max_length=200, unique=False)
    description = models.TextField(max_length=500, null=False, blank=False)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date < timezone.now()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

