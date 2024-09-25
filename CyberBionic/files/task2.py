import shelve

employees = [
    {
        "name": "Chungachanga",
        "position": "Developer",
        "experience": "5 years",
        "efficiency_coefficient": 0.87,
        "tech_stack": ["Python", "Django", "PostgreSQL", "Docker"],
        "salary": 3000,
    },
    {
        "name": "Papa-Karlo",
        "position": "Designer UX/UI",
        "experience": "3 years",
        "efficiency_coefficient": 0.92,
        "tech_stack": ["Figma", "Sketch", "Adobe XD"],
        "salary": 2500,
    },
    {
        "name": "Terminator",
        "position": "Data science",
        "experience": "7 years",
        "efficiency_coefficient": 0.95,
        "tech_stack": ["Python", "R", "SQL", "Tableau"],
        "salary": 3500,
    },
]


def create_db(employee):
    with shelve.open("employees") as db:
        for employee in employees:
            db[employee["name"]] = employee

def get_name_from_db(name):
    with shelve.open("employees") as db:
        return db.get(name) 

# Не розібрався з апдейт
# def update_db(employee):
#     with shelve.open("employees") as db:
#         db[employee["name"]] = employee 

# update_db(employee)

with shelve.open("employees") as db:
    print(dict(db))