from Nodes.database_node import DatabaseNode

job_titles_data = [
    (1, "Менеджер"),
    (2, "Разработчик"),
    (3, "Аналитик"),
    (4, "Дизайнер")
]

employees_data = [
    (1, "Иванов", "Иван", 2),
    (2, "Петров", "Петр", 1),
    (3, "Сидорова", "Мария", 3),
    (4, "Козлов", "Алексей", 2),
    (5, "Васильева", "Ольга", 4)
]

db = DatabaseNode("SQLliteTask/Nodes/company.db")

db.insert_job_titles(job_titles_data)
db.insert_employees(employees_data)

db.close()