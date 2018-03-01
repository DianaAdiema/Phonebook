import uuid


class PhoneBook:

    def __init__(self):
       self.phonebook_dict = {}

    def add_contact(self, name, email, number):
    	contact_uuid = uuid.uuid4()
    	self.phonebook_dict[contact_uuid] = {
    	'name':name, 
    	'email':email,
    	'tel':number,
    	'uuid': contact_uuid
    	}

    	return self.phonebook_dict

    def search(self,field, search_param):
	    for k, v in self.phonebook_dict.items():
	        if v.get(field) == search_param:
	            return v
	    return None


       
 
    def update_contact(self,uuid,fields): 
    	"""
    	Fields should be a dictionary containing either email,name,tel. to search find uuid before deleting


    	"""
    	contact = self.phonebook_dict.get(uuid,None) 

    	if contact is None:
    		return None
    	contact.update(fields) #searches using uuid then updates rest of field attached to uuid.


    def delete_contact(self, uuid):
    	contact = self.phonebook_dict.get(uuid,None) #Search for contact to be delete, if not there return none
    	if contact is None:
    		return None
    	self.phonebook_dict.pop(uuid) #delete the uuid(key) which deletes the fields aligned to it
    	return self.phonebook_dict

    def view_contact(self):

         for k, v in self.phonebook_dict.items():
         	return v




    	
        

        


