from django.test import TestCase

class GetLoginTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/login')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'login.html')

    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 4),
            ('<button', 1),
            ('type="email"',1),
            ('type="checkbox"',1),
            ('type="password"',1),
            ('type="submit"',1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context["form"]
        self.assertIsInstance(form, LoginForm)