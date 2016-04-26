# django-crispy-more

Example:
Assuming that your app names "myapp"

View: (`myapp/views.py`)
```python
from django.views.generic import FormView

from crispy_example.forms import SimpleForm


class Index1View(FormView):
    template_name = 'myapp/index.html'
    form_class = SimpleForm
```

Template: (`myapp/templates/myapp/index.html`)
```html
{% load crispy_forms_tags %}
{% load staticfiles %}
<!DOCTYPE html>
<html>
    <head>
        {{ form.media }}
    </head>
    <body>
        <div class="container">
            <div class="row">
                {% crispy form %}
            </div>
        </div>
    </body>
</html>
```

Model: (`myapp/models.py`)
```python
from django.db import models


class Cigar(models.Model):
    name = models.CharField(max_length=255)

class Smoker(models.Model):
    name = models.CharField(max_length=255)
    best_friend = models.ForeignKey('myapp.Smoker')
    cigar = models.ManyToManyField(Cigar)
```

Form: (`myapp/forms.py`)
```python
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_more.fields import MultiChosenField
from .models import Smoker
from crispy_more.forms import ModelForm

class SimpleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SimpleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            MultiChosenField(self, 'cigar')
        )

    class Meta:
        model = Smoker
        fields = '__all__'
```