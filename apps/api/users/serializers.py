from avatar.models import Avatar

from apps.api.serializers import ModelSerializer
from apps.users.models import User

from .fields import AvatarField


class UserBaseSerializer(ModelSerializer):
    avatar = AvatarField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'avatar', 'first_name', 'last_name',)
        private_fields = ('username',)
        read_only_fields = ('username',)


class UserSerializer(UserBaseSerializer):
    class Meta(UserBaseSerializer.Meta):
        pass

    def update(self, instance, validated_data):
        if 'avatar' in validated_data:
            avatar = validated_data.pop('avatar')
            if avatar:
                Avatar.objects.create(user=instance, primary=True, avatar=avatar)
            else:
                instance.avatar_set.all().delete()
        return super().update(instance, validated_data)

    def to_representation(self, user):
        request = self.context['request']
        if request.user.is_authenticated() and request.user.pk == user.pk:
            return super().to_representation(user)
        else:
            return UserPublicSerializer(user).data


class UserPublicSerializer(UserBaseSerializer):
    class Meta(UserSerializer.Meta):
        fields = tuple(set(UserSerializer.Meta.fields) - set(UserSerializer.Meta.private_fields))
        read_only_fields = tuple(set(UserSerializer.Meta.read_only_fields) - set(UserSerializer.Meta.private_fields))
