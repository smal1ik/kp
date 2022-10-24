from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AppService(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "Service: {}, url: {}".format(self.name, self.url)
    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

class UserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    darktheme = models.BooleanField(default=False)

    def __str__(self):
        return "Dark theme: {}".format(self.darktheme)
    class Meta:
        verbose_name = "Настройки пользователя"
        verbose_name_plural = "Настройки пользователей"

class Worker(models.Model):
    #user = models.ForeignKey(User, on_delete==models.CASCADE)
    #id #` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    display_name = models.CharField(max_length=200) # отображаемое ФИО` varchar(200) DEFAULT '0',
    last_name = models.CharField(max_length=200) # фамлия` varchar(200) DEFAULT '0',
    first_name = models.CharField(max_length=200) # имя` varchar(200) DEFAULT '0',
    middle_name = models.CharField(max_length=200, null=True) # отчество` varchar(200) DEFAULT '0',
    department = models.CharField(max_length=255, null=True) # подразделение` varchar(255) DEFAULT '0',
    mail = models.CharField(max_length=200, null=True) # email` varchar(200) DEFAULT '0',
    inner_phone = models.CharField(max_length=200, null=True) # внутренний телефон` varchar(200) DEFAULT '0',
    outer_phone = models.CharField(max_length=200, null=True) # городской телефон` varchar(200) DEFAULT '0',
    mobile_phone = models.CharField(max_length=200, null=True) # мобильный` varchar(200) DEFAULT '0',
    post = models.CharField(max_length=255, null=True) # должность` varchar(255) DEFAULT '0',
    room = models.CharField(max_length=50, null=True) # кабинет` varchar(50) DEFAULT '0',
    birth_date = models.CharField(max_length=200, null=True) # день рождения` varchar(200) DEFAULT '0',
    account_name = models.CharField(max_length=200, null=True) #логин` varchar(200) DEFAULT '0',
    gender = models.CharField(max_length=20) # пол` varchar(20) DEFAULT '0'

    def __str__(self):
        return "User: {}, phone {}".format(self.display_name, self.inner_phone)
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

class OtherWorker(models.Model):
    GENDER_TYPES = [
        ('1', 'None'),
        ('2', 'Male'),
        ('3', 'Female'),
    ] # пол` varchar(20) DEFAULT '0'

    #user = models.ForeignKey(User, on_delete==models.CASCADE)
    #id #` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    display_name = models.CharField(max_length=200) # отображаемое ФИО` varchar(200) DEFAULT '0',
    last_name = models.CharField(max_length=200) # фамлия` varchar(200) DEFAULT '0',
    first_name = models.CharField(max_length=200) # имя` varchar(200) DEFAULT '0',
    middle_name = models.CharField(max_length=200, null=True, blank=True) # отчество` varchar(200) DEFAULT '0',
    department = models.CharField(max_length=255, null=True, blank=True) # подразделение` varchar(255) DEFAULT '0',
    mail = models.CharField(max_length=200, null=True, blank=True) # email` varchar(200) DEFAULT '0',
    inner_phone = models.CharField(max_length=200, null=True, blank=True) # внутренний телефон` varchar(200) DEFAULT '0',
    outer_phone = models.CharField(max_length=200, null=True, blank=True) # городской телефон` varchar(200) DEFAULT '0',
    mobile_phone = models.CharField(max_length=200, null=True, blank=True) # мобильный` varchar(200) DEFAULT '0',
    post = models.CharField(max_length=255, null=True, blank=True) # должность` varchar(255) DEFAULT '0',
    room = models.CharField(max_length=50, null=True, blank=True) # кабинет` varchar(50) DEFAULT '0',
    birth_date = models.CharField(max_length=200, null=True, blank=True) # день рождения` varchar(200) DEFAULT '0',
    account_name = models.CharField(max_length=200, null=True, blank=True) #логин` varchar(200) DEFAULT '0',
    gender = models.CharField(choices=GENDER_TYPES, default=1, max_length=1)

    def __str__(self):
        return "Other user: {}, phone {}".format(self.display_name, self.inner_phone)
    class Meta:
        verbose_name = "Дополнительный cотрудник"
        verbose_name_plural = "Дополнительные сотрудники"

class Post(models.Model):
    title = models.CharField(max_length=200)
    shorttext = models.CharField(max_length=200)
    text = models.TextField()
    short = models.BooleanField(default=True)

    def __str__(self):
        return "Статья: {}".format(self.title)
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"



