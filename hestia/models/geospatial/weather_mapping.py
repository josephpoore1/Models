MODEL_MAPPING=dict(
    location=r'D:\ProArch\hestia\data\database.csv',
    location_type='file',
    data_format='csv',
    separator='|',
    id_key='id',
    column_names={
        'AQ': 'id',
        'MI': 'crop_name',
        'PJ': 'pet',
        'PH': 'winter_type_corr',
        'PI': 'avg_temp',
        'PG': 'precip',
        'PK': 'eco_clim_zone',
        }
)