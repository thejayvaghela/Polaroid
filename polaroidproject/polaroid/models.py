from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.template import Library
from PIL import Image

register = Library()

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    dob = models.DateField(null=True)#default=datetime.date(1997, 10, 19),
    gender = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    phone = PhoneNumberField(null=True)
    profilepic = models.ImageField(upload_to='profilepics/')
    bio = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)

''' def calculateAge(self):
        today = date.today()
        try:
            birthday = dob.replace(year = today.year)

        except ValueError:
            birthday = dob.replace(year = today.year,  month = dob.month + 1, day = 1)

        if birthday > today:
            return today.year - dob.year - 1
        else:
            return today.year - dob.year
    age=property(calculateAge)      '''

class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)
    postpic = models.ImageField(upload_to='postpics/')
    postcaption = models.CharField(max_length=100)
    posttime = models.DateTimeField(auto_now_add=True)

    def isLiked(self):
        l=[]
        for i in self.like_set.all():
            l.append(i.userid.user_email)
        return l

class Friend(models.Model):
    user1 = models.ForeignKey(User, related_name="user1", on_delete=models.CASCADE, null=True)
    user2 = models.ForeignKey(User, related_name="user2", on_delete=models.CASCADE, null=True)
    request_from = models.ForeignKey(User, related_name="request_from_r", on_delete=models.CASCADE, null=True)
    friends = models.BooleanField(default=False)
    request_pending = models.BooleanField(default=False)

class Like(models.Model):
    likeid = models.AutoField(primary_key=True)
    postid = models.ForeignKey(Post, on_delete=models.CASCADE)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    commentid = models.AutoField(primary_key=True)
    postid = models.ForeignKey(Post, on_delete=models.CASCADE)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=100, null=True)