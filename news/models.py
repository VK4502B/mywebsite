from django.db import models
from django.template.defaultfilters import slugify


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):              # __unicode__ on Python 2
        return self.full_name



    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    

    def __str__(self):
        return self.category_name
   


class Article(models.Model):
    pub_date = models.DateField()
    pub_time = models.TimeField(default="00:00")
    headline = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(allow_unicode=False)    
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.headline    


    class Meta:
        """docstring for Meta"""

        ordering = ["-pub_date","-pub_time"]
            


    def __str__(self):              # __unicode__ on Python 2
        return self.headline  



        