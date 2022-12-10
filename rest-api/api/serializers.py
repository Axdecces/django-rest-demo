from rest_framework import serializers

from api.models import User, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'number', 'postcode', 'city']

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)

        user = User.objects.create(address=address, **validated_data)
        return user

    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'birthday', 'address']