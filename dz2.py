print('Введите производителя корма:')
print("Royal Canin\nChappi\nHill's\nPurina\nBrit")
hiring= input()
print('Введите тип корма из списка')
print('Лакомство\nСухой\nКонсервированый')
typee = input()
print('Виберите возрастной диапозон')
print('Для щенков\nДля взрослый\nДля пожилых')
age = input()
print('Виберите особености из предлогаемого списка:')
print('Ветеренарная\nДиетическая\nДля белых собак\nВысокие энеготические потребности')
cpecial_featyres = input()
print('Выберете упаковку:')
print('Пакет\nКонтейнер\nБанка\nПауч')
packaging = input()
print('Введите вес')
print("100\n250\n500\n1000\n10kg")
weight = input()
print('Спасибо что выбрали наш магазин\Ваш заказ принят\n',"Номер вашего заказа " )
print('Ваш заказ:\n'
      +'\nПроизводителя корма'+hiring
     +'\nТип корма:' + typee
     +'\nВозрастной диапозон'+ age
     +'\nОсобености'+cpecial_featyres
     +'\nУпоковка'+packaging
     +"\nВес" +weight )

