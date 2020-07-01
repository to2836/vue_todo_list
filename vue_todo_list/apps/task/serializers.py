
from rest_framework import serializers
from task.models import Task, SubTask, Repository
import json

class TaskSerializer(serializers.ModelSerializer):

    sub_task = serializers.SerializerMethodField()
    
    def get_sub_task(self, item):
        result=[]
        sub_task = SubTask.objects.filter(task=item.id)
        for obj in sub_task:
            result.append({'id':obj.id,'name':obj.name, 'complete':obj.complete})
        return result
    
    class Meta:
        model = Task
        fields = '__all__'

class RepositorySerializer(serializers.ModelSerializer):
    
    task_cnt = serializers.SerializerMethodField()

    def get_task_cnt(self, item):
    
        return Task.objects.filter(id=item.id).count()

    class Meta:
        model = Repository
        fields = '__all__'

