from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value: str) -> None:
        self._value = None
        self.value = value
    
    
    

class Name(Field):
    
    # def __init__(self, value: str) -> None:
    #    super().__init__(value)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, name: str): 
        if len(name) <= 10:
            self._value = name
        else:
            print ("Too long name") 



class Phone(Field):
    
    # def __init__(self, value: str) -> None:
    #     super().__init__(value)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, phone: str): 
        if len(phone) <= 12:
            self._value = phone # яку перевірку зробити?
        else:
            print("Too long number. It should not be more than 10 digits")

class Birthday:
    def __init__(self, birthday):
        self.birthday = birthday

    @property
    def value(self):
        return self.birthday
    
    @value.setter
    def value(self, birthday: str): # приходить строка типу 21.05.2000, потрібно перетворити на дататайм?
        self.birthday = datetime.strptime(birthday, "%d %B %Y")



class Record:
    
    def __init__(self, name: Name, phone: Phone=None, birthday: Birthday=None) -> None:
        self.name = name
        self.phones = [phone] if phone else []
        if type(birthday) == str: # чи потрібна ці перевірка?
            birthday = Birthday(birthday)
        else:
            self.birthday = birthday
        
    
    def add_phone(self, phone) -> None:
        if phone not in self.phones:
            self.phones.append(phone)

    def delete_phone(self, phone) -> None:
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone
    
    def days_to_birthday(self, birthday: Birthday): # для виклику створюється окремо екземпляр, в якому йде перетворення на обєкт класу Birthday і викликається метод
        self.birthday = birthday
        current_datetime = datetime.now()
        birthday_this_year = birthday.replace(year=current_datetime.year)
        result = current_datetime.data() - birthday_this_year
        return result

class AddressBook(UserDict):
    
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
    
    def find_record(self, value: str) -> Record:
        return self.data.get(value)    


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')