from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

# 로그인 할 때 이메일 제외
class CustomLoginSerializer(LoginSerializer):
    email = None

# 회원가입 시 사용자로부터 입력받을 정보
class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    age = serializers.IntegerField(required=False)
    phoneNo = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', ''),
            'phoneNo': self.validated_data.get('phoneNo', ''),
            'money': self.validated_data.get('money', ''),
            'salary': self.validated_data.get('salary', ''),
            'financial_products': self.validated_data.get('financial_products', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        user.nickname = self.cleaned_data.get('nickname', '')
        user.age = self.cleaned_data.get('age', '')
        user.money = self.cleaned_data.get('money', '')
        print(f'money: {user.money}')  # Add this line for logging
        user.salary = self.cleaned_data.get('salary', '')
        user.phoneNo = self.cleaned_data.get('phoneNo', '')
        # user.financial_products = self.cleaned_data.get('financial_products', '')
        user.save()
        # print(f'Nickname: {user.nickname}')  # Add this line for logging
        return user

# 커스텀 유저 디테일
# 유저 정보 확인 (로그인 후 발급받는 토큰 필요)
# 아래에 보여줄 정보를 수정할 수 있음
class CustomUserDetailsSerializer(UserDetailsSerializer):
    
    age = serializers.IntegerField(required=False)
    phoneNo = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    phoneNo = serializers.IntegerField(required=False)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
    )
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('age', 'money', 'salary', 'nickname', 'phoneNo', 'financial_products' )
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()

        data_dict['age'] = self.validated_data.get('age', None)
        data_dict['money'] = self.validated_data.get('money', None)
        data_dict['salary'] = self.validated_data.get('salary', None)
        data_dict['nickname'] = self.validated_data.get('nickname', None)
        data_dict['phoneNo'] = self.validated_data.get('phoneNo', None)
        data_dict['financial_products'] = self.validated_data.get('financial_products', None)
        
        return data_dict
    
    def update(self, instance, validated_data):
            
        instance = super().update(instance, validated_data)
        # instance.username = validated_data.get('username', None)
        instance.age = validated_data.get('age', None)
        instance.money = validated_data.get('money', None)
        instance.salary = validated_data.get('salary', None)
        instance.nickname = validated_data.get('nickname', None)
        instance.phoneNo = validated_data.get('phoneNo', None)
        instance.financial_products = validated_data.get('financial_products', None)
        instance.save()
        return instance
    
    def save(self):
        # self.validated_data.pop('username', None)
        user = super().save()
        user.age = self.validated_data.get('age', None)
        user.gender = self.validated_data.get('money', None)
        user.salary = self.validated_data.get('salary', None)
        user.nickname = self.validated_data.get('nickname', None)
        user.phoneNo = self.validated_data.get('phoneNo', None)
        user.financial_products = self.validated_data.get('financial_products', None)
        user.save()
        return user