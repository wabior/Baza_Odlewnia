from django import forms

from .models import Machine, Production

class MachineForm(forms.ModelForm):
     class Meta:
         model = Machine
         fields = [
             'Code_Name',
             'Name',
             'Status',
             'Form_Forms',
             'Current_Shoots',
             'Total_Shoots',
         ]

class NowyRaport(forms.ModelForm):
    class Meta:
        model = Production
        fields = [
            'shift_date',
            'Machine',
            'Production_Value',
        ]
