MODEL_MAPPING=dict(
    location=r'D:\ProArch\hestia\data\database.csv',
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'OT': 'type',
        'NS': 'amount_applied',
        'NU': 'energy_fuel',
        'NT': 'energy_electr'
        }
)