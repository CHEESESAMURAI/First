import keyboa

START_TEST = keyboa.keyboa_maker(['Пройти тест'], copy_text_to_callback=True)
ANOTHER_TEST = keyboa.keyboa_maker(['Пройти другой тест'], copy_text_to_callback=True)
PLUS_MINUS = keyboa.keyboa_maker(['+', '-'], items_in_row=2, copy_text_to_callback=True,front_marker='ans_')
