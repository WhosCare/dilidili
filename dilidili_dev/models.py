from django.db import models
from dilidili_dev.users import User

# models
# ��Ƶmodel
class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos')
    image = models.ImageField()
    describe = models.CharField(max_length=200)
    tag = models.CharField(max_length=84)  # ÿ��tag����20���ַ���ÿ����Ƶ�������4��tag��tag����'#'�ָ�
    play = models.IntegerField(default=0)  # ���Ŵ���
    money = models.IntegerField(default=0)  # Ӳ����
    owner = models.OneToOneField('User')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # ��¼�ϴ�ʱ��
    status = models.IntegerField(default=0)  # �����0�������1������2


# ��Ļ
class Bullet(models.Model):
    video = models.ForeignKey('Video')
    user = models.ForeignKey('User')
    time = models.IntegerField(default=0)  # ��¼���ʱ�䣬�������Ƶ��ʼʱ���֡����
    send_date = models.DateTimeField(auto_now=False, auto_now_add=True)  # �ϴ�ʱ�䣬�����ж���ѯ
    content = models.CharField(max_length=200)
    color = models.CharField(max_length=10)  # ��Ļ��ɫ


# ����
class Comment(models.Model):
    video = models.ForeignKey('Video')
    user = models.ForeignKey('User')
    content = models.CharField(max_length=400)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)


# ˽��
class Message(models.Model):
    user_from = models.ManyToManyField('User', related_name="user_from")
    user_to = models.ManyToManyField('User', related_name="user_to")
    status = models.BooleanField(default=False)  # �Ѷ� δ��
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # ��¼����ʱ��


# ���� Ĭ�ϣ�һ�㲻����
class Category(models.Model):
    name = models.CharField(max_length=40)
    video_list = models.ManyToManyField('Video')


# ר��
class Album(models.Model):
    image = models.ImageField()
    money = models.IntegerField(default=0)  # Ӳ�����������ר��ҳ���Ӳ�ҵ����
    owner = models.OneToOneField('User')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # ��¼�ϴ�ʱ��
    name = models.CharField(max_length=40)
    describe = models.CharField(max_length=200)
    video_list = models.ManyToManyField('Video', through="AlbumVideo")


# ר��--��Ƶ��ϵ
class AlbumVideo(models.Model):
    album = models.ForeignKey('Album')
    video = models.ForeignKey('Video')
    video_number = models.IntegerField()  # video��album�е����


# ��ҳ��Ƶ
class BestVideo(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    video = models.OneToOneField('Video')
