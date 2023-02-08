from . import views
from django.urls import path

urlpatterns=[
    path('',views.add_task,name='task'),
    # path('delete/<int:task_id>/',views.delete,name='delete'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),

    path('cvbdetails/<int:pk>/',views.TaskDetailview.as_view(),name='cvbdetails'),
    path('cvbupadate/<int:pk>/',views.Taskupadateview.as_view(),name='cvbupadate'),
    path('cvbdelete/<int:pk>/',views.TaskeDeleteview.as_view(),name='cvbdelete')


]