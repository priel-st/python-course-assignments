import dig_count

def test_join_numbers():
    assert dig_count.join_numbers([123,455,1]) == '1234551'
    
def test_digit_list():
    assert dig_count.digit_list('1231230') == ['0', '1', '2', '3']
