from pandas import DataFrame
import pandas as pd
import os

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(data, *args, **kwargs):

    # load file from disk
    file = data['file']
    df = pd.read_parquet(file)

    # set date as index
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Date'}, inplace=True)

    # columnnames to drop
    to_drop = [col for col in df.columns if col[1] == 'Actual Consumption']
    df = df.drop(columns=to_drop)

    # drop second level column names
    df.columns = df.columns.droplevel(1)



    file_clean = f"{data['path']}{data['year']}-{data['month']}-{data['day']}_clean.parquet"
    df.to_parquet(file_clean)
    data['file_clean'] = file_clean


    return [df, data]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """

    columns = ['Date', 'Biomass', 'Fossil Brown coal/Lignite', 'Fossil Gas',
       'Fossil Hard coal', 'Fossil Oil', 'Geothermal', 'Hydro Pumped Storage',
       'Hydro Run-of-river and poundage', 'Hydro Water Reservoir', 'Other',
       'Other renewable', 'Solar', 'Waste', 'Wind Offshore', 'Wind Onshore']

    #assert output.shape == (96, 16), "export data frame doesn't have the right shape"
    #assert list(output.columns) == columns, "export data frame doesn't have the right column names"