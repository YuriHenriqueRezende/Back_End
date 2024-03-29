from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixion


class CustomUser(AbstractBaseUser, PermissionsMixion):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    resgistrationNumber = models.CharField(max_lenght=30)
    phoneNumber = models.CharField(max_lenght=15, null=True, blanck=True)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    def __str__(self):
        return self.email

BLOCK = [
    ('A','Bloco A'),
    ('B','Bloco B'),
    ('C','Bloco C'),
]

class Environments(models.Model):
    name = models.CharField(max_length=100)
    block = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
STATUS = [
        ("AB","Aberta"),
        ("EA","Em Andameno"),
        ("CA","Cancela"),
        ("CO","Concluido"),
        ("EN","Encerrado"),

]

class task(models.Model):
    environmentsFK = models.ForeignKey(Environments, related_name="Environments", on_delete=models.CASCADE)
    reporterFK = models.ForeignKey(CustomUser, related_name="TaskesCustomUser", on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    diagnostic = models.CharField(max_length=100)
    type = tatus = models.CharField(max_length=100, choices=task_type)
    status = models.CharField(max_length=100, choices=STATUS)
    environmentAlocationFK = models.ForeignKey(EnvironmentAlocation, related_name="TaskEnvironmentAlocation", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TasksAssignees(models.Model):
    taskFK = models.ForeignKey(task, related_name="taskAssigneesTask", on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(task, related_name="taskAssigneesTask", on_delete=models.CASCADE)



class Equipments(models.Model):
    name = models.CharField(max_length=100)
    code = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

