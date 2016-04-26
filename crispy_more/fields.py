from crispy_forms.layout import Field
from crispy_forms.utils import TEMPLATE_PACK
from django.template import Template
from django.utils.six import text_type


class JS(Field):
    template = "%s/layout/javascript_tag.html"

class JS(object):
    def __init__(self, html):
        self.html = '''<script type="text/javascript">%s</script>''' % html

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        return Template(text_type(self.html)).render(context)

class CrispyMoreField(Field):
    def __init__(self, form, *args, **kwargs):
        kwargs['css_class'] = 'crispy-more-chosen'
        self._form = form
        self.add_media()
        super().__init__(*args, **kwargs)

    def add_media(self):
        for i in self.Media.css:
            self._form.Media.css['all'].append(i)
        for i in self.Media.js:
            self._form.Media.js.append(i)

    class Media:
        css = []
        js = []

class MultiChosenField(CrispyMoreField):
    template = "%s/layout/multichosen.html"

    class Media:
        css = ['//cdn.bootcss.com/chosen/1.4.2/chosen.min.css']
        js = ['//cdn.bootcss.com/chosen/1.4.2/chosen.jquery.min.js']

    def __init__(self, *args, **kwargs):
        kwargs['css_class'] = 'crispy-more-chosen'
        args = list(args) + [JS('$(".crispy-more-chosen").chosen();')]
        super().__init__(*args, **kwargs)
