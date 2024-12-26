from django import forms
from .models import Contracts,PremiumCollection
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class TestForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = ('province', 'start_contract_date','contract_number')

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['start_contract_date'] = JalaliDateField(label=('start_contract_date'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

class PremiumCollectionForm(forms.ModelForm):
    class Meta:
        model = PremiumCollection
        fields = ['contract', 'amount_collected','collection_date1']

    def __init__(self, *args, **kwargs):
        super(PremiumCollectionForm, self).__init__(*args, **kwargs)
        self.fields['collection_date1'] = JalaliDateField(label=('collection_date1'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        if not self.instance.pk:  # هنگام ایجاد یک شیء جدید
            self.fields['contract'].empty_label = 'انتخاب قرارداد'  # یا هر عنوان دلخواهی
