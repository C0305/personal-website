from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'name',
            'subject',
            'email',
            'message'
        ]

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', css_class="input-field"),
        Field('subject', css_class="input-field"),
        Field('email', css_class="input-field", type="textarea"),
        Field('message', css_class="input-field"),
        Submit('submit', 'Submit', css_class='submit', css_id='submit-btn')
    )
