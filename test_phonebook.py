import unittest
from phonebook import PhoneBook



class PhoneBookTestCase(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()
        self.search = self.phonebook.search
        self.add_contact = self.phonebook.add_contact
        self.delete_contact = self.phonebook.delete_contact
        self.view_contact = self.phonebook.view_contact
        self.update_contact = self.phonebook.update_contact

    def test_search(self):
        self.add_contact('jane','diana@email.com','947894704')
        self.add_contact('diana','diana@email.com','9353835')
        actual = self.search('name','diana')
        print(actual)
        self.assertIsNotNone(actual)

        self.assertEquals(actual['name'],'diana')

    def test_add(self):
        actual = self.add_contact('diana','diana@email.com','9353835')
        results = self.search('name', 'diana')
        self.assertIsNotNone(actual)
        self.assertIsNotNone(results)
        self.assertEquals(results['tel'],'9353835')

    def test_delete(self):
        
        
        self.add_contact('diana','diana@email.com','9353835') #we need this for test
        results = self.search('name', 'diana') #search for it
        self.assertIsNotNone(results) #confirm it exists
        self.delete_contact(results['uuid']) #Deletes it regarding the key field,uuid
        results2 = self.search('name', 'diana') #searches to comfirm deletion
        self.assertIsNone(results2) #it does noe exist. Deletion successfull

    def test_update_contact(self):
        actual = self.add_contact('diana','diana@email.com','9353835') #we need this for test
        results = self.search('name','nancy')
        results2 = self.update_contact('uuid',('jane','diana@email.com','9353835'))
        self.assertIsNone(results)
        



   