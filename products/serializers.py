from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item

# class ItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50)
#     have_sale = serializers.BooleanField(default=False)
#     discount = serializers.FloatField(default = 0.0)

#     def create(self,validated_data):
#         return Item.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.have_sale = validated_data.get('have_sale',instance.have_sale)
#         instance.discount = validated_data.get('discount',instance.discount)
#         instance.save()

#         return instance
class UserSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedIdentityField(many=True, view_name='item-detail',read_only=True)

    class Meta:
        model = User
        fields = ('url','id', 'username', 'items')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    price_afte_sale = serializers.ReadOnlyField()
    num = serializers.ReadOnlyField()
    class Meta:
        model = Item
        fields = ('url','id','name','num','owner','price','have_sale','discount','price_afte_sale')

