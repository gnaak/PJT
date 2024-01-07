from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionSerializer(serializers.ModelSerializer):
    class DepositProductsSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositProducts
            fields = '__all__'
    # product = DepositProductsSerializer(read_only=True)
    # product = DepositProductsSerializer()

    class Meta:
        model = DepositOptions
        fields = '__all__'
