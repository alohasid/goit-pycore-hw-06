from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []


    def remove_phone(self, phone: Phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            print(f"Phone {phone} not found in record {self.name}.")

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone: Phone):
        for p in self.phones:
            if p.value == phone.value:
                return p
        return None

    def __repr__(self):
        return f"{self.name.value}: {'; '.join(p.value for p in self.phones)}"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        for record in self:
            if name.value in record.name.value:
                return record  
        return None
    
    def delete(self, name):
        record = self.find(name)
        if record:
            self.data.pop(name.value)
        return record
    
    def iterator(self, n):
        for i in range(0, len(self.data), n):
            yield list(self.data.values())[i:i+n]

    def __iter__(self):
        for records in self.iterator(2):
            for record in records:
                yield record
    
    def __str__(self):
        return '\n'.join(str(record) for record in self)

# Створення нової адресної книги
john = Name("John")
jane = Name("Jane")
book = AddressBook()

# Створення запису для John
john_record = Record(john)
john_record.add_phone(Phone('1234567890'))
john_record.add_phone(Phone('5555555555'))

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record(jane)
jane_record.add_phone(Phone('1234567890'))
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find(john)
john.change_phone(Phone("1112223333"), Phone('11122233333'))

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone(Phone('5555555555'))
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete(jane)
