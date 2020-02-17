MODEL_MAPPING=dict(
    location=r'D:\ProArch\hestia\data\database.csv',
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'I': 'country',
        'MI': 'crop_name',
        'PC':' slope',
        'PB': 'slope_len',
        'OX': 'sand',
        'OW': 'clay',
        'PA': 'phos',
        'OV': 'phH2O',
        'OY': 'org_carbon',
        'PE': 'loss_to_aquatics',
        'OZ': 'nitrogen',
        'PF': 'erodibility',
        'PD': 'drainage'
    }
)