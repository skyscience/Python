@echo off


echo 1. ��ȡ��������
echo 2. ��������ϵͳ

set /p input=�밴�����ѡ��������:
if %input% equ 1 echo a1
    echo [��Ϣ]: ��ȡ������...
    d:
    cd D:\Program\Python\Python ����\Scrapy\Ľ�����渨��ϵͳ\mk\mk\spiders
    scrapy crawl mk 


if %input% equ 2 echo a2
    echo [��Ϣ]: ����ϵͳ��������
    d:
    cd D:\Program\Python\Python ����\Scrapy\Ľ�����渨��ϵͳ
    python cs.py
@pause
