from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView 
from cleanworkapp.models import Banner,Service, Gallery,  Customers, Companies,  SosialMedia, SiteSettings
from cleanworkapp.api.serializers import ( BannerSerializers , BannerRetrieveSerializer,
        ServiceSerializer, GallerySerializer, ServiceRetrieveSerializer, CustomersSerializer, CompaniesSerializer,
        SosialMediaSerializer, SiteSettingsSerializer, GalleryRetrieveSerializer, 
            
)


class BannerListCreateAPIView(ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers
    


    
    
class BannerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Banner.objects.all()
    serializer_class =BannerRetrieveSerializer
    lookup_field = "id"
    
    
    
class BannerRetrieveAPIView(RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerRetrieveSerializer
    lookup_field = "id"   
    
    
class BannerDestroyAPIView(DestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers
    lookup_field = "id"
    
    
class ServiceListaAPIView(ListAPIView):
    queryset =Service.objects.all()
    serializer_class = ServiceSerializer
    
class ServiceRetrieveAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceRetrieveSerializer
    lookup_field = "id"
    
    
class GalleryListaAPIView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    
class GalleryRetrieveAPIView(RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryRetrieveSerializer
    lookup_field = "id"
    
class GalleryCreateAPIView(CreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    
class GalleryUpdateAPIView(UpdateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = "id"
    
class GalleryDestroyAPIView(DestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = "id"
    
    
class CustomersListaAPIView(ListAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    
class CustomersRetrieveAPIView(RetrieveAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    lookup_field = "id"
    
class CustomersCreateAPIView(CreateAPIView):
    queryset =Customers.objects.all()
    serializer_class = CustomersSerializer
    
class CustomersUpdateAPIView(UpdateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    lookup_field = "id"
    
class CustomersDestroyAPIView(DestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    
    
class CompaniesListaAPIView(ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    
class CompaniesRetrieveAPIView(RetrieveAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    lookup_field = "id"
    
class CompaniesCreateAPIView(CreateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    lookup_field = "id"
    
class CompaniesUpdateAPIView(UpdateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    
class CompaniesDestroyAPIView(DestroyAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    lookup_field = "id"
    
    
class SosialMediaListaAPIView(ListAPIView):
    queryset = SosialMedia.objects.all()
    serializer_class = SosialMediaSerializer
    
    

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    

     

    
    
    
    
    

    
    
    
    
    