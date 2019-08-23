from django.db import models

# Create your models here.
class Blog(models.Model):
    titles = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        s = self.body[:100]
        if len(s)==100:
            print('greater than 100')
            return s+'...'
        else:
            print('less than 100')
            return s

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
