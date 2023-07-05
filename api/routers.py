from api .views import KnowledgeViewset

from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register(r"crm", KnowledgeViewset, basename="crud operations")



urlpatterns = [
    *router.urls,
]
