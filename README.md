<div align="center">
    <img src="./frontend/public/addons/rguk.svg" width="600" height="125" alt="rguk.svg" />
    <h1>Сервисный лендинг <a href="https://github.com/bukabtw/kosygin-transfer-website">РГУ им. А.Н. Косыгина</a></h1>
    <p><b><i>Интерактивный сервис для перевода студентов из других вузов (∩^o^)⊃━☆</i></b></p>
    <br>

![Vue.js](https://img.shields.io/badge/vue-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=yellow) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
</div>

## 📌 [Этот лендинг для перевода студентов](https://github.com/bukabtw/kosygin-transfer-website) это...

...интерактивный сервис с пошаговой инструкцией, калькулятором шансов и чек-листом документов. Проект разработан для упрощения процесса перевода студентов из других учебных заведений в РГУ им. А.Н. Косыгина.

Этот проект резюмирует практические навыки, полученные в процессе прохождения производственной практики в **РГУ им. А.Н. Косыгина**.

## 🏗 Архитектура

### Диаграмма системы

Основные части системы взаимодействуют следующим образом:

1. **Пользователь** работает с интерфейсом (**Фронтенд**);
2. **Фронтенд** отправляет данные заявок на консультацию в **Бэкенд** (FastAPI);
3. **Бэкенд** сохраняет заявки в базу данных **SQLite**.

```mermaid
graph LR
    User((Пользователь))

    subgraph FE["Фронтенд (Vue 3)"]
        UI["Интерфейс"]
        Calc["Калькулятор"]
        Checklist["Чек-лист"]
    end

    subgraph BE["Бэкенд (FastAPI)"]
        API["REST API"]
        ConsultService["Сервис заявок"]
    end

    subgraph INF["Инфраструктура"]
        DB[(SQLite)]
    end

    User <--> UI
    UI --> API
    API --> ConsultService
    ConsultService --> DB

    classDef frontend fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px
    classDef backend fill:#E8F5E9,stroke:#43A047,stroke-width:2px
    classDef infra fill:#FFFDE7,stroke:#F9A825,stroke-width:2px
    classDef user fill:#FCE4EC,stroke:#C2185B,stroke-width:2px

    class UI,Calc,Checklist frontend
    class API,ConsultService backend
    class DB infra
    class User user
```

## 🚀 Запуск проекта

### Требования

* **Node.js** (версия 18+)
* **Python** (версия 3.9+)

### Запуск Бэкенда

```bash
cd backend
python -m venv venv
# Windows
.\venv\Scripts\activate
pip install -r requirements.txt
# Запуск сервера
uvicorn main:app --reload
```

Бэкенд будет доступен по адресу: [http://localhost:8000](http://localhost:8000)

### Запуск Фронтенда

```bash
cd frontend
npm install
npm run dev
```

Приложение будет доступно по адресу: [http://localhost:5173](http://localhost:5173)

## 📚 API-Документация

После запуска бэкенда интерактивная документация доступна по адресу:
[http://localhost:8000/docs](http://localhost:8000/docs)

### Основные эндпоинты

* `POST /api/consultations/` — Отправка заявки на консультацию
* `GET /` — Проверка статуса API

## 🛠 Технологический стек

| Область | Технология |
| ---- | --- |
| **Фронтенд** | Vue 3, Vite, Axios, CSS3 |
| **Бэкенд** | Python, FastAPI, SQLAlchemy, Pydantic |
| **База данных** | SQLite |
| **Инструменты** | Mermaid, Git |

## 📂 Структура проекта

```text
├── backend/                # Сервер (FastAPI)
│   ├── main.py             # Основной файл приложения
│   ├── models.py           # Описание таблиц БД
│   └── requirements.txt    # Зависимости Python
├── frontend/               # Клиент (Vue 3)
│   ├── public/             # Статика и скриншоты
│   ├── src/                # Исходный код компонентов
│   └── package.json        # Зависимости Node.js
└── README.md               # Документация проекта
```

## 📸 Скриншоты

<details>
<summary>Посмотреть скриншоты системы</summary>

*Главный экран*
![Main Screen](frontend/public/screenshots/main-section.png)

*Чек-лист документов*
![Checklist](frontend/public/screenshots/checklist.png)

*Часто задаваемые вопросы*
![FAQ](frontend/public/screenshots/faq.png)

*Таймер дедлайна*
![Timer](frontend/public/screenshots/timer.png)
</details>

---

<div align="center">
    <a href="https://github.com/bukabtw/kosygin-transfer-website">
        <img src="./frontend/public/addons/rguk.svg" alt="Logo" width="400" height="100">
    </a>
    <br>
    <sub><b>Сервисный лендинг // РГУ им. А.Н. Косыгина</b></sub>
    <br>
    <sup><i>Made with love by <a href="https://github.com/bukabtw" target="_blank" title="bukabtw">bukabtw</a></i></sup>
</div>
