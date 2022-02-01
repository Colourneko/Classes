

street = str
city = str
province = str
postal_code = str
country = str

#def toString():
  #  return f'i live on {street} in {city} and in the {province} the postal code is{postal_code} and my country is {country}'



class Address:
    def __init__(self ,street:str, city:str, province:str, postal_code:str,country:str ):
        self._street = street
        self._city = city
        self._province = province
        self._postal_code = postal_code
        self._country = country

    def get_street(self):
        return self._street
    def get_city(self):
        return self._city
    def get_province(self):
        return self._province
    def get_postal_code(self):
        return  self._postal_code
    def get_country(self):
        return  self._country

    def set_street(self, street):
        self._street = street
    def set_city(self, city):
        self._city = city
    def set_province(self, provice):
        self._province = province
    def set_postal_code(self, postal_code):
        self._postal_code = postal_code
    def set_country(self, country):
        self._country = country

    def toString(self):
        return f'i live on {self.street} in {self.city} and in the {self.province} the postal code is{self.postal_code} and my country is {self.country}'







