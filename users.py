from abc import ABC, abstractmethod

class CreateUser(ABC):
    @abstractmethod
    def create(self):
        pass

class CreateStudent(CreateUser):
    def create(self):
        from datetime import date
        import random
        
        current_date = date.today()
        
        id = random.randrange(1, 100, 1)
        
        #Inputs of the student data
        first_name = input('> Enter the first name of the student: ')
        last_name = input('> Enter the last name of the student: ')
        phone_number = input('> Enter the phone number of the student')
        email = input('> (Optional) Enter the email of the student: ')
        
        #The status is regular by default
        status = 'regular'
        
        #The register is constructed this way year-period-id within 8 characters
        register = ''
        if current_date.month < 6:
            register = f'{current_date.year}{1}{id}'
        else:
            register = f'{current_date.year}{2}{id}'
        
        print(f'> The student named {first_name} {last_name} was created with the register: {register}')

def CreateProfessor()