from crud import create_defect, read_defect_by_code, update_defect_count, delete_defect_by_code
from crud import create_employer, read_employer_by_id, update_employer_sheets_sent, delete_employer_by_id
from crud import loading_data_from_json

#В ЭТОМ ФАЙЛЕ ВЫ МОЖЕТЕ ВЗАИМОДЕЙСТВОВАТЬ С БАЗОЙ ДАННЫХ ПРИ ПОМОЩИ ORM-КОМАНД ИЗ ФАЙЛА crud

loading_data_from_json() #добавляем данные из json в бд

create_employer(260676, "Арапов", "Егор", "Евгеньевич", 15) 

create_defect(24506, "Отсутствие сигналов", "Death", "pc", 15) 

employer_id_1 = read_employer_by_id(1) #Поиск сотрудника по его ID
print(employer_id_1)

defect_number_24506 = read_defect_by_code('24506')
print(defect_number_24506) #Поиск дефекта по номеру

update_defect_count("24506", 5) #Обновление численности дефекта с 15 на 5

update_employer_sheets_sent(35, 30) #обновление количества отправленных листов сотрудника с 10 до 30

delete_defect_by_code("24506") #Удаление дефекта номер 24506

delete_employer_by_id(35) #Удаление сотрудника