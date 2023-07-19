# def solution(A):
#     product = 1
#     for num in A:
#         product *= num

#     if product == 0:
#         return 0
#     elif product > 0:
#         return 1
#     else:
#         return -1

# def multiply_numeric(sequence, multiplier):
#     result = []
#     for element in sequence:
#         if isinstance(element, (int, float)):
#             result.append(element * multiplier)
#         return result
#     print(multiply_numeric)

def extract_domain_name(url):
    parsed_url = url.split("://")[-1].split("/")[0]
    if parsed_url.startswith("www."):
        parsed_url = parsed_url[4:]
    if parsed_url.endswith(".com"):
        parsed_url = parsed_url[:-4]
    return parsed_url

# Test cases
url1 = "https://www.example.com/page"
url2 = "http://subdomain.example.co.uk/path"
url3 = "https://www.subdomain.example.com"

print(extract_domain_name(url1))  # Output: "example"
print(extract_domain_name(url2))  # Output: "subdomain.example.co.uk"
print(extract_domain_name(url3))  # Output: "subdomain.example"
