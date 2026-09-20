# JobMatcher

JobMatcher —  веб-приложение для поиска вакансий и подбора наиболее
подходящих предложений на основе навыков, опыта и профессионального
профиля пользователя.

Пользователь может зарегистрироваться, заполнить профиль, загрузить
резюме PDF/DOCX, автоматически извлечь навыки, просматривать вакансии и
получать рекомендации с процентом соответствия профилю.

> **Для проверяющего:** основной сценарий запуска --- Windows +
> PowerShell. Инструкция ниже рассчитана на чистый компьютер и содержит
> все команды по порядку. Docker нужен только для локальной проверки
> восстановления пароля через Mailpit.

## Возможности

-   регистрация и авторизация;
-   восстановление пароля;
-   профессиональный профиль;
-   загрузка резюме PDF/DOCX;
-   извлечение навыков из резюме;
-   просмотр и поиск вакансий;
-   демонстрационная база вакансий;
-   расчёт процента соответствия вакансии профилю;
-   рекомендации вакансий;
-   REST API на FastAPI;
-   веб-интерфейс на React.

## Стек технологий

### Backend

-   Python 3.13+
-   FastAPI
-   SQLAlchemy 2
-   Alembic
-   MySQL 8
-   Pydantic
-   Uvicorn
-   PyMuPDF
-   python-docx
-   PyJWT
-   pwdlib / Argon2
-   Pytest

### Frontend

-   React
-   Vite
-   React Router
-   Lucide React
-   CSS

### Дополнительно

-   Git
-   Docker Desktop / Docker Compose
-   Mailpit --- локальный SMTP-сервер для тестирования восстановления
    пароля

# Быстрый порядок запуска

После установки необходимых программ запуск выполняется в таком порядке:

``` text
1. git clone
2. backend: создать .venv и установить requirements.txt
3. MySQL: создать базу jobmatcher
4. backend: создать и заполнить .env
5. backend: alembic upgrade head
6. backend: загрузить демонстрационные вакансии
7. при необходимости восстановления пароля: запустить Mailpit
8. терминал 1: запустить Backend
9. терминал 2: запустить Frontend
10. открыть http://localhost:5173
```

Подробная инструкция --- ниже.


# 1. Что необходимо установить

Перед клонированием проекта рекомендуется установить:

1.  Git for Windows
2.  Python 3.13 или новее
3.  MySQL Server 8
4.  Node.js LTS
5.  Docker Desktop --- **только если нужно проверить восстановление
    пароля через Mailpit**

Проверка:

``` powershell
git --version
python --version
mysql --version
node --version
npm --version
```

Docker проверяется отдельно:

``` powershell
docker --version
docker compose version
```

Если после установки какой-либо программы команда не распознаётся,
закройте PowerShell и откройте его снова.

Официальные страницы:

-   Git for Windows: https://git-scm.com/download/win
-   Python: https://www.python.org/downloads/
-   MySQL Installer: https://dev.mysql.com/downloads/installer/
-   Node.js LTS: https://nodejs.org/en/download
-   Docker Desktop: https://www.docker.com/products/docker-desktop/

# 2. Клонирование проекта

Создайте или выберите папку, в которой будет находиться проект.

Например:

``` text
C:\Users\USERNAME\Documents\JobMatcher-Test
```

Откройте эту папку в Проводнике Windows, нажмите на адресную строку,
введите:

``` text
powershell
```

и нажмите `Enter`.

Проверьте Git:

``` powershell
git --version
```

Клонируйте проект:

``` powershell
git clone https://github.com/donette243/Jobmatcherv2.git
```

Перейдите в проект:

``` powershell
cd Jobmatcherv2
```

В корне должны находиться как минимум:

``` text
backend
frontend
docker-compose.yml
README.md
```


# 3. Backend: виртуальное окружение

Перейдите в backend:

``` powershell
cd backend
```

Создайте виртуальное окружение:

``` powershell
python -m venv .venv
```

Активируйте его:

``` powershell
.\.venv\Scripts\Activate.ps1
```

После успешной активации строка PowerShell начинается с:

``` text
(.venv)
```

## Если PowerShell блокирует Activate.ps1

Если появляется `PSSecurityException` или сообщение о запрете выполнения
сценариев, выполните:

``` powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Подтвердите изменение, если Windows спросит, затем снова:

``` powershell
.\.venv\Scripts\Activate.ps1
```

> При открытии нового PowerShell виртуальное окружение необходимо
> активировать снова.


# 4. Backend: установка зависимостей

Убедитесь, что вы находитесь в `backend` и видите `(.venv)`.

Выполните:

``` powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Дополнительная ручная установка Python-библиотек не требуется.


# 5. MySQL: установка и создание базы

JobMatcher использует MySQL.

Проверьте:

``` powershell
mysql --version
```

Если MySQL не установлен, установите MySQL Server 8 через MySQL
Installer:

https://dev.mysql.com/downloads/installer/

Во время установки:

-   можно выбрать `Developer Default` или `Server Only`;
-   оставьте стандартный порт `3306`, если нет причины менять его;
-   задайте пароль пользователя MySQL и сохраните его;
-   убедитесь, что MySQL Server запущен.

## Создание базы через MySQL Workbench

Откройте MySQL Workbench, подключитесь к локальному серверу и выполните:

``` sql
CREATE DATABASE jobmatcher;
```

Если база уже существует, повторно создавать её не нужно.


# 6. Backend: файл .env

Все команды этого раздела выполняются из папки `backend`.

Создайте `.env` из шаблона:

``` powershell
Copy-Item .env.example .env
```

Откройте файл:

``` powershell
notepad .env
```

Пример:

``` env
DATABASE_URL=mysql+pymysql://USER:PASSWORD@localhost:3306/jobmatcher

JWT_SECRET_KEY=replace-with-a-random-secret-key-at-least-32-bytes-long
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

SMTP_HOST=localhost
SMTP_PORT=1025
SMTP_FROM=jobmatcher@example.com
SMTP_USE_TLS=false

FRONTEND_URL=http://localhost:5173
```

Замените:

-   `USER` --- на пользователя MySQL, например `root`;
-   `PASSWORD` --- на пароль этого пользователя;
-   `JWT_SECRET_KEY` --- на собственный случайный секрет длиной не менее
    32 байт.

Например, структура `DATABASE_URL`:

``` text
mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/jobmatcher
```

> **Важно:** не публикуйте `.env`, пароли, JWT-секреты и SMTP-данные в
> GitHub.

Если пароль MySQL содержит специальные символы, строка URL может
потребовать URL-кодирования. Самый простой вариант для локального теста
--- использовать корректно закодированный пароль или отдельного
MySQL-пользователя для проекта.


# 7. Backend: PYTHONPATH и миграции

Перед миграциями убедитесь, что:

-   MySQL Server запущен;
-   база `jobmatcher` существует;
-   `.env` настроен;
-   `.venv` активирован;
-   текущая папка --- `backend`.

В PowerShell установите:

``` powershell
$env:PYTHONPATH="src"
```

> `PYTHONPATH` действует только в текущем терминале. В новом PowerShell
> эту команду нужно выполнить снова.

Примените миграции:

``` powershell
alembic upgrade head
```

После успешной миграции создаются таблицы приложения:

``` text
users
profiles
preferences
skills
profile_skills
jobs
job_skills
alembic_version
```

Проверить текущую миграцию:

``` powershell
alembic current
```

Если появляется:

``` text
ModuleNotFoundError: No module named 'jobmatcher'
```

проверьте, что вы находитесь в `backend`, `.venv` активирован и
выполнено:

``` powershell
$env:PYTHONPATH="src"
```

# 8. Добавление тестовых вакансий

После создания новой базы данных таблица вакансий будет пустой.

Чтобы сразу проверить работу поиска вакансий и системы рекомендаций,
проект содержит набор из 20 тестовых вакансий.

Из папки `backend`, при активном `.venv` и установленном `PYTHONPATH`,
выполните:

``` powershell
python -m jobmatcher.scripts.seed_jobs
```

При первом запуске ожидается сообщение вида:

``` text
Demo jobs added: 20. Already existed: 0.
```

Повторный запуск безопасен и не создаёт дубликаты:

``` text
Demo jobs added: 0. Already existed: 20.
```

После этого в приложении будут доступны демонстрационные вакансии разных
направлений, а раздел рекомендаций сможет рассчитывать matching.


