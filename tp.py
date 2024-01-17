# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://dblp.uni-trier.de/pers/?prefix=Li+Feng'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# element_with_id = soup.find(id='browse-person-output')
# final_arr_dict=[]
#
# link2=''
# if element_with_id:
#     ul_element = element_with_id.find('ul')
#
#     if ul_element:
#         for li in ul_element.find_all('li'):
#             a_element = li.find('a')
#             if a_element:
#                 href_link = a_element.get('href')
#                 link2=href_link
#                 break
#     else:
#         print("No <ul> element found inside the element with id 'example_id'.")
# else:
#     print("No element with id 'example_id' found on the page.")
#
#
# def extract_id_from_url(url):
#     url_parts = url.split('/')
#     pid_index = url_parts.index('pid') if 'pid' in url_parts else -1
#     if pid_index != -1 and pid_index + 1 < len(url_parts):
#         return '/'.join(url_parts[pid_index + 1:]).split('.')[0]
#     else:
#         return None
#
# if link2:
#     response = requests.get(link2)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     element_with_id = soup.find(class_='expand-head')
#     print(element_with_id)
#     if element_with_id:
#         for li in element_with_id.find_all('li'):
#             a_element = li.find('a')
#             s = ''
#             for a_tag in a_element:
#                 s+=a_tag.text
#             print(s)
#             if a_element:
#                 href_link = a_element.get('href')
#                 print(href_link)
#
#                 id_from_url = extract_id_from_url(href_link)
#                 print(id_from_url)
#                 dict={'name':s, 'url':href_link, 'pid':id_from_url}
#                 final_arr_dict.append(dict)
#     element_with_id = soup.find(class_='expand-body')
#
#     if element_with_id:
#         for li in element_with_id.find_all('li'):
#             a_element = li.find('a')
#             s = ''
#             for a_tag in a_element:
#                 s += a_tag.text
#             print(s)
#             if a_element:
#                 href_link = a_element.get('href')
#                 print(href_link)
#
#                 id_from_url = extract_id_from_url(href_link)
#                 print(id_from_url)
#                 dict = {'name': s, 'url': href_link, 'pid': id_from_url}
#                 final_arr_dict.append(dict)
#
#     element_with_id = soup.find(class_='hide-body hidden')
#     print(element_with_id)
#     if element_with_id:
#         for li in element_with_id.find_all('li'):
#             a_element = li.find('a')
#             s = ''
#             for a_tag in a_element:
#                 s += a_tag.text
#             print(s)
#             if a_element:
#                 href_link = a_element.get('href')
#                 print(href_link)
#
#                 id_from_url = extract_id_from_url(href_link)
#                 print(id_from_url)
#                 dict = {'name': s, 'url': href_link, 'pid': id_from_url}
#                 final_arr_dict.append(dict)
#
# print(final_arr_dict)

def contains_network_substring(input_string, network_set):
    for network_substring in network_set:
        if network_substring in input_string:
            return True
    return False

# Example usage
network = ('SIGCOMM', 'INFOCOM', 'IWQoS')
input_string = 'sdsadSIGCOmMasdsad'

result = contains_network_substring(input_string, network)
print(result)
