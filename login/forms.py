# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import DateInput, NumberInput, TextInput

from .models import EquipInfo

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=200)
    netimpv_file = forms.FileField()

class EquipInfoForm(ModelForm):
    class Meta:
        model = EquipInfo
        fields = '__all__'
        error_messages = {
            'serial_no': {
                'null': _(u"尚未输入任何字符，序列号不能为空，请输入！"),
                'blank': _(u"序列号不能为空，请输入！"),
                'invalid': _(u"此序列号无效，请重新输入!"),
                'unique': _(u"此序列号已存在!"),
                'required': _(u"序列号为必填项，请输入!"),
            },
        }
        widgets ={
            'app_name':TextInput(attrs={'size':50,'maxlength':255}),
            'app_module':TextInput(attrs={'size':35,'maxlength':100}),
            'app_proj':TextInput(attrs={'size':35,'maxlength':100}),
        }