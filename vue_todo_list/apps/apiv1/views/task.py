from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from task.models import Task, SubTask, Repository
from users.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from task.serializers import TaskSerializer, RepositorySerializer

class TaskListCreateView(ListCreateAPIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.user)

        # print(request.data)
        # return Response({'data':'success'}, status=200)
        
        try:
            task_id = request.data['id']
            task = Task.objects.get(id=task_id)
            task.name=request.data['task']
            task.notes=request.data['notes']
            task.complete=request.data['task_checked']
            task.save()

            for sub in request.data['sub_tasks']:
                sub_id = sub['id']
                sub_task = SubTask.objects.get(id=sub_id)
                sub_task.name=sub['title']
                sub_task.complete=sub['checked']
                sub_task.save()
            return Response({'data':'success'}, status=200)  
            
        except:
            task = Task.objects.create(
                user=user,
                # repository=
                name=request.data['task'],
                notes=request.data['notes'],
                complete=request.data['task_checked']
            )
            for i in range(0,len(request.data['sub_tasks'])):

                sub_task = SubTask.objects.create(
                    task=task,
                    name=request.data['sub_tasks'][i]['title'],
                    complete=request.data['sub_tasks'][i]['checked'],
                )
            return Response({'data':'success'}, status=200)    
            

class TaskDeleteUpdateView(RetrieveUpdateDestroyAPIView):

    def patch(self, request, *args, **kwargs):

        print(request.data['complete'])
        print(request.data['id'])

        task = Task.objects.get(id=request.data['id'])
        task.complete=request.data['complete']
        task.save()
        return Response({'detail':'success'},status=200)
    
    def delete(self, request, *args, **kwargs):

        pk = self.kwargs.get('task_id')

        Task.objects.get(id=pk).delete()

        return Response({'detail':'success'},status=200)


class RepositoryListCreateView(ListCreateAPIView):
    serializer_class = RepositorySerializer
    
    
    def get_queryset(self):
    
        user = self.request.user
        return Repository.objects.filter(user=user)
    

    def post(self, request, *args, **kwargs):
        
        user = User.objects.get(username=self.request.user)

        Repository.objects.create(
            user=user, 
            name=request.data['name']
        )
        
        return Response({'detail':'success'},status=200)




