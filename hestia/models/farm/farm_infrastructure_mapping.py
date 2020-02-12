MODEL_MAPPING=dict(
    location=r'D:\ProArch\hestia\data\database.csv',
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'RF': 'energy_electricity',
        'RG': 'energy_disel',
        'NN': 'amount',
        'NO': 'hours',
        'NP': 'plastic',
        }
)