# 9. Запуск Backend

Откройте PowerShell в папке `backend`.

Если это новый терминал:

``` powershell
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH="src"
```

Запустите:

``` powershell
uvicorn jobmatcher.main:app --reload
```

Успешный запуск выглядит примерно так:

``` text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

Откройте Swagger:

``` text
http://127.0.0.1:8000/docs
```

Если Swagger открывается, Backend работает.

> **Не закрывайте этот терминал.** Backend должен работать одновременно
> с Frontend.


# 10. Frontend: установка и запуск

Откройте **новый PowerShell**. Backend должен продолжать работать в
первом терминале.

Проверьте Node.js:

``` powershell
node --version
npm --version
```

Если Node.js не установлен, установите LTS:

https://nodejs.org/en/download

Перейдите из корня проекта в frontend:

``` powershell
cd frontend
```

Если новый терминал открылся в другом месте, сначала перейдите в папку
проекта, например:

``` powershell
cd C:\Users\USERNAME\Documents\JobMatcher-Test\Jobmatcherv2\frontend
```

Установите зависимости:

``` powershell
npm install
```

Запустите Frontend:

``` powershell
npm run dev
```

Ожидаемый адрес:

``` text
http://localhost:5173
```

Откройте его в браузере.

Во время обычной работы должны одновременно оставаться открытыми:

``` text
Терминал 1 — Backend
http://127.0.0.1:8000

Терминал 2 — Frontend
http://localhost:5173
```

Если Frontend показывает `Failed to fetch`, первым делом проверьте, что
Backend всё ещё запущен.


# 11. Mailpit и восстановление пароля

## Важно

Docker и Mailpit **не нужны для регистрации, входа, профиля, CV,
вакансий и рекомендаций**.

Они нужны для локальной проверки отправки письма восстановления пароля.

Mailpit перехватывает письмо локально. Письмо **не приходит в настоящий
Gmail/Outlook**. Его нужно открыть в интерфейсе Mailpit.

## 11.1 Проверка Docker

Запустите Docker Desktop.

Затем:

``` powershell
docker --version
docker compose version
docker info
```

`docker info` должен содержать работающую серверную часть Docker
(`Server`).

Если Docker установлен, но `docker info` сообщает ошибку подключения к
`docker_engine`, дождитесь запуска Docker Desktop.

Если Docker Desktop показывает:

``` text
Virtualization support not detected
```

Docker Engine на этом компьютере не может запуститься, пока в
системе/BIOS не будет доступна аппаратная виртуализация.

В этом случае основной JobMatcher продолжит работать, но локальный
Mailpit через Docker запустить нельзя.

## 11.2 Запуск Mailpit

`docker-compose.yml` находится **в корне JobMatcher**, а не в `backend`.

Если вы сейчас в `backend`, перейдите на уровень выше:

``` powershell
cd ..
```

Запустите:

``` powershell
docker compose up -d
```

Проверьте:

``` powershell
docker compose ps
```

Mailpit использует:

``` text
SMTP: localhost:1025
Web UI: http://localhost:8025
```

Откройте:

``` text
http://localhost:8025
```

Если интерфейс Mailpit открывается, локальный SMTP готов.

> `docker compose up -d` в этом проекте запускает Mailpit. Backend и
> MySQL этой командой не запускаются.

Остановить Mailpit:

``` powershell
docker compose down
```

## 11.3 Полный тест восстановления пароля

Для проверки:

1.  Backend должен работать.
2.  Frontend должен работать.
3.  Mailpit должен работать.
4.  В JobMatcher откройте страницу входа.
5.  Нажмите `Забыли пароль?`.
6.  Введите email зарегистрированного пользователя.
7.  Отправьте запрос.
8.  Откройте `http://localhost:8025`.
9.  Откройте письмо JobMatcher.
10. Перейдите по ссылке восстановления.
11. Установите новый пароль.
12. Войдите с новым паролем.

Если Mailpit не запущен, запрос восстановления может завершиться
ошибкой, потому что Backend не сможет подключиться к SMTP на
`localhost:1025`.


# 12. Использование внешнего SMTP

Mailpit предназначен для локальной разработки.

Для реальной доставки писем можно настроить внешний SMTP-провайдер в
`.env`:

