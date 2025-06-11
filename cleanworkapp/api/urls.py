from django.urls import path
from cleanworkapp.api import views


urlpatterns = [
    path('banner-list-create/', views.BannerListCreateAPIView.as_view()),
    path('banner-retrieve-update/<int:id>/', views.BannerRetrieveUpdateAPIView.as_view()), 
    path('banner-delete/', views.BannerDestroyAPIView.as_view()),
    
    path('service-list/',views.ServiceListaAPIView.as_view()),
    path('service-retrieve/<int:id>/',views.ServiceRetrieveAPIView.as_view()), 
    
    path('galery-list/',views.GalleryListaAPIView.as_view()), 
    path('galery-retrieve/<int:id>/',views.GalleryRetrieveAPIView.as_view()), 
    path('galery-create/',views.GalleryCreateAPIView.as_view()),
    path('galery-update/',views.GalleryUpdateAPIView.as_view()),
    path('galery-delete/',views.GalleryDestroyAPIView.as_view()),
    
    path('customers-list/',views.CustomersListaAPIView.as_view()),
    path('customers-retrieve/<int:id>/',views.CustomersRetrieveAPIView.as_view()), 
    path('customers-create/',views.CustomersCreateAPIView.as_view()),
    path('customers-update/',views.CustomersUpdateAPIView.as_view()),
    path('customers-delete/',views.CustomersDestroyAPIView.as_view()),
    
    path('companies-list/',views.CompaniesListaAPIView.as_view()),
    path('companies-retrieve/<int:id>/',views.CompaniesRetrieveAPIView.as_view()), 
    path('companies-create/',views.CompaniesCreateAPIView.as_view()),
    path('companies-update/',views.CompaniesUpdateAPIView.as_view()),
    path('companies-delete/',views.CompaniesDestroyAPIView.as_view()),
    
    path('sitesettings-list/', views.SiteSettingsListAPIView.as_view()),
    path('sosialmedia-list/', views.SosialMediaListaAPIView.as_view()),
   
    
]
