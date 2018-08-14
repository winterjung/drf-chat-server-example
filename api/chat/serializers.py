from django.contrib.auth.models import User
from rest_framework import serializers

from api.chat.models import Message, Room


class GetUserMixin:
    def get_user_from_request(self):
        request = self.context.get('request')
        if not request:
            return None
        if not hasattr(request, 'user'):
            return None
        return request.user


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoomSerializer(GetUserMixin, serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Room
        fields = ('id', 'title', 'participants')

    def validate_participants(self, value):
        user = self.get_user_from_request()
        if not user:
            return value

        if user not in value:
            raise serializers.ValidationError('User must be in participants.')
        return value


class MessageSerializer(GetUserMixin, serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), write_only=True)

    class Meta:
        model = Message
        fields = ('id', 'content', 'sender', 'room', 'created_at')

    def validate_sender(self, value):
        user = self.get_user_from_request()
        if not user:
            return value

        if user.id != value.id:
            raise serializers.ValidationError('User must be same with sender.')
        return value

    def validate_room(self, value):
        user = self.get_user_from_request()
        if not user:
            return value

        if not user.room_set.filter(id=value.id):
            raise serializers.ValidationError('User must be in room.')

        url_room_pk = self.context.get('view').kwargs.get('parent_lookup_room')
        if int(url_room_pk) != value.id:
            raise serializers.ValidationError('Room must be same with room of url.')
        return value
