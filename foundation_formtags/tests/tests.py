from django.template import Template, Context
import unittest

from .forms import SimpleForm, ComplexForm


def render_form(text, form=None, **context_args):
    tpl = Template("{% load foundation_formtags %}" + text)
    context_args.update({'form': ComplexForm() if form is None else form})
    context = Context(context_args)
    return tpl.render(context)


def render_field(field, template_filter, params, *args, **kwargs):
    filters = [(template_filter, params)]
    filters.extend(zip(args[::2], args[1::2]))
    filter_strings = ['|%s:"%s"' % (f[0], f[1],) for f in filters]
    render_field_str = '{{ form.%s%s }}' % (field, ''.join(filter_strings))
    return render_form(render_field_str, **kwargs)


class TestFoundationform(unittest.TestCase):

    def filter_or_tag_test(self, template, context, contains):
        t = Template('{% load foundation_formtags %}' + template)
        c = Context(context)
        self.assertIn(contains, t.render(c))

    def test_as_foundation_filter_simple(self):
        data = {'text': 'Tests'}
        simple_form = SimpleForm(data)
        template = '{{ form|as_foundation }}'
        context = {'form': simple_form}
        contains = '<input id="id_text" name="text" type="text" value="Tests" />'

        self.filter_or_tag_test(template, context, contains)

    def test_as_foundation_filter_complex(self):
        data = {'char_field': 'Tests', 'password_field': 'password',
                'choice_field': 'Option 1', 'boolean_field': 'True'}
        complex_form = ComplexForm(data)
        template = '{{ form|as_foundation }}'
        context = {'form': complex_form}
        contains = '<input id="id_password_field" name="password_field" type="password" />'

        self.filter_or_tag_test(template, context, contains)

    def test_render_field_tag_simple(self):
        data = {'text': 'Tests'}
        simple_form = SimpleForm(data)
        template = '<form class="form" action="" method="POST"> \
                        {% csrf_token %} \
                        {% render_field form.text %} \
                    </form>'
        context = {'form': simple_form}
        contains = '<input id="id_text" name="text" type="text" value="Tests" />'

        self.filter_or_tag_test(template, context, contains)

    def test_render_field_tag_complex(self):
        data = {'char_field': 'Tests', 'password_field': 'password',
                'choice_field': 'Option 1', 'boolean_field': 'True'}
        complex_form = ComplexForm(data)
        template = '<form class="form" action="" method="POST"> \
                        {% csrf_token %} \
                        {% render_field form.char_field %} \
                        {% render_field form.password_field %} \
                    </form>'
        context = {'form': complex_form}
        contains = '<input id="id_password_field" name="password_field" type="password" />'

        self.filter_or_tag_test(template, context, contains)

    def test_add_multiple_classes(self):
        res = render_field('char_field', 'add_class', 'foo bar')
        self.assertIn('class="foo bar"', res)

    def test_add_class_chaining(self):
        res = render_field('char_field', 'add_class', 'foo', 'add_class', 'bar')
        self.assertIn('class="bar foo"', res)

    def test_silence_without_field(self):
        res = render_field("nothing", 'add_class', 'some')
        self.assertEqual(res, "")

if __name__ == '__main__':
    unittest.main()
