{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "62292529",
   "metadata": {
    "_cell_guid": "25a46d06-e1d3-4dda-abca-22330f5d74c5",
    "_uuid": "6ad49588-4059-4232-b03d-ff3a18051776",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2024-07-13T10:16:56.075535Z",
     "iopub.status.busy": "2024-07-13T10:16:56.075139Z",
     "iopub.status.idle": "2024-07-13T10:16:56.873035Z",
     "shell.execute_reply": "2024-07-13T10:16:56.872072Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.803875,
     "end_time": "2024-07-13T10:16:56.875586",
     "exception": false,
     "start_time": "2024-07-13T10:16:56.071711",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "\n",
    "def filter_can(data, filter_value, filter_type='id'):\n",
    "    if filter_type == 'id':\n",
    "        if isinstance(filter_value, int):\n",
    "            filter_value = [filter_value]\n",
    "        filtered_data = [frame for frame in data if frame['can_id'] in filter_value]\n",
    "    elif filter_type == 'name':\n",
    "        filtered_data = [frame for frame in data if 'signals' in frame and filter_value in frame['name']] # fix this \n",
    "    else:\n",
    "        raise ValueError(\"filter_type must be either 'id' or 'name'\")\n",
    "    \n",
    "    return filtered_data\n",
    "\n",
    "\n",
    "def get_available_data(data):\n",
    "    # Initialize a set to hold the unique names\n",
    "    unique_names = set()\n",
    "\n",
    "    for item in data:\n",
    "        if 'name' in item:\n",
    "            unique_names.add(item['name'])\n",
    "        # else:\n",
    "        #     print(\"Warning: 'name' key missing in data entry:\", item)\n",
    "\n",
    "    return unique_names\n",
    "\n",
    "def save_to_json(data, path):\n",
    "    with open(path, 'w') as f:\n",
    "        json.dump(data, f, indent=4)\n",
    "\n",
    "\n",
    "# Function to safely extract and prepare data from the provided format\n",
    "def extract_data(frames):\n",
    "    result = []\n",
    "    for frame in frames:\n",
    "        base_info = {key: frame[key] for key in frame if key not in ['signals', 'can_id', 'name']}\n",
    "        signals = frame.get('signals', {})\n",
    "        full_info = {**base_info, **signals, 'timestamp': pd.to_datetime(frame['timestamp'], unit='s')}\n",
    "        result.append(full_info)\n",
    "    return result"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 5381353,
     "sourceId": 8943269,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 30746,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 3.842044,
   "end_time": "2024-07-13T10:16:57.297676",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-07-13T10:16:53.455632",
   "version": "2.5.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
