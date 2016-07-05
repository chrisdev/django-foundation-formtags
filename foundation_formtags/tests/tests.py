from django.template import Template, Context
import unittest

from .forms import SimpleForm, ComplexForm


class TestFoundationform(unittest.TestCase):

    def tag_test(self, template, context, contains):
        t = Template('{% load foundation_formtags %}' + template)
        c = Context(context)
        self.assertIn(contains, t.render(c))

    def test_as_foundation_tag_simple(self):
        data = {'text': 'Tests'}
        simple_form = SimpleForm(data)
        template = '{{ form|as_foundation }}'
        context = {'form': simple_form}
        contains = '<input id="id_text" name="text" type="text" value="Tests" />'

        self.tag_test(template, context, contains)

    def test_as_foundation_tag_complex(self):
        data = {'char_field': 'Tests', 'password_field': 'password',
                'choice_field': 'Option 1', 'boolean_field': 'True'}
        simple_form = ComplexForm(data)
        template = '{{ form|as_foundation }}'
        context = {'form': simple_form}
        contains = '<small class="error">This field is required.</small>'

        self.tag_test(template, context, contains)

if __name__ == '__main__':
    unittest.main()
