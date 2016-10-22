from io import BytesIO

from django.core.files.images import ImageFile

import requests
from avatar.models import Avatar


def get_username(strategy, details, response, user=None, *args, **kwargs):
    storage = strategy.storage

    if not user:
        username = details['email']
    else:
        username = storage.user.get_username(user)
    return {'username': username}


def set_avatar(is_new, backend, user, response, *args, **kwargs):
    if not is_new:
        return

    image_url = None
    image_params = {}

    if backend.name == 'facebook':
        image_url = 'https://graph.facebook.com/v2.8/me/picture'
        image_params = {'type': 'large', 'access_token': response['access_token']}

    if image_url:
        response = requests.get(image_url, params=image_params)
        image = BytesIO(response.content)
        Avatar.objects.create(user=user, primary=True, avatar=ImageFile(image, name='pic.jpg'))
