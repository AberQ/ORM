
import json
from models import session, Defect, Employer

#ЭТОТ ФАЙЛ НУЖЕН ДЛЯ СОЗДАНИЯ ORM-КОМАНД


def create_defect(code, defect, work_name, unit, count):
    new_defect = Defect(code=code, defect=defect, work_name=work_name, unit=unit, count=count)
    session.add(new_defect)
    session.commit()
    return new_defect


def read_defect_by_code(code):
    return session.query(Defect).filter_by(code=code).first()


def update_defect_count(code, new_count):
    defect = session.query(Defect).filter_by(code=code).first()
    if defect:
        defect.count = new_count
        session.commit()
        return True
    return False

def delete_defect_by_code(code):
    defect = session.query(Defect).filter_by(code=code).first()
    if defect:
        session.delete(defect)
        session.commit()
        return True
    return False


def create_employer(telegram_id, last_name, first_name, middle_name, sheets_sent):
    new_employer = Employer(telegram_id=telegram_id, last_name=last_name, first_name=first_name, middle_name=middle_name, sheets_sent=sheets_sent)
    session.add(new_employer)
    session.commit()
    return new_employer


def read_employer_by_id(employer_id):
    return session.query(Employer).get(employer_id)


def update_employer_sheets_sent(employer_id, new_sheets_sent):
    employer = session.query(Employer).get(employer_id)
    if employer:
        employer.sheets_sent = new_sheets_sent
        session.commit()
        return True
    return False


def delete_employer_by_id(employer_id):
    employer = session.query(Employer).get(employer_id)
    if employer:
        session.delete(employer)
        session.commit()
        return True
    return False

#___________________________________________________________
#Функции для JSON
#___________________________________________________________

def load_data_from_json(file_path):
   
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def add_defects_from_json(data):
    
    for defect_data in data.get("defects", []):
        defect = Defect(**defect_data)
        session.add(defect)
    session.commit()

def add_employers_from_json(data):
   
    for employer_data in data.get("employers", []):
        employer = Employer(**employer_data)
        session.add(employer)
    session.commit()

def loading_data_from_json():
    data = load_data_from_json('data.json')
    add_defects_from_json(data)
    add_employers_from_json(data)
    print("Данные успешно добавлены в базу данных.")