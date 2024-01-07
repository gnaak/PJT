from django.db import models


AGE_CHOICES = [
    ('20-24', '20~24세'),
    ('25-29', '25~29세'),
    ('30-34', '30~34세'),
    ('35-39', '35~39세'),
    ('40-44', '40~44세'),
    ('45-49', '45~49세'),
    ('50-54', '50~54세'),
    ('55-59', '55~59세'),
    ('60+', '60세 이상'),
]

GENDER_CHOICES = [
    ('male', '남성'),
    ('female', '여성'),
    ('other', '기타'),
]

FINANCIAL_GOAL_CHOICES = [
    ('savings', '적금'),
    ('investment', '투자'),
    ('retirement', '은퇴 준비'),
    ('education', '교육 자금 마련'),
    ('other', '기타'),
]

CURRENT_PRODUCTS=[
    ('savings_account', '적금'),
    ('fixed_deposit', '예금'),
    ('investment_fund', '투자 펀드'),
    ('retirement_account', '연금 계좌'),
    ('credit_card', '신용카드'),
    ('other', '기타'),
]

class Survey(models.Model):
    full_name = models.CharField(max_length=100)
    ages = models.CharField(max_length=5, choices=AGE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    additional_income = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2)
    financial_goals = models.CharField(max_length=20, choices=FINANCIAL_GOAL_CHOICES)
    risk_tolerance = models.CharField(max_length=10)  # 'low', 'medium', 'high'
    current_financial_products = models.CharField(max_length=20, choices=CURRENT_PRODUCTS)
    satisfaction_level = models.CharField(max_length=20)  # 'very_satisfied', 'satisfied', ...
    financial_advice_needed = models.BooleanField(default=False)
    # 다른 필드들도 추가...

    def __str__(self):
        return self.full_name
