from django.db.models import Sum
from django.db.models import Prefetch
from django.views.generic import CreateView
from .models import Contracts, PremiumCollection
from .forms import PremiumCollectionForm, TestForm

class ContractsCreateView(CreateView):
    model = Contracts
    form_class = TestForm
    template_name = 'myapp/TEMPLATE_NAME.html'
    success_url = "/"  # پس از ذخیره به لیست قراردادها هدایت می‌شود

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # result22 = Contracts.objects.annotate(
        #     total_collected=Sum('premium_collections__amount_collected')
        # ).values(
        #     'contract_number',  # شماره قرارداد
        #     'province',  # استان
        #     'premium',  # حق بیمه
        #     'premium_collections__collection_date__year',  # سال وصول
        #     'premium_collections__collection_date__month'  # ماه وصول
        # ).order_by('contract_number', 'premium_collections__collection_date__year',
        #            'premium_collections__collection_date__month')
        result23 = Contracts.objects.annotate(
            total_collected1=Sum('premium_collections__amount_collected')
        ).values(
            'contract_number',  # شماره قرارداد
            'province',  # استان
            'premium',  # حق بیمه
            'population',
            'premium_collections__collection_date1',  # سال وصول
            'premium_collections__amount_collected',  # مبلغ وصول‌شده

        ).order_by('contract_number', 'premium_collections__collection_date1')

        # دریافت تمام قراردادها همراه با پرداخت‌های حق بیمه
        contracts = Contracts.objects.prefetch_related(
            Prefetch('premium_collections', queryset=PremiumCollection.objects.all())
        )

        # دریافت مجموع مبلغ‌های وصول‌شده به تفکیک قرارداد
        result = contracts.annotate(
            total_collected=Sum('premium_collections__amount_collected')
        )

        # محاسبه مجموع مبلغ‌های وصول‌شده برای هر قرارداد
        contract_totals = []
        for contract in contracts:
            total_collected = contract.premium_collections.aggregate(total=Sum('amount_collected'))['total'] or 0
            contract_totals.append({
                'contract': contract,
                'total_collected': total_collected
            })
        #
        # # محاسبه مبلغ وصول‌شده به تفکیک ماه برای هر قرارداد
        # contract_monthly_totals = []
        # for contract in contracts:
        #     monthly_collections = contract.premium_collections.values('collection_date__year', 'collection_date__month').annotate(
        #         monthly_amount=Sum('amount_collected')
        #     ).order_by('collection_date__year', 'collection_date__month')
        #
        #     contract_monthly_totals.append({
        #         'contract': contract,
        #         'monthly_collections': monthly_collections
        #     })

        # افزودن داده‌ها به context
        context['contract_totals'] = contract_totals
        # context['contract_monthly_totals'] = contract_monthly_totals
        context['result'] = result  # نتیجه نهایی برای تفکیک استان، قرارداد و تاریخ
        # context['result22'] = result22
        context['result23'] = result23


        return context


class PremiumCollectionCreateView(CreateView):
    model = PremiumCollection
    form_class = PremiumCollectionForm
    template_name = 'myapp/premium_collection_create.html'
    success_url = "/"  # پس از ذخیره به لیست وصول‌های حق بیمه هدایت می‌شود
