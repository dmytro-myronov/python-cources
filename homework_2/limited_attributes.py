

class LimitedAttributes:

    attributes = ['name', 'email']
    def __init__(self,*args, **kwargs):
        self.__dict__.update(kwargs)

    def __call__(self, *args, **kwargs):
        if len(kwargs) > len(LimitedAttributes.attributes):
            raise AttributeError('Too many attributes')
        self.__dict__.update(kwargs)
        return self

    def __setattr__(self, name, value):

        try :
            if self.__dict__[name]:
                self.__dict__[name] = value
        except KeyError as e:
            print("You can not add/edit this attribute")


class Person(metaclass=LimitedAttributes):

    def __init__(self, **kwargs):
        super().__init__(kwargs)


person = Person(name ='Dima', email ='email2@gmail.com')
person.age = 34
person.email ="afer@gmaillcom"
print(person.email)