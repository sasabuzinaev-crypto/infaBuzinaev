# Репозиторий для домашних заданий по информатике

## Быстрый старт (uv + venv)
1. Убедись, что `uv` в PATH (`uv --version`). Если не видит, добавь `export PATH="$HOME/.local/bin:$PATH"` в `~/.zshrc` и перезапусти терминал.
2. В корне репозитория (`/Users/sashabuzinaevicloud.com/Documents/infaDemiusdz`):
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install pandas openpyxl
   ```

## Основные скрипты
- Импорт данных из CSV в SQLite:  
  `uv run SQLliteTask/import_from_csv.py`

- Проверка класса `Database` на временной БД:  
  `uv run SQLliteTask/test_database.py`

- Экспорт данных в CSV/XLSX и обратная проверка чтения:  
  `uv run SQLliteTask/test_io.py`
  (для XLSX нужен установленный `openpyxl`)

## Структура данных
- База: `SQLliteTask/Nodes/company.db`
- CSV для импорта: `SQLliteTask/data/job_titles.csv`, `SQLliteTask/data/employees.csv`, пример `SQLliteTask/data/sample_contacts.csv`

## Полезные команды
- Сохранить список зависимостей в файл:  
  `uv pip freeze > requirements.txt`
