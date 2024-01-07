from django.urls import path,include
from .views import CustomRegisterView, CustomUserDetailsView, CustomLoginView

# URL 순서 때문에 CustomUserDetailsView 동작 안했음
urlpatterns = [
    path('signup/', CustomRegisterView.as_view(), name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='account_login'),
    path('user/', CustomUserDetailsView.as_view(), name='account_userinfo'),
    path('signup/', include('dj_rest_auth.registration.urls')), # 라이브러리
    path('', include('dj_rest_auth.urls')), # 라이브러리
]