def generate_email_addresses(S, C):
    names = S.split(', ')
    email_map = {}

    def get_email_address(first_name, middle_name, last_name, company):
        formatted_last_name = last_name.replace('-', '')[:8].lower()
        first_part = first_name[0].lower()
        middle_part = middle_name[0].lower() if middle_name else ''
        email_part = f"{first_part}{middle_part}{formatted_last_name}@{company.lower()}.com"
        return email_part

    result = []
    for name in names:
        first_name, middle_name, last_name = name.split(' ')
        email = get_email_address(first_name, middle_name, last_name, C)

        if email not in email_map:
            email_map[email] = 1
        else:
            email_map[email] += 1
            email_map[name] = email_map[email]

        count = email_map[name]
        email_with_count = f"{email}{count}" if count > 1 else email
        result.append(f"{name} <{email_with_count}>")

    return ', '.join(result)




# Email Address

# You are given a list of names of new employees in a company. You need to generate a company email address for each of them.
# The name of each person consists of two or three parts: a first name, an optional middle name, and a last name, separated by spaces. Each part can include only English letters (but the last name may additionally contain hyphens). The name of the company also consists only of English letters Each address must use the format "FirstMiddleLast @Company.com' where
# • First is the initial of the first name,
# • Middle is the initial of the middle name (but only if the person has a middle name,
# • Last is the last name, truncated to at most 8 initial letters,
# • Company is the company name.
# The address should be in lower case and should not contain hyphens.
# Note that hyphens should be removed before truncating the last name.
# Additionally, if more than one person would have the same email address, differentiate their addresses by adding subsequent integers (starting from the second address and number 2) before the " " sign. For example, if there are three people who would have the address " jd@company. com", they should be assigned addresses " ja@company.com", " jd2@company.com" and
# "ja3@company.com" respectively.
# Write a function:
# function solution(S, C) /
# that, given a string $ containing a list of names separated by the characters","
# (a comma followed by a space)
# and a string C specifying the name of the company, returns a string containing the list of email addresses separated by the characters", " in the same order as they were in the input. Each entry on the list should be of the form Name ‹Emails"
# For example, given C = "Bxample" and string S as follows:
# "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker" the function should return:
# "John Doe <jdoe@example.com>, Peter Parker <pparker@example.com, Mary Jane Watson-Parker <m jwatsonpalexample.com>, James Doe < jdoe2@example.com>.
# John Elvis Doe <jedoe@example.com, Jane Doe <jdoe3@example.com>, Penny Parker <pparker2@example.com"
# A
# Assume that:
# • the length of string S is within the range [3.. 1,000];
# • the length of string c is within the range it...1001;
# • string S consists only of letters (a-z and/or A-2), spaces, hyphens and commas;
# • string S contains valid names; no name appears more than once;
# • string C is made only of letters (a-z and/or A-2).