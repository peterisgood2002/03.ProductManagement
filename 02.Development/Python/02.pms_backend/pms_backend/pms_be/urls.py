from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cnn5", views.getCNN5Things, name="cnn5"),
    path("test", views.testDB, name="test"),
    path("addPlatform", views.addPlatform, name="addPlatform"),
    path("addCustomer", views.addCustomer, name="addCustomer"),
    path("addProject", views.addProject, name="addProject"),
    path("addMilestone", views.addMilestone, name="addMilestone"),
]
