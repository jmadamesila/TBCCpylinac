def read_baseline_csv(csv_path: str) -> dict:
    """
    Reads a baseline CSV file and returns data_location and data_value.
    
    Parameters:
        csv_path (str): Path to the baseline CSV file.
    
    Returns:
        dict: Dictionary containing 'data_location' and 'data_value'.
    """
    import pandas as pd
    
    df = pd.read_csv(csv_path)
    data_location = df['data_location'].tolist()
    data_value = df['mean_data_value'].tolist()
    return {
        'data_location': data_location,
        'data_value': data_value
    }