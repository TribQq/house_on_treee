repository == шлюз для взаимодействия с бд
доп разделения,для возмонжости замены бд
благодаря ему мы можем туда положить хоть sql, хоть бд, хоть orm шо у-го-дно





------------------------- транзакции ---------------------------

Проблемы которые решают транзакции:



1. Потерянное обновление:
User.update.money += 100                    |      User.update.money += 300
   (операции перезатрут себя и будет либо +200, либо +100, но не валидные +300)

2. Грязное чтение:

User.update.name =  'Олег'                  |
                                            | user.get.name # взяли олега
REVERT #а транзакция откатилась             |


3. Неповторяющееся чтение:
                                            | user.get.name = 'Василилий'
    user.update.name = 'Олег'               |
                                            | user.get.name = 'Олег'


                                            
4. Чтение фантомов                          
                                            | users.get.all()
       user.create('Олег')                  |
                                            |users.get.all()
   (Добавится лишний юзер, не так критично и очень сложно пофиксит(полной синхронностью бд по очереди))
---------------------------

Начинаем базово со 2го уроня вроде но домик говорит про 3й нужнаа статья)

