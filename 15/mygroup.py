groupmates = [
{
	 "name": "Александр",
	 "surname": "Гусев",
	 "exams": ['БЖ', 'ИТиП', 'АИС'],
	 "marks": [4, 5, 4]
},
{
	 "name": "Валерий",
	 "surname": "Сафонов",
	 "exams": ['История', 'Электротехника', 'ИТиП'],
	 "marks": [4, 4, 3]
},
{
	 "name": "Александр",
	 "surname": "Макашов",
	 "exams": ['Социологоия', 'История', 'КПТ'],
	 "marks": [5, 3, 3]
}
]

def sortbyavg(avg, studlist):
    for i in studlist:
        if sum(i["marks"])/len(i["marks"]) >= avg:
            print(i["name"], i["surname"])
target = float(input("Введите средний балл: "))
sortbyavg(target, groupmates)
