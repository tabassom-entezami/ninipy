from django.urls import include, path, re_path
from rest_framework import routers
from . import views
from .views import *

router = routers.DefaultRouter()
#to create and easy use
router.register(r'one', views.ProductOneViewset)
router.register(r'two', views.ProductTwoViewset)
router.register(r'three', views.ProductThreeViewset)
router.register(r'brand', views.BrandViewset)
router.register(r'category', views.CategoryViewset)
# what you asked

urlpatterns = [
    path('', include(router.urls)),
    # return with name of brand can use for id too
    re_path('^first/(?P<name>.+)/$', ProductOneAsked.as_view()),
    re_path('^first/(?P<name>.+)/$', ProducttwoAsked.as_view()),
    re_path('^first/(?P<name>.+)/$', ProductthreeAsked.as_view()),

]
