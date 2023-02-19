"""
    Первый запрос
    select * from test.customers cust, test.cities cit
    where cust.city_id = cit.id
"""
"""
    Второй запрос
    select * from test.customers cust
    inner join test.cities on cust.city_id = cities.id
"""
"""
    Третий запрос
    select cit.id as cit_id ,cit.name city_name, string_agg(c.name, ',') custumers
    from test.cities cit
    inner join test.customers c on cit.id = c.city_id
    group by cit.id
"""
