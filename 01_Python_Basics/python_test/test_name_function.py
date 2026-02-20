from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Rohit Sharma' work?"""
    formatted_name = get_formatted_name('rohit', 'sharma')
    assert formatted_name == 'Rohit Sharma'


def test_first_last_middle_name():
    """Do names like 'Sachin Ramesh Tendulkar work' ?"""
    formatted_name = get_formatted_name('sachin', 'tendulkar', 'ramesh')
    assert formatted_name == 'Sachin Ramesh Tendulkar'
