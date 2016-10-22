'''
isort:skip_file
'''

from django.conf.urls import include, url

from .routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

# Login / Register
# from .login.views import LoginViewSet  # noqa
# from .social_auth.views import SocialAuthViewSet  # noqa

# router.register(r'login', LoginViewSet, base_name='login')
# router.register(r'social-auth', SocialAuthViewSet, base_name='social-auth')

# # Users
# from .users.views import UsersViewSet  # noqa

# router.register(r'users', UsersViewSet, base_name='users')

urlpatterns = [
    url(r'v1/', include(router.urls, namespace='v1')),
]
