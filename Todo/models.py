from django.db import models
from django.contrib.auth.models import User
#from myauth.models import User

# Create your models here.

class Todo(models.Model):
    PRIORITY_LIST = (
        (0, 'Low'),
        (5, 'Normal'),
        (10, 'High'),
        (15, 'Urgent'),
    )
    title = models.CharField(max_length=140)
    owner = models.ForeignKey(User)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_LIST, default=5)
    added_on = models.DateTimeField(auto_now_add=True)
    due_on = models.DateField()
    class Meta:
        permissions = (('view_todo', 'Can view todo'),)
        ordering = ['due_on']
    def __unicode__(self):
        return u"%s" % self.title
    @models.permalink
    def get_absolute_url(self):
        return ('todo_detail', [int(self.pk)])
