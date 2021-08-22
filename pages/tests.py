from django.test import TestCase
from .forms import MyForm,ResForm
from .models import UserAccount,Area,Restaurant
import unittest
from pages import views
# Create your tests here.
class ResTestClass(TestCase):
    @classmethod

    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        UserAccount.objects.create(first_name='Big', last_name='Bob')
    
    def test_first_name_label(self):
        user1 = UserAccount.objects.get(id=1)
        field_label = user1._meta.get_field('first_name').verbose_name
        print("Method: testing first name field")
        self.assertEqual(field_label,'first name',"Testing first name in user")

    def test_userobject_name(self):
        user1= UserAccount.objects.create(first_name='Mike', last_name='Bob')
        object_fname = f'{user1.first_name}'
        object_lname = f'{user1.last_name}'
        print("Method: Checking/Matching first name and last name ")
        self.assertEqual('Mike', object_fname,"Testing First Name")
        self.assertNotEqual('Mike', object_lname,"Testing Last Name")


    def test_createRestaurant(self):
        res1= Restaurant.objects.create(Rid=9, Rname='Burger Lab',Aname='Gulshan')
        res=Restaurant.objects.get(Rid=9)
        object1 = res.Rname
        print("Method: Creating object of Restaurant Class")
        self.assertEqual('Burger Lab', object1,"Testing Restaurant Name")
        self.assertNotEqual('Gulshan', object1,"Testing False Area Name")

    def test_deleteRestaurant(self):
        res1= Restaurant.objects.create(Rid=10, Rname='Burger Lab',Aname='Gulshan')
        res=Restaurant.objects.get(Rid=10)
        object1 = res.Rname
        print("Method: Deleting object of Restaurant Class")
        self.assertEqual('Burger Lab', object1,"Testing Restaurant Name")
        views.deleteRes1(10)
        self.assertNotEqual('Burger Lab', res1,"Deleting Restaurant Name")


    def test_DublicateRestaurant(self):
        res1= Restaurant.objects.create(Rid=10, Rname='KFC',Aname='Gulshan')
        object1 = res1.Rname
        print("Method: Checking Dublicate value")
        res2 = Restaurant.objects.create(Rid=11, Rname='KFC',Aname='Gulshan2')
        self.assertNotEqual('KFC', object1,"Dublicate Restaurant Name")    

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    
       