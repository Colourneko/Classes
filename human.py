class Person:

    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'



newPerson =  Person("Luke", "Edmunds", )

print(newPerson.full_name())


class UserAccount:
        def __init__(self, user_name, email, password, date_of_birth):
            self.__user_name = user_name
            self.__email = email
            self.__password = password
            self.__dob = date_of_birth
        @property
        def getUname(self):
            return self.__user_name
        @getUname.setter
        def setUname(self, new_uname):
            return  self.__user_name == new_uname

        @property
        def getEmail(self):
            return self.__email
        @getEmail.setter
        def setEmail(self, new_email):
            assert  isinstance(new_email, str),'must be a string'
            assert  '@ ' in new_email, ' must be  vaild email'
            return  self.__email == new_email

        @property
        def getPassword(self):
            return self.__password
        @getPassword.setter
        def setPassword(self, new_password):
            if new_password >= 8:
                print("password must be 8 letters please try again")
                assert isinstance(new_password, str),'must ve a string'
                asser

            return self.__password == new_password

        @property
        def getDob(self):
            return self.__dob
        @getDob.setter
        def setDob(self, new_Dob):
            return self.__dob == new_Dob


aaron = UserAccount(user_name="Aaron Russel",
                        email="aaron.russel@gmail.com",
                        password="nunyabusiness",
                        date_of_birth=date(year=1997, month=6, day=29))

print(aaron.user_name)