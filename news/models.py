from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete,pre_delete
from django.dispatch import receiver



class News(models.Model):
    title = models.CharField(max_length=150 )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT ,blank=True)

    def get_absolute_url(self):
        return reverse('news_post', kwargs={"id": self.pk})

    def __str__(self):
        return self.title
 

@receiver(pre_delete, sender=News)
def submission_delete(sender, instance, **kwargs):
    instance.photo.delete() 
    # instance.photo.delete(False) for filefield


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)


    def get_absolute_url(self):
        return reverse('category', kwargs={"id": self.pk})

    def __str__(self):
        return self.title