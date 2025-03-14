## Скрипт выполняет парсинг SPF записи для домена ##
Скрипт запрашивает имя домена и выводит IP адреса для всех хостов, которые он находит в SPF записи.

### Подготовка ###
Установите пакет для работы скрипта:
```
pip install dnspython
```
### Вывод ###
Скрипт выводит все подчинённые SPF записи для выбранного домена.
Для каждого IP адреса или диапазона скрипт дополнительно выводит информацию о том модификаторе записи SPF, из которого адресы были извлечены (в виде последовательности от самого вложенного SPF до родительского).

Пример вывода для домена `yandex.ru`:
```
SPF record for yandex.ru:
v=spf1 redirect=_spf.yandex.ru

SPF record for _spf.yandex.ru:
v=spf1 include:_spf-ipv6.yandex.ru include:_spf-ipv4-yc.yandex.ru ~all

SPF record for _spf-ipv6.yandex.ru:
v=spf1 ip6:2a02:6b8:c00::/40 ip6:2a02:6b8:0:1472::/64 ip6:2a02:6b8:0:1619::/64 ip6:2a02:6b8:0:1a2d::/64 ip6:2a02:6b8:0:801::/64 ~all

SPF record for _spf-ipv4-yc.yandex.ru:
v=spf1 ip4:178.154.239.80/28 ip4:178.154.239.72/29 ip4:178.154.239.144/28 ip4:178.154.239.136/29 ip4:178.154.239.208/28 ip4:178.154.239.200/29 ip4:51.250.56.16/28 ip4:51.250.56.80/28 ip4:51.250.56.144/28 ~all

Found IP addresses for yandex.ru SPF record:
178.154.239.136/29; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
178.154.239.144/28; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
178.154.239.200/29; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
178.154.239.208/28; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
178.154.239.72/29; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
178.154.239.80/28; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
2a02:6b8:0:1472::/64; _spf-ipv6.yandex.ru(ip6),_spf.yandex.ru(include:_spf-ipv6.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
2a02:6b8:0:1619::/64; _spf-ipv6.yandex.ru(ip6),_spf.yandex.ru(include:_spf-ipv6.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
2a02:6b8:0:1a2d::/64; _spf-ipv6.yandex.ru(ip6),_spf.yandex.ru(include:_spf-ipv6.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
2a02:6b8:0:801::/64; _spf-ipv6.yandex.ru(ip6),_spf.yandex.ru(include:_spf-ipv6.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
2a02:6b8:c00::/40; _spf-ipv6.yandex.ru(ip6),_spf.yandex.ru(include:_spf-ipv6.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
51.250.56.144/28; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
51.250.56.16/28; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
51.250.56.80/28; _spf-ipv4-yc.yandex.ru(ip4),_spf.yandex.ru(include:_spf-ipv4-yc.yandex.ru),yandex.ru(redirect=_spf.yandex.ru)
```
