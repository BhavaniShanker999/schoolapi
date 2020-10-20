from rest_framework import routers
from django.urls import path,include
from .  import views

router=routers.DefaultRouter()
router.register('Schoolinfo',views.schoolview)
router.register('Staffinfo',views.staffview)

urlpatterns = [
    path('', include(router.urls)),
]