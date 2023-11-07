from django.contrib import admin
from .models import Publisher
# pip import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# Register your models here.

class PublisherResource(resources.ModelResource):
    date = Field()
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'country', 'date')
        export_order = ( 'id', 'name', 'country', 'date')
    
    def dehydrate_date(self, obj):
        return obj.created.strftime("%d/%m/%y")

class PublisherAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PublisherResource

admin.site.register(Publisher, PublisherAdmin)