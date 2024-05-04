import json
from my_functions import build_person, build_experiment
from my_classes import Subject

def main():
    # Benutzer nach den benötigten Daten für die Person fragen
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    sex = input("Enter sex: ")
    birth_date = input("Enter birth date (YYYY-MM-DD): ")

    # Instanz für die Person erstellen
    person = Subject(first_name, last_name, birth_date, sex)

    # Maximale Herzfrequenz schätzen
    max_hr_bpm = person.estimate_max_hr()
    print("Max Heart Rate (bpm):", max_hr_bpm)

    # Instanz für das Experiment erstellen
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date: ")
    supervisor = input("Enter supervisor name: ")
    experiment = build_experiment(experiment_name, date, supervisor, person)  # person als Argument übergeben

    # Dictionary für die Experiment-Informationen erstellen
    experiment_info = {
        "experiment_name": experiment_name,
        "date": date,
        "supervisor": supervisor,
        "subject": {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "sex": sex,
            "max_hr_bpm": max_hr_bpm
        }
    }

    # Experimenten-Dictionary ausgeben
    print("Experiment Information:", experiment_info)

    # Experimenten-Dictionary in einer Datei speichern
    with open("experiment.json", "w") as outfile:
        json.dump(experiment_info, outfile, indent=4)

if __name__ == "__main__":
    main()
