# Система управления деятельностью цифровой кафедры. Чат Бот телеграм

Система состоит из следующих частей:
- Чат бот
- Панель управления для составления, редактирования и хранения расписания
- База для хранения данных о пользователях и их ролях (SQLite? Postgres? MySQL? MongoDB?)

Что хранит, и с чем работает: 

- Учебное расписание, куда входят:
  1. Данные об учащихся, и их группах;
  2. Данные о преподавателях;
  3. Данные о предметах и часах.
- Команды для вывода расписания
- (ФИЧА) Уведомления о начале занятий
- (ФИЧА) Уведомления от имени преподавателя

# Функции
- Авторизация пользователя (студент, преподаватель) (внесение его в систему);
- Добавление, удаление, редактирование данных о пользователе;
- Хранение, отображение, создание, редактирование расписания;