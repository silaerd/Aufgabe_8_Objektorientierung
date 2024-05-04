from my_classes import Subject

if __name__ == "__main__":
    # Testperson erstellen
    test_subject = Subject("Lukas", "Balog", "2002-05-09", "male", "lukas@example.com")
    
    # Testperson auf dem Webserver anlegen
    test_subject.put()

    # E-Mail-Adresse aktualisieren
    new_email = "lukas@example.com"
    test_subject.update_email(new_email)

    # Maximale Herzfrequenz schätzen
    max_hr_bpm = test_subject.estimate_max_hr()
    print("Maximale Herzfrequenz (bpm):", max_hr_bpm)
