from django.contrib import admin
from task.models import Repository, Task, SubTask

class RepositoryAdmin(admin.ModelAdmin):

    list_display = ['name']


class TaskAdmin(admin.ModelAdmin):
    
    list_display = ['name','complete']


class SubTaskAdmin(admin.ModelAdmin):
    
    list_display = ['name','complete']

admin.site.register(Repository, RepositoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)