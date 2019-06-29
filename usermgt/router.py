from rest_framework import routers
from . import apis

router = routers.DefaultRouter()
router.register(r'users', apis.UserViewSet)
router.register(r'profiles', apis.ProfileViewSet)
router.register(r'groups', apis.GroupViewSet)
router.register(r'questions', apis.QuestionViewSet)