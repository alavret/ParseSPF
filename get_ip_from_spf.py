import dns.resolver
import re
from ipaddress import ip_address, ip_network

def resolve_spf(domain):
    """
    Извлекает и парсит SPF запись для заданного домена
    """
    try:
        # Получаем TXT записи для домена
        answers = dns.resolver.resolve(domain, 'TXT')
        spf_record = None
        
        # Ищем запись, содержащую SPF
        for rdata in answers:
            txt_record = rdata.to_text()
            txt_record = txt_record.replace('" "', '').replace('"', '')
            if 'v=spf1' in txt_record:
                spf_record = txt_record
                break
                
        if not spf_record:
            return f"No SPF record found for {domain}"
            
        return parse_spf(spf_record, domain)
        
    except dns.resolver.NXDOMAIN:
        return f"Domain {domain} not found"
    except dns.resolver.NoAnswer:
        return f"No TXT records found for {domain}"
    except Exception as e:
        return f"Error resolving SPF: {str(e)}"

def parse_spf(spf_record, original_domain):
    """
    Рекурсивно парсит SPF запись и извлекает IP адреса
    """
    ip_list = {}
    elements = spf_record.split()
    
    for element in elements:
        try:
            element = element.replace('+', '')
            # Обработка прямых IP адресов (ip4 и ip6)
            if element.startswith('ip4:'):
                ip = element.replace('ip4:', '')
                if ip in ip_list.keys():
                    ip_list[ip] += ', ip4'
                else:
                    ip_list[ip] = 'ip4'
                
            elif element.startswith('ip6:'):
                ip = element.replace('ip6:', '')
                if ip in ip_list.keys():
                    ip_list[ip] += ', ip6'
                else:
                    ip_list[ip] = 'ip6'
                
            # Обработка MX записей
            elif element.startswith('mx'):
                try:
                    mx_records = dns.resolver.resolve(original_domain, 'MX')
                    for mx in mx_records:
                        mx_domain = str(mx.exchange)
                        # Получаем A/AAAA записи для MX
                        try:
                            a_records = dns.resolver.resolve(mx_domain, 'A')
                            for a in a_records:
                                if str(a) in ip_list.keys():
                                    ip_list[str(a)] += ', mx'
                                else:
                                    ip_list[str(a)] = 'mx'
                        except:
                            pass
                        try:
                            aaaa_records = dns.resolver.resolve(mx_domain, 'AAAA')
                            for aaaa in aaaa_records:
                                if str(aaaa) in ip_list.keys():
                                    ip_list[str(aaaa)] += ', mx'
                                else:
                                    ip_list[str(aaaa)] = 'mx'
                        except:
                            pass
                except:
                    pass
                    
            # Обработка A записей
            elif element.startswith('a'):
                domain = original_domain
                if ':' in element:
                    domain = element.split(':')[1]
                try:
                    a_records = dns.resolver.resolve(domain, 'A')
                    for a in a_records:
                        if str(a) in ip_list.keys():
                            ip_list[str(a)] += ', a'
                        else:
                            ip_list[str(a)] = 'a'
                except:
                    pass
                    
            # Рекурсивная обработка include
            elif element.startswith('include:') or element.startswith('redirect='):
                included_domain = element.replace('include:', '').replace('redirect=', '')
                included_spf = resolve_spf(included_domain)
                if isinstance(included_spf, dict):
                    for ip in included_spf:
                        if ip in ip_list.keys():
                            ip_list[ip] += ', ' + element   
                        else:
                            ip_list[ip] = element
                    
        except Exception as e:
            print(f"Error processing element {element}: {str(e)}")
            continue
            
    return ip_list

def main():
    # Пример использования
    domain = input("Enter domain name (e.g., google.com): ")
    result = resolve_spf(domain)
    
    if isinstance(result, dict):
        print(f"\nFound IP addresses for {domain} SPF record:")
        #print(result)
        for k,v in sorted(result.items()):
            print(f'{k}; {v}')
    else:
        print(result)

if __name__ == "__main__":
    main()