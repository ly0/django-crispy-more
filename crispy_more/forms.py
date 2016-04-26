from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms
from crispy_more.fields import MultiChosenField
from myapp.models import Smoker

class Form(forms.Form):
    class Media:
        css = {
            'all': [
                '//cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css'
            ]
        }
        js = ['//cdn.bootcss.com/jquery/3.0.0-beta1/jquery.min.js']

class ModelForm(Form, forms.ModelForm):
    pass