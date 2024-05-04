import json
import requests
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, birth_date, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.__birth_date = birth_date  # Geburtsdatum als verstecktes Attribut markiert
        self.sex = sex

    def put(self):
        url = "https://example.com/persons"
        data = self.to_dict()
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print("Person erfolgreich auf dem Server erstellt.")
        else:
            print("Fehler beim Erstellen der Person auf dem Server.")

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "birth_date": self.__birth_date  
        }

class Subject(Person):
    def __init__(self, first_name, last_name, birth_date, sex, email):
        super().__init__(first_name, last_name, birth_date, sex)
        self.email = email

    def update_email(self, new_email):
        url = "https://example.com/subjects/{}/update_email".format(self.first_name)
        data = {"email": new_email}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("E-Mail erfolgreich aktualisiert.")
        else:
            print("Fehler beim Aktualisieren der E-Mail.")

    def estimate_max_hr(self):
        birth_date = datetime.strptime(self._Person__birth_date, '%Y-%m-%d')
        age_years = (datetime.now() - birth_date).days // 365
        if self.sex == "male":
            max_hr_bpm = 223 - 0.9 * age_years
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * age_years
        else:
            max_hr_bpm = int(input("Enter maximum heart rate: "))
        return int(max_hr_bpm)

if __name__ == "__main__":
    test_subject = Subject("Lukas", "Balog", "2003-04-22", "male", "lukas@example.com")
    max_hr_bpm = test_subject.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)

    # Ausgabe des Dictionary
    print("Personen-Daten:")
    print(json.dumps(test_subject.to_dict(), indent=4))
