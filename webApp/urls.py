from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^submit/expence/$',views.submit_expence,name="submit_expence")
    path('submit/expence/',views.submit_expence,name="submit_expence"),
]
