from crispy_forms.layout import Field
from crispy_forms.utils import TEMPLATE_PACK
from django.template import Template
from django.template.loader import render_to_string
from django.utils.six import text_type


class JS(Field):
    template = "%s/layout/javascript_tag.html"

class JS(object):
    """
    Layout object. It can contain pure HTML and it has access to the whole
    context of the page where the form is being rendered.

    Examples::

        HTML("{% if saved %}Data saved{% endif %}")
        HTML('<input type="hidden" name="{{ step_field }}" value="{{ step0 }}" />')
    """

    def __init__(self, html):
        self.html = '''<script src="text/javascript">%s</script>''' % html

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, **kwargs):
        return Template(text_type(self.html)).render(context)



class MultiChosenField(Field):
    template = "%s/layout/multichosen.html"

    def __init__(self, *args, **kwargs):
        kwargs['css_class'] = 'crispy-more-chosen'

        args = list(args) + [JS('$(".crispy-more-chosen").chosen();')]
        super().__init__(*args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK, extra_context=None, **kwargs):
        if not hasattr(form, 'Media'):
            form.Media = type('Media', (object,), dict(
                css={
                    'all': []
                },
                js=[]
            ))

        form.Media.css['all'].extend(['//cdnjs.cloudflare.com/ajax/libs/chosen/1.5.1/chosen.jquery.min.js2'])
        form.Media.js.append('//cdnjs.cloudflare.com/ajax/libs/chosen/1.5.1/chosen.css')
        return super(MultiChosenField, self).render(form, form_style, context, template_pack=template_pack, extra_context=extra_context, **kwargs)
    
