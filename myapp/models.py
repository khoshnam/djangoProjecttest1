from django.db import models

from django.db import models
from django_jalali.db import models as jmodels
import jdatetime

class Contracts(models.Model):
    province = models.CharField(max_length=100, blank=True, null=True, verbose_name='شعبه صدور قرارداد')
    policyholder = models.CharField(max_length=100, blank=True, null=True, verbose_name='بیمه گزار')
    template_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='شماره الگوی قرارداد')
    contract_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='شماره قرارداد')
    rasa_contract_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='شماره قرارداد سامانه')
    start_contract_date = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ شروع قرارداد')
    end_contract_date = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ پایان قرارداد')
    profile_type = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام پروفایل')
    premium = models.IntegerField(blank=True, null=True, verbose_name='حق بیمه')
    population = models.IntegerField(blank=True, null=True, verbose_name='جمعیت بیمه‌شدگان')
    is_active_contract = models.BooleanField(verbose_name='وضعیت فعال/غیر فعال', default=True)

    def total_collected_premium(self):
        # محاسبه مجموع مبلغ‌های وصول‌شده برای این قرارداد
        total_collected = self.premium_collections.aggregate(total=models.Sum('amount_collected'))['total'] or 0
        return total_collected

    def __str__(self):
        return self.contract_number

    def __str__(self):
        return f'{self.policyholder} - {self.contract_number}'

    class Meta:
        verbose_name = 'قرارداد'
        verbose_name_plural = 'قراردادها'


class PremiumCollection(models.Model):
    contract = models.ForeignKey(Contracts, related_name='premium_collections', on_delete=models.CASCADE)
    amount_collected = models.IntegerField(verbose_name='مقدار حق بیمه وصول‌شده')
    collection_date = jmodels.jDateField(auto_now_add=True,blank=True, null=True, verbose_name='تاریخ وصول اتوماتیک')
    collection_date1 = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ وصول')




    def __str__(self):
        return f'{self.contract.contract_number} - {self.amount_collected}'

    class Meta:
        verbose_name = 'وصول حق بیمه'
        verbose_name_plural = 'وصول‌های حق بیمه'

