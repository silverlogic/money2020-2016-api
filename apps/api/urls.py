'''
isort:skip_file
'''

from django.conf.urls import include, url

from .routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

# Login / Register
from .social_auth.views import SocialAuthViewSet  # noqa

router.register(r'social-auth', SocialAuthViewSet, base_name='social-auth')

# Users
from .users.views import UsersViewSet  # noqa

router.register(r'users', UsersViewSet, base_name='users')

# Vending Machines
from .vending_machines.views import VendingMachinesViewSet  # noqa

router.register(r'vending-machines', VendingMachinesViewSet, base_name='vending-machines')

# Approvals
from .approvals.views import ApprovalCreateViewSet, ApprovalUpdateViewSet  # noqa

router.register(r'approval-create', ApprovalCreateViewSet, base_name='approval-create')
router.register(r'approval-update', ApprovalUpdateViewSet, base_name='approval-update')

urlpatterns = [
    url(r'v1/', include(router.urls, namespace='v1')),
]
