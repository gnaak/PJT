from rest_framework import serializers
from .models import SavingProducts, SavingOptions

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionSerializer(serializers.ModelSerializer):
    class SavingProductsSerializer(serializers.ModelSerializer):
        class Meta:
            model = SavingProducts
            fields = '__all__'
    # product = DepositProductsSerializer(read_only=True)
    # product = DepositProductsSerializer()

    class Meta:
        model = SavingOptions
        fields = '__all__'
