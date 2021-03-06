from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class PermissionsMixin(models.Model):
    '''
    A mixin class that adds the fields and methods necessary to support
    Django's Permission model using the ModelBackend.
    '''
    is_superuser = models.BooleanField(
        _('superuser status'), default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.')
    )

    class Meta:
        abstract = True

    def has_perm(self, perm, obj=None):
        '''
        Returns True if the user is superadmin and is active
        '''
        return self.is_active and self.is_superuser

    def has_perms(self, perm_list, obj=None):
        '''
        Returns True if the user is superadmin and is active
        '''
        return self.is_active and self.is_superuser

    def has_module_perms(self, app_label):
        '''
        Returns True if the user is superadmin and is active
        '''
        return self.is_active and self.is_superuser

    @property
    def is_staff(self):
        return self.is_superuser


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    # Profile
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_full_name()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username
