from django.db import models



class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT ,blank=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)


    def __str__(self):
        return self.title