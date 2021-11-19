# define helper functions for pipeline of data processing 
# diffs and rolling averages both require a date column (of date type)
def create_proportion(data, col_name, total_col, output_name=False):
    if not output_name:
        output_name = col_name + '_rate'
    data_copy = data.copy()
    data_copy.loc[:,output_name] = data[col_name] / data[total_col]
    return data_copy 

def create_proportions(data, cols, total_col):
    for col_name in cols:
        data = create_proportion(data, col_name, total_col)
    return data 


def create_diff(data, col_name, output_name=False):
    if not output_name:
        output_name = col_name + '_diff'
    sorted_data = data.sort_values(by="Date")
    sorted_data.loc[:,output_name] = sorted_data.loc[:,col_name].diff()
    return sorted_data

def create_diffs(data, cols):
    for col_name in cols:
        data = create_diff(data, col_name)
    return data

def create_rolling_average_by_time(data, col_name,  window_offset, 
                                   output_name = False, date_col="Date"):
    if not output_name:
        output_name = col_name + '_rolling_avg_' + str(window_offset)
    temp_df = (data[[date_col,col_name]]
           .set_index(date_col)
           .sort_index()
           .rolling(window_offset).mean().reset_index()
           .rename(columns={col_name:output_name})
          )
    #requires day col to be unique! 
    data = data.merge(temp_df, how="left", left_on=date_col, right_on=date_col)
    return data

def create_rolling_averages_by_time(data, cols, window_offset):
    for col_name in cols:             
        data = create_rolling_average_by_time(data, col_name, window_offset)
    return data