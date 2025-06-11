from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='banner_images/')
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.title


class Service( models.Model):
    image = models.ImageField(upload_to='service_imagea/')
    second_image =  models.ImageField(upload_to='service_imagea/', blank=True, null=True)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=100)
    short_content = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    duraction =models.FloatField(blank=True,null=True)    
    star = models.IntegerField(default=0)
    
    class Meta:
        ordering = ("-id",)
    
    def __str__(self):
        return self.title
    
    
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='galery_images/')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="photos")
    
    class Meta:
        verbose_name = "Photo Gallery"
        verbose_name_plural = "Photo Galleries"
        ordering = ("-id",)
    
    def __str__(self):
        return self.service.title + "(" + str(self.id) + ")"  
    
    
class Servicetag(models.Model):
    name = models.CharField(max_length=50)
    services = models.ManyToManyField(Service, related_name="tags")
    
    class Meta:
        verbose_name = "Service Tag"
        ordering = ("-id",)
    
    def __str__(self):
        return self.name 
    
    
      
    
class Customers(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='custom_imagea/')
    title = models.CharField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Companies(models.Model):
    logo = models.ImageField(upload_to='companies_images/')
    
    def __str__(self):
        return self.logo
    
    
class SosialMedia(models.Model):
    icon = models.CharField(max_length=100)
    
    def __str__(self):
        return self.icon
    
    
class SiteSettings(models.Model):
    name = models.CharField(max_length=100)
    icontent = models.TextField()
    image = models.ImageField(upload_to='settings_images/')
    elogo = models.ImageField(upload_to='settings_images/')
    location = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    etitle = models.CharField(max_length=50)
    service_hours = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Site Settings'

    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings,self).save(*args,**kwargs)

    def __str__ (self):
        return "Setting"    