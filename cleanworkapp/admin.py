from django.contrib import admin
from cleanworkapp.models import Banner, Service, Servicetag , Gallery, Customers, Companies, SiteSettings, SosialMedia


admin.site.register(Banner)
admin.site.register(Service)
admin.site.register(Gallery)
admin.site.register(Servicetag)
admin.site.register(Customers)
admin.site.register(Companies)
admin.site.register(SiteSettings)
admin.site.register(SosialMedia)