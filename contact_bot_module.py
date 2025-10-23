from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
	pass

class Phone(Field):
    def value(self, value):
         if value.isdigit() and len(value) == 10:
              super().__init__(value)
         else:
              raise ValueError('Invalid phone number')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def find_phone(self, phone_number):
         for phone in self.phones:
              if phone.value == phone_number:
                   return phone
         return None
              
    def remove_phone(self, phone_number):
         phone_to_remove = self.find_phone(phone_number)
         if phone_to_remove:
              self.phones.remove(phone_to_remove)
         else:
              raise ValueError('Phone number dose not exist')

    def edit_phone(self, old_phone_number, new_phone_number):
         phone_to_edit = self.find_phone(old_phone_number)
         if phone_to_edit:
              phone_to_edit.value = new_phone_number
         else:
              raise ValueError('Phone number dose not exist')

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self, record: Record):
         self.data[record.name.value] = record
    
    def find(self, name):
         return self.data.get(name)
    
    def delete(self,name):
         if name in self.data:
            self.data.pop(name)
         else:
              raise ValueError('This contact dose not exist')
         

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
        print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")