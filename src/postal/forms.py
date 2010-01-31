from django import forms
from django.utils.translation import ugettext_lazy as _

from models import PostalAddress

class PostalAddressForm(forms.ModelForm):
    line1 = forms.CharField(label=_(u"Company name"), required=False, max_length=100)
    line2 = forms.CharField(label=_(u"Street"), required=False, max_length=100)
    line3 = forms.CharField(label=_(u"Zip Code"), required=False, max_length=100)
    line4 = forms.CharField(label=_(u"City"), required=False, max_length=100)
    line5 = forms.CharField(label=_(u"State"), required=False, max_length=100)

    class Meta:
        model = PostalAddress
        


