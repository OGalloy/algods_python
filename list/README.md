Привет.
Этот репозиторий имплементирует структуру данных список.


### LinkedList.py(Связныйсписок) ###

Основная ячейка хранения данных это объект класса Link.
Содержит два свойства: data для хранения данных, next как ссылка на следующий объект Link.
Таким образом наш LinkedList состоит из последовательности объектов класса Link.

Сам объект LinkedList имеет лишь одно свойство head, который является None(Если список пустой) или Link.

Добавление нового значения происходит в начале списка.
Создаеётся новый объект Link, у которого значени поля data равно новому значению, которое мы добавляем в список. А значение поля next будет ссылкой на объект head. Теперь новый объект Link становится головой списка.

Удаление также происходит просто.
Второй элемент списка становится головой

Вставка вначало и удаление из начала односвязного списка происходит за O(1). Можно реализовать стек.

Поиск, и удаление по ключу происходит за O(n) 
