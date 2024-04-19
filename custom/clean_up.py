import os
if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(data, *args, **kwargs):

    data = data[1]

    file = data['file']
    file_clean = data['file_clean']

    if os.path.exists(file):
        os.remove(file)
    if os.path.exists(file_clean):
        os.remove(file_clean)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    file = output['file']
    file_clean = output['file_clean']
    #assert os.path.exists(file) is false, f'{file} was not removed'
    #assert os.path.exists(file_clean) is false, f'{file_clean} was not removed'
