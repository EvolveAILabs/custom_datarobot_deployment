import pandas as pd
import numpy as np

def load_model(input_dir):
    """Custom model hook for loading our knowledge base."""
    return True

def score_unstructured(model, data, query, **kwargs) -> str:
    """Custom model hook for making completions with our knowledge base."""
    import json
    try:
        data_dict = json.loads(data)
        num_matrices = data_dict['num_matrices']
        row_count = data_dict['row_count']
        col_count = data_dict['col_count']
        matrix_list = []
        for i in range(num_matrices):
            matrix_list.append(np.random.randint(0, 100, (row_count, col_count)))
        rv = pd.Series(matrix_list).to_json(orient='values')
    except Exception as e:
        rv = {'error': f"{e.__class__.__name__}: {str(e)}"}
    return json.dumps(rv)