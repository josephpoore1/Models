MODEL_MAPPING=dict(
    location=r'D:\ProArch\hestia\data\database.csv',
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'RF': 'fallow_allocation',
        'RG': 'crop_allocation',
        'NN': 'cultivation_duration'
        }
)