from django.contrib import admin
from .models import Customer
# pip import-export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# Register your models here.

class CustomerResource(resources.ModelResource):
    additional_info = Field()
    registered = Field()
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'phone', 'rating', 'books', 'book_count') # aditional_info and registered, was added automatically at the end of the fields
        export_order = fields 
    
    def dehydrate_registered(self, obj):
        return obj.registered.strftime("%d/%m/%y")

    def dehydrate_additional_info(self, obj):
        if len(obj.additional_info) == 0:
            return "-"
        elif len(obj.additional_info) < 5:
            return obj.additional_info
        else:
            txt_list = obj.additional_info.split(" ")[:5]
            return " ".join(txt_list) + "..."

class CustomerAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = CustomerResource

admin.site.register(Customer, CustomerAdmin)