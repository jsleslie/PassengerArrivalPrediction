# Author: Jarome Leslie
# Date: 2020-02-05
#
"""Reads in pdf data and performs the necessary wrangling and transformations to create a tidy csv.

Usage: src/process_pdf_passengers.py --path_in=<path_in> --path_out=<path_out>

Options:
--path_in=<path_in>    Path (including filename) of where to read source data
--path_out=<path_out>    Path (excluding filename) of where to locally write the file

"""

import numpy as np
import pandas as pd


from docopt import docopt
import requests
import os


from tabula import read_pdf
import pandas as pd


opt = docopt(__doc__)

def wrangler(input_path, output_path):
    #pdf table area bounds
    y1 =104.08
    x1 = 168.28
    y2 = y1+1062.22
    x2 = x1+455.83
    table_dims = (y1,x1,y2,x2)

    # Read in pdf file for the selected area
    yvr_pass_df = read_pdf(input_path, area = table_dims,pandas_options={'header':None})[0]

    # Add column names
    yvr_pass_df.columns = ['Year','Type','January','February','March','April','May','June',
                        'July','August','September','October','November','December','Total']

    # Fill in missing year values
    yvr_pass_df['Year'] = yvr_pass_df['Year'].fillna(method = 'ffill')

    # Drop annual counts, leaving the monthly values
    yvr_pass_df = yvr_pass_df.drop(columns=['Total'])

    # Melt the wide columns into a month variable
    yvr_pass_df = pd.melt(yvr_pass_df, id_vars=['Year','Type'], var_name = 'Month', value_vars=['January','February','March','April','May','June',
                        'July','August','September','October','November','December'], value_name='Passengers' )

    # Convert the floats in the `Year` column to integers
    yvr_pass_df['Year'] = yvr_pass_df['Year'].map(int)

    # Write `yvr_pass_df` to a csv file
    yvr_pass_df.to_csv(output_path, index=False)

def main(path_in, path_out):
    wrangler(path_in, path_out)

if __name__ == "__main__":
    main(opt["--path_in"], opt["--path_out"])


# python src/process_pdf_passengers.py --path_in=data/YVR_Passengers.pdf --path_out=data/tidy_YVR_passengers.csv