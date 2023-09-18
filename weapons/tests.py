from django.test import TestCase, Client
# Create your tests here.

class mainTest(TestCase):
    def test_weapons_url_is_exist(self):
        response = Client().get('/weapons/')
        self.assertEqual(response.status_code, 200)

    def test_weapons_using_weapons_template(self):
        response = Client().get('/weapons/')
        self.assertTemplateUsed(response, 'weapons.html')
    
    def test_html_content(self):
        response = Client().get('/weapons/')
        self.assertContains(response, "<h1>My Weapons Inventory</h1>", html=True)

        
        
        
# Create your tests here.
