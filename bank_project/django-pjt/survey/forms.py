from django import forms
from .models import Survey, AGE_CHOICES, CURRENT_PRODUCTS, FINANCIAL_GOAL_CHOICES, GENDER_CHOICES

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'
        
    ages = forms.ChoiceField(
        label='나이',
        choices=AGE_CHOICES,
        widget=forms.RadioSelect,
    )


    gender = forms.ChoiceField(
        label='성별',
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
    )

    monthly_income = forms.DecimalField(label='월 소득')
    additional_income = forms.DecimalField(label='기타 소득')

    # 지출 정보
    monthly_expenses = forms.DecimalField(label='월 지출')
    debt_amount = forms.DecimalField(label='현재 부채')

    # 금융 목표
    financial_goals = forms.ChoiceField(
        label='금융 목표',
        choices=FINANCIAL_GOAL_CHOICES,
        widget=forms.RadioSelect,
    )

    # 위험 허용 수준
    risk_tolerance = forms.ChoiceField(
        label='위험 허용 수준',
        choices=[('low', '낮음'), ('medium', '보통'), ('high', '높음')],
    )

    current_financial_products = forms.ChoiceField(
        label='현재 보유 중인 금융 상품',
        choices=CURRENT_PRODUCTS,
        widget=forms.RadioSelect,
    )

    # 금융 상품 만족도
    satisfaction_level = forms.ChoiceField(
        label='현재 보유 중인 금융 상품에 대한 만족도',
        choices=[
            ('very_satisfied', '매우 만족함'),
            ('satisfied', '만족함'),
            ('neutral', '보통'),
            ('dissatisfied', '불만족함'),
            ('very_dissatisfied', '매우 불만족함'),
        ],
    )

    # 추가적인 금융 상담 희망 여부
    financial_advice_needed = forms.BooleanField(
        label='추가적인 금융 상담을 받고 싶으신가요?',
        required=False,
    )