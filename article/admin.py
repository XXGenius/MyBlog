from django.contrib import admin
from article.models import Article, Comments, Category

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'id')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name' ,'id')




admin.site.register(Article, ArticleAdmin)	

admin.site.register(Category,CategoryAdmin)






