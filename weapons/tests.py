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
        self.assertContains(response, "<h5>Name: Iron Sword</h5>", html=True)
        self.assertContains(response, "<h5>Atk: 5</h5>", html=True)
        self.assertContains(response, "<h5>Amount: 1</h5>", html=True)
        self.assertContains(response, "<h5>Crit Dmg: 80.3</h5>", html=True)
        self.assertContains(response, "<h5>Crit Rate: 18.9</h5>", html=True)
        self.assertContains(response, "<h5>Desc: Basic sword made of iron</h5>", html=True)

        
        
        
# Create your tests here.
