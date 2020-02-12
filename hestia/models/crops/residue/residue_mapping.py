MODEL_MAPPING=dict(
    location=r'D:\ProArch\hestia\data\database.csv',
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'ON': 'removed',
        'OO': 'burnt_percent',
        'OP': 'burnt_kg',
        'OQ': 'above_ground_remaining',
        'OR': 'below_ground_remaining',
        'OS': 'total'
        }
)