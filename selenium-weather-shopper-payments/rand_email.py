import random
import string
from random import randint

def random_mail():

    random_word = ''.join([random.choice(string.ascii_lowercase) for n in range(6)])
#print(random_word)
    domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com", "qxf2.com"]
    domain_item = random.choice(domains)
    email = random_word + '@' + domain_item
    return email

def random_zip(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_phone(n):
    rng_start = 10**(n-1)
    rng_stop = (10**n)-1
    return randint(rng_start, rng_stop)

def random_cvv(n):
    range_strt = 10**(n-1)
    range_stop = (10**n)-1
    return randint(range_strt, range_stop)
