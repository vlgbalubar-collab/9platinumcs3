class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = float(bill_amount)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = float(bill_amount)

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


patients = [
    Patient("Juan Dela Cruz", 15000),
    SeniorPatient("Maria Santos", 15000),
    PhilhealthPatient("Pedro Reyes", 15000)
]

print("Hospital Billing System\n")
for patient in patients:
    print(f"Patient Name: {patient.get_name()}")
    patient.display_patient_type()
    print(f"Original Bill: P{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: P{patient.calculate_bill():,.2f}\n")
