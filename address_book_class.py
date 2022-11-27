from collections import UserDict

#----------створюємо Клас Field, який буде батьківським для всіх полів.
class Field:
    def __init__(self, value) -> None:
        self.value = value

#----------створюємо Клас Name, обов'язкове поле з ім'ям.
class Name(Field):
    pass

#----------створюємо Клас Phone, необов'язкове поле з телефоном.
class Phone(Field):
    pass

#class EMail(Field):
#   pass

#---------створюємо Клас Record, який відповідає за логіку додавання/видалення/редагування
#---------необов'язкових полів та зберігання обов'язкового поля Name.
class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []
#       self.e_mail = []

    def get_info(self):
        phones_info = ""
        for phone in self.phones:
            phones_info += f"{phone.value}"
        return f"{self.name.value}:{phones_info[:]}"

#---------додавання номера
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

#---------видалення номера
    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False

#---------редагування номера
    def change_phones(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)

#----------Клас AddressBook, який успадковується від UserDict.
class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)
        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record
        raise ValueError(f"Contact {value} doesn't exist.")