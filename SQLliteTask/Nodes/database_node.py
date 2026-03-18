import sqlite3

class DatabaseNode:
    def __init__(self,db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS `job_titles` (
             `id_job_title` integer primary key NOT NULL UNIQUE,
            `name` TEXT NOT NULL
);
""")

        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS `employees` (
    `id` integer primary key NOT NULL UNIQUE,
    `surname` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `id_job_title` INTEGER NOT NULL,
    FOREIGN KEY(`id_job_title`) REFERENCES `job_titles`(`id_job_title`)

                    );
""")
        self.connection.commit()
    def close(self):
        self.connection.close()
