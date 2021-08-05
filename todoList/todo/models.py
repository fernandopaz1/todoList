from django.db import models
from django.utils import timezone
# Create your models here.


class Todo(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    state = models.CharField( default='backlog',max_length=20,
        choices=(
            ("backlog", "Backlog"),
            ("bloqueada", "Bloqueada"),
            ("enProceso", "En proceso"),
            ("avanzada", "avanzada"),
            ("atrazada", "Atrasada"),
            ("terminada", "Terminada")
        ))
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @staticmethod
    def delete_todo(pk):
        toDelete = Todo.objects.get(pk=pk)
        toDelete.delete()        

    def set_state(self ,new_state):
        self.state = new_state
        self.save() 

    @staticmethod
    def change_state(pk, new_state):
        toChange = Todo.objects.get(pk=pk)
        toChange.set_state(new_state)

    def __str__(self):
        return self.title
