import json
import pandas as pd



def filter_can(data, filter_value, filter_type='id'):
    if filter_type == 'id':
        if isinstance(filter_value, int):
            filter_value = [filter_value]
        filtered_data = [frame for frame in data if frame['can_id'] in filter_value]
    elif filter_type == 'name':
        filtered_data = [frame for frame in data if 'signals' in frame and filter_value in frame['name']] # fix this 
    else:
        raise ValueError("filter_type must be either 'id' or 'name'")
    
    return filtered_data


def get_available_data(data):
    # Initialize a set to hold the unique names
    unique_names = set()

    for item in data:
        if 'name' in item:
            unique_names.add(item['name'])
        # else:
        #     print("Warning: 'name' key missing in data entry:", item)

    return unique_names

def save_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


# Function to safely extract and prepare data from the provided format
def extract_data(frames):
    result = []
    for frame in frames:
        base_info = {key: frame[key] for key in frame if key not in ['signals', 'can_id', 'name']}
        signals = frame.get('signals', {})
        full_info = {**base_info, **signals, 'timestamp': pd.to_datetime(frame['timestamp'], unit='s')}
        result.append(full_info)
    return result