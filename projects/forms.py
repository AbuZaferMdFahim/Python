from django.forms import ModelForm
from django import forms
from .models import Project,Review

class ProjectForm(ModelForm):
    class Meta():
        model = Project
        fields = ['title','featured_image','description','demo_link','source_link','tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **Kwargs):
        super(ProjectForm, self).__init__(*args, **Kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {
            'value': 'Place your Vote',
            'body' : 'Add a comment woth your vote'
        }
    def __init__(self, *args, **Kwargs):
        super(ReviewForm, self).__init__(*args, **Kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
