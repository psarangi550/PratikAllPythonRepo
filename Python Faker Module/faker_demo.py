import faker
fake=faker.Faker("en-IN")
print(dir(fake))
# element=["Book","Hello"]
# print(fake.random_element(elements=element))
print(fake)
# print(dir(fake))
print((fake.phone_number()[1:]))

# _class__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__
# getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__'
# , '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_factories', '_factory_map', '_locales', '_ma
# p_provider_method', '_select_factory', '_unique_proxy', '_weights', 'aadhaar_id', 'aba', 'add_provider', 'address', 'administrative_unit', 'am_pm', 'an
# droid_platform_token', 'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email', 'bank_country', 'bban', 'binary', 'boolean', 'both
# ify', 'bs', 'building_number', 'cache_pattern', 'catch_phrase', 'century', 'chrome', 'city', 'city_name', 'city_suffix', 'color', 'color_name', 'compan
# y', 'company_email', 'company_suffix', 'coordinate', 'country', 'country_calling_code', 'country_code', 'credit_card_expire', 'credit_card_full', 'cred
# it_card_number', 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency', 'cryptocurrency_code', 'cryptocurrency_name', 'csv', 'currency'
# , 'currency_code', 'currency_name', 'currency_symbol', 'current_country', 'current_country_code', 'date', 'date_between', 'date_between_dates', 'date_o
# bject', 'date_of_birth', 'date_this_century', 'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between'
# , 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_
# week', 'del_arguments', 'dga', 'domain_name', 'domain_word', 'dsv', 'ean', 'ean13', 'ean8', 'email', 'factories', 'file_extension', 'file_name', 'file_
# path', 'firefox', 'first_name', 'first_name_female', 'first_name_male', 'first_name_nonbinary', 'fixed_width', 'format', 'free_email', 'free_email_doma
# in', 'future_date', 'future_datetime', 'generator_attrs', 'get_arguments', 'get_formatter', 'get_providers', 'hex_color', 'hexify', 'hostname', 'http_m
# ethod', 'iana_id', 'iban', 'image', 'image_url', 'internet_explorer', 'ios_platform_token', 'ipv4', 'ipv4_network_class', 'ipv4_private', 'ipv4_public'
# , 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'items', 'job', 'json', 'language_code', 'language_name', 'last_name', 'last_name_female', 'last_name_male', '
# last_name_nonbinary', 'latitude', 'latlng', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor', 'local_latlng', 'locale', 'locales',
# 'localized_ean', 'localized_ean13', 'localized_ean8', 'location_on_land', 'longitude', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'mi
# me_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 'name_male', 'name_nonbinary', 'nic_handle', 'nic_handles', 'null_boolean', 'numerify
# ', 'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'past_date', 'past_datetime', 'phone_number', 'port_number', 'postcode', 'prefix', 'prefix_
# female', 'prefix_male', 'prefix_nonbinary', 'pricetag', 'profile', 'provider', 'providers', 'psv', 'pybool', 'pydecimal', 'pydict', 'pyfloat', 'pyint',
#  'pyiterable', 'pylist', 'pyset', 'pystr', 'pystr_format', 'pystruct', 'pytimezone', 'pytuple', 'random', 'random_choices', 'random_digit', 'random_dig
# it_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'random_elements', 'random_int', 'random_letter', 'random_le
# tters', 'random_lowercase_letter', 'random_number', 'random_sample', 'random_uppercase_letter', 'randomize_nb_elements', 'rgb_color', 'rgb_css_color',
# 'ripe_id', 'safari', 'safe_color_name', 'safe_domain_name', 'safe_email', 'safe_hex_color', 'seed', 'seed_instance', 'seed_locale', 'sentence', 'senten
# ces', 'set_arguments', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state', 'street_address', 'street_name', 'street_suffix', '
# suffix', 'suffix_female', 'suffix_male', 'suffix_nonbinary', 'swift', 'swift11', 'swift8', 'tar', 'text', 'texts', 'time', 'time_delta', 'time_object',
#  'time_series', 'timezone', 'tld', 'tsv', 'unique', 'unix_device', 'unix_partition', 'unix_time', 'upc_a', 'upc_e', 'uri', 'uri_extension', 'uri_page',
#  'uri_path', 'url', 'user_agent', 'user_name', 'uuid4', 'weights', 'windows_platform_token', 'word', 'words', 'year', 'zip']
# <faker.proxy.Faker object at 0x0089F6E8>