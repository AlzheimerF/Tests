from django import forms
from .models import TestSet, Questions_and_answers

class CreateQA(forms.ModelForm):

    class Meta:
        model = Questions_and_answers
        fields = '__all__'

class CreateTestSet(forms.ModelForm):

    class Meta:
        model = TestSet
        fields = '__all__'

