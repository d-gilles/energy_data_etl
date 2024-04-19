from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(data: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.CLEAN_COLUMN_NAME

    Docs: https://docs.mage.ai/guides/transformer-blocks#clean-column-names
    """

    df = data[0]
    data = data[1]
    if 'nuclear' not in df.columns:
        df['nuclear'] = 0

    columnnames = ['date', 'biomass', 'fossil_brown_coal', 'fossil_gas',
       'fossil_hard_coal', 'fossil_oil', 'geothermal', 'hydro_pumped_storage',
       'hydro_run_of_river', 'hydro_water_reservoir', 'nuclear', 'other',
       'other_renewable', 'solar', 'waste', 'wind_offshore', 'wind_onshore']

    df.columns = columnnames

    return [df, data]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
