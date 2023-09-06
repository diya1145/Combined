from django.contrib import admin
from django.http import HttpResponse
from .models import Post,Category,Tags,Comment,User
from import_export.admin import ImportExportMixin


admin.site.register(User)



class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "category",'image')
    list_filter = ('author','category','image')
    
admin.site.register(Post,PostAdmin)


# class RegisterAdmin(admin.ModelAdmin):
#     list_display = ("username", "email",'password')
#     list_filter = ('username','email','password')


# admin.site.register(RegistrationForm,RegisterAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post",'body','reply')
    list_filter = ('author','post','body','reply')
   
admin.site.register(Comment,CommentAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "text")
    list_filter = ('name','text')

admin.site.register(Category,CategoryAdmin)


class TagAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("name", "text")
    list_filter = ('name','text')
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename="your_model_data.csv"'

        writer = csv.writer(response)
        writer.writerow(['name', 'text'])  # Add more field names here

        for obj in queryset:
            writer.writerow([obj.name, obj.text])  # Add more fields as needed

        return response

    export_to_csv.short_description = "Export selected items to CSV"

admin.site.register(Tags,TagAdmin)

    