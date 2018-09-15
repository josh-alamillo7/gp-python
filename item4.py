import pandas

def new_data_frame_without_duplicate_rows(data_frame, column_name):
  return data_frame.drop_duplicates(column_name)

sample_data_column_one = ['red', 'yellow', 'green', 'purple', 'blue']
sample_data_column_two = ['blue', 'orange', 'blue', 'green', 'yellow']
sample_data_column_three = ['orange', 'pink', 'pink', 'pink', 'orange']

sample_dictionary = {
  'col_1': sample_data_column_one,
  'col_2': sample_data_column_two,
  'col_3': sample_data_column_three
}

test_dataframe = pandas.DataFrame(data = sample_dictionary, columns = ['col_1', 'col_2', 'col_3'])

print new_data_frame_without_duplicate_rows(test_dataframe, 'col_1')
#should output an identical data frame
print test_dataframe is new_data_frame_without_duplicate_rows(test_dataframe, 'col_1')
#should be false
print new_data_frame_without_duplicate_rows(test_dataframe, 'col_2')
#row 3 should be removed
print new_data_frame_without_duplicate_rows(test_dataframe, 'col_3')
#rows 3, 4, 5 should be removed