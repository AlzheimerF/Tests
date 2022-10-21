from django.urls import path
from . import views

urlpatterns = [
    path('list_test/', views.list_test, name='list_'),
    path('list_qa/', views.list_qa, name='list_qa'),
    path('test/<int:id>/', views.use_test, name='use_test'),
    path('test_au/<int:id>/', views.use_test_au, name='use_test_au'),
    path('create_test_set/', views.add_test_set, name='create_test'),
    path('create_answer_and_question/', views.add_answer_and_question, name='create_answer_and_question'),
    path('list_of_users/', views.list_of_users, name='list_u'),
    path('delete_qa/<int:id>/', views.delete_qa, name='delete_qa'),
    path('delete_test/<int:id>/', views.delete_test, name='delete_test'),
]