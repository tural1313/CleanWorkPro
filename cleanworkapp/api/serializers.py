from rest_framework import serializers
from cleanworkapp.models import Banner, Service, Gallery , Customers, Companies, SosialMedia, SiteSettings



class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields= '__all__'
        # exclude = ('id',)
        
        
class BannerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Banner
        fields = "__all__"
        
        

        
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ('content',)
        
        
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ( 'image',)
        
        
class ServiceRetrieveSerializer(serializers.ModelSerializer):
    photos = GallerySerializer(many=True)
    related_services = serializers.SerializerMethodField()
    class Meta:
        model =Service
        fields = "__all__"
        
    def get_related_services(self,obj):
        return Service.objects.filter(
            tags__in = obj.tags.all()
        )
    
        
class GalleryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields= ('id',)
        
        
class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"

class CustomersRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        exclude = ('id',)

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields ="__all__"
        
class CompaniesRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('id',)
        
        
class SosialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SosialMedia
        fields = ('id',)
    
        
        
class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ('id',)
        
        
        
        
        