``` env
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your-user
SMTP_PASSWORD=your-password
SMTP_FROM=your-email@example.com
SMTP_USE_TLS=true
FRONTEND_URL=http://localhost:5173
```

Конкретные значения зависят от SMTP-провайдера.

Никогда не сохраняйте реальные SMTP-пароли или API-ключи в GitHub.

# 13. Проверка основного сценария

После запуска Backend и Frontend:

1.  Зарегистрируйте нового пользователя.
2.  Войдите.
3.  Откройте панель управления.
4.  Заполните и сохраните профессиональный профиль.
5.  Загрузите CV в формате PDF или DOCX.
6.  Проверьте извлечённые данные/навыки.
7.  Откройте `Вакансии`.
8.  Проверьте поиск по вакансиям.
9.  Откройте `Рекомендации`.
10. Проверьте проценты соответствия.
11. Выйдите из аккаунта.
12. Войдите снова и убедитесь, что данные профиля сохранены.

Если появляется:

``` text
Invalid or expired token
```

выйдите из аккаунта и войдите снова, чтобы получить новый токен.


# 14. Backend-тесты

Откройте отдельный PowerShell в `backend`.

Выполните:

``` powershell
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH="src"
pytest
```

Текущий ожидаемый результат:

``` text
5 passed
```

Тестовый CV находится в:

``` text
backend/test_files/cv.pdf
```


# 15. Частые проблемы

## `git` не распознаётся

Установите Git for Windows и заново откройте PowerShell.

## `Activate.ps1 cannot be loaded` / `PSSecurityException`

``` powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

После этого снова активируйте `.venv`.

## `ModuleNotFoundError: No module named 'jobmatcher'`

Из `backend`:

``` powershell
$env:PYTHONPATH="src"
```

## `Failed to fetch`

Проверьте Backend:

``` text
http://127.0.0.1:8000/docs
```

Если Swagger не открывается, запустите Backend.

Если `Failed to fetch` появляется именно при восстановлении пароля,
посмотрите терминал Backend. Если там ошибка
SMTP/`ConnectionRefusedError`, запустите Mailpit.

## `ConnectionRefusedError` при восстановлении пароля

Обычно Mailpit не работает.

Проверьте:

``` powershell
docker info
docker compose ps
```

И откройте:

``` text
http://localhost:8025
```

## `Virtualization support not detected`

Это ограничение Docker Desktop/системы, а не Backend JobMatcher. Для
запуска Docker Engine требуется доступная аппаратная виртуализация. Без
неё можно использовать основной функционал JobMatcher, но Mailpit через
Docker работать не будет.

## `Invalid or expired token`

Выйдите из JobMatcher и войдите снова.

## Вакансии не отображаются

Убедитесь, что выполнен seed:

``` powershell
cd backend
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH="src"
python -m jobmatcher.scripts.seed_jobs
```

## MySQL `Access denied`

Проверьте `USER` и `PASSWORD` в `DATABASE_URL` файла `.env`, а также
убедитесь, что этот MySQL-пользователь имеет доступ к базе `jobmatcher`.


# 16. API

После запуска Backend Swagger доступен здесь:

``` text
http://127.0.0.1:8000/docs
```

Swagger позволяет просматривать и тестировать API endpoints.


# 17. Структура запуска для проверяющего

После первоначальной установки при последующих запусках обычно
достаточно следующего.

## Терминал 1 --- Backend

``` powershell
cd PATH\TO\Jobmatcherv2\backend
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH="src"
uvicorn jobmatcher.main:app --reload
```

## Терминал 2 --- Frontend

``` powershell
cd PATH\TO\Jobmatcherv2\frontend
npm run dev
```

## Только для проверки восстановления пароля

Из корня проекта:

``` powershell
docker compose up -d
```

Mailpit:

``` text
http://localhost:8025
```

Приложение:

``` text
http://localhost:5173
```



# 18. Статус проекта

Основной пользовательский сценарий реализован и протестирован:

-   регистрация и авторизация;
-   профессиональный профиль;
-   загрузка и обработка CV;
-   извлечение навыков;
-   демонстрационные вакансии;
-   поиск вакансий;
-   matching и рекомендации;
-   восстановление пароля через Mailpit в локальной среде с работающим
    Docker;
-   Backend-тесты.

