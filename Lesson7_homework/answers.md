***
* Зачем закрывать файл после его открытия?
***
Питон хранит изменения в буфере, потом, когда эти изменения накапливаются, он их переносит на жёсткий диск. Поэтому если файл не закрыть, то может не всё сохраниться. Также открытый файл занимает много оперативной памяти, поэтому его лучше не оставлять открытым.
***
* В чем смысл конструкции with? Когда ее стоит использовать?
***
Конструкция with содержит блоки:
  
    try:
    |
    |
    finally:
        f.close()

То есть при завершении работы с файлом (когда отступов больше не будет) он закрывается автоматически. 
***
* В каких случаях используется сериализация?
***
Чтобы сохранить данные, которые будем пересылать или выгружать из файла в оперативную память. когда нам они нужны.

***
* Каким методы позволяют десериализовать объекты со сложным состоянием?
***
getstate используется для сериализации, в нём _ dict _().copy() копирует атрибуты, потом удаляет несериализуемые. Для дессериализации
используется setstate(), в котором есть метод  _dict _().update(), подгружающий данные вместе с восстановленными атрибутами.