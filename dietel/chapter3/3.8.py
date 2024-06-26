import statistics

patient = 0
count = 0
total_patient_list = []
while count < 7:
    entered_patient = int(input("Hasta sayısını giriniz: "))
    patient += entered_patient
    count += 1
    total_patient_list.append(entered_patient)
print("Total patients are: ", sum(total_patient_list))
print("Average the patients number: ", statistics.mean(total_patient_list))
print("max patient number in a day: ", max(total_patient_list))
print("min patient number in a day: ", min(total_patient_list))
print(total_patient_list)