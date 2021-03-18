### Каталог курса "Введение в анализ данных с Python" 

Текущий курс всегда в корневой папке. Архивные в папках по годам окончания курса. 

Размешено домашнее задание 1 (см. папку meeting 02 файл README.md)

expire_after = datetime.timedelta(days=3)

session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

data_exchange={}

for s in symbol:

      data_exchange[s] =  web.DataReader(s, 'yahoo', start, end, session=session)   
