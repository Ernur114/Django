from django.contrib import admin
from posts.models import Posts , Images, Categories
# Register your models here.

@admin.register(Posts)
class ClientAdmin(admin.ModelAdmin):
    model = Posts
    list_display = (

        "title",
        "description",
        "date_publication",
        "user",
    )
    list_filter = ("title", "date_publication", "user")
    search_fields = ("title", "user")


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    model = Images
    list_display = ("post", "Image")
    list_filter = ("post",)
    search_fields = ("post",)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    model = Categories
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("title",)