from django.contrib import admin
from django.http import HttpResponse
from .models import Post,Category,Tags,Comment,User
from import_export.admin import ImportExportMixin


admin.site.register(User)



class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "category",'image')
    list_filter = ('author','category','image')
    view_on_site = True
admin.site.register(Post,PostAdmin)



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

        writer = csv.writer(response)
        writer.writerow(['name', 'text']) 

        for obj in queryset:
            writer.writerow([obj.name, obj.text]) 
        return response

    export_to_csv.short_description = "Export selected items to CSV"

admin.site.register(Tags,TagAdmin)

# def view_on_site_link(modeladmin, request, queryset):
#     if queryset.count() == 1:
#         post = queryset.first()
#         url = reverse('post/<int:pk>/', args=[post.pk])  # Replace 'post_detail_url_name' with the actual URL name for your post detail view
#         return format_html('<a href="{}" target="_blank">View on site</a>', url)
#     else:
#         return format_html('<p>Select only one post to view on site.</p>')

# view_on_site_link.short_description = "View on Site"
