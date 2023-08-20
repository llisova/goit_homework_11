from collections import UserDict
from datetime import date

class Field:
    def __init__(self, value: str) -> None:
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value): 
        self._value = value
        

class Name(Field):
    
    def __init__(self, value: str) -> None:
       super().__init__(value)

        
    @Field.value.setter
    def value(self, name: str): 
        if len(name) > 10:
            raise ValueError("Too long name") 
        self._value = name 



class Phone(Field):
    
    def __init__(self, value: str) -> None:
        super().__init__(value)

        
    @Field.value.setter
    def value(self, phone: str): 
        if len(phone) > 12:
            raise ValueError("Too long number. It should not be more than 10 digits")
        self._value = phone 
            

class Birthday(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)

    @staticmethod
    def valid_date_iso(birthday: str) -> None:
        try:
            date.isoformat(birthday)
        except:
            ValueError("date must be in format yyyy-mm-dd")

       

    @Field.value.setter
    def value(self, birthday: str): 
        self.valid_date_iso(birthday)
        self._value = birthday



class Record:
    
    def __init__(self, name: Name, phone: Phone=None, birthday: Birthday=None) -> None:
        self.name = name
        self.phones = [phone] if phone else []
      
        self.birthday = birthday
        
    
    def add_phone(self, phone) -> None:
        if phone not in self.phones:
            self.phones.append(phone)

    def delete_phone(self, phone) -> None:
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone
    
    def days_to_birthday(self) -> int: # для виклику створюється окремо екземпляр, в якому йде перетворення на обєкт класу Birthday і викликається метод
        if self.birthday == None:
            raise KeyError("No birthday set for the contact.")
        
        current_date = date.today()
        birthday = date.fromisoformat(self.birthday.value)
        age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))
        if age >= 100:
            return "Long-lived person"
        birthday = birthday.replace(year=current_date.year) #др в цьому році
        if current_date > birthday:
            birthday = birthday.replace(year=current_date.year+1)
        return (birthday - current_date).days
            
        

class AddressBook(UserDict):
    
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
    
    def find_record(self, value: str) -> Record:
        return self.data.get(value)    


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('12345671258')
    birthday = Birthday("1994-02-26")
    rec = Record(name, phone, birthday)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '12345671258'
    print('All Ok)')
    print(rec.days_to_birthday())
    