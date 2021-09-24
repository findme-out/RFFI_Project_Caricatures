# rffi_carricature_project

the repository contains python-programs on excel files parsing

Requirements: 
1) python 3
2) python packages:
	a) pandas ver 1.3.1;
	b) openpyxl ver 3.0.7;
	c) xlrd ver 2.0.1;
	d) chameleon ver 3.9.1.
	
Примечание: установка питон-пакетов производится через "pip install *package name*" в командной строке

Порядок использования следующий:
1) запустить программу 1:
	а) через консоль (командную строку) перейти в папку с файлами программы;
	б) запустить код в таком формате: python Excel_Handler_Driver.py "xxx", где xxx - путь до папки с Excel-файлами;
	в) дождаться завершения работы программы
	
По завершении парсинга программа указывает, сколько файлов были обработаны успешно, а также автоматически создает папку "Отчет" в папке с Эксель файлами. В папке содержится несколько Excel файлов: первый (отчет.xlsx) содержит информацию о том, какие таблицы были успешно обработаны - указан их путь и статус обработки. Второй (отчет_таблица.xlsx) содержит общую таблицу-матрицу из успешно обработанных файлов (чей статус = success). Третий  - отчет_результат.csv - csv формат таблицы для последующей обработки
	
2) запустить программу 2:	
	а) через консоль (командную строку) перейти в папку с файлами программы;
	б) запустить код в таком формате: python Program_2_Driver.py "xxx", где xxx - путь до папки с csv-файла из работы программы 1 (Excel/Отчет/отчет_результат.csv);
	в) дождаться завершения работы программы
	
По завершении работы в папке Excel/Отчет можно прсомотреть полученный результат обработки
	



