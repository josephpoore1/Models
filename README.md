A set of modules for creating structured data models from LCA observations and evaluating environmental aspects of specific farming cycle

This library is semnticaly structured to a set of modules that represent diferrent objects actions and results of LCA:

# Models


### Emisssions:

All emissions are being divided into groups

#### Chemical (chemical compounds):
Lists emissions as chemical compounds that are being created by a specific activity during a cycle, these include:
 **CH4, NO2, NOx, HN3, NO3, P, CO2**
 Each model has a property that represents amount of its total contributed by a activity or a source:
 - synthetic fertilizer
 - organic fertilizer
 - excreta
 - residue 
 - residue burn
 - urea, lime (applies to CO2 emissions)
 - total


#### Activities:
Lists the emission models that are generated in a cycle, and reflects an ipact of a farming activity these include:
- synthetic fertilizer
- organic fertilizer
- excreta
- residue
- residue burn
- emissions from production of fertilizers, pesticides and other inputs that are applied in a cycle
- emissions from production of machinery and infrastructure
- emissions from fuel used by machinery
- emissions from fuel and electricity for irrigation

## Model Mapping
Each model has at least one configuration file that points to the location of data source which holds it's values, it's type and 
property (column) map that defines what values to load and how to assign it:

    farm_infrastructure_mapping.py

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

#Data clients:
Set of modules that implement logic for loading data from file or directory storages 

# Factories (model builders):
A list of modules for constructing semantic objects from lca data. Each factory is a module that constructs a corresponding model
and uses data cliens to lload data and configuration file that describes the location of data source. 

    irrigation_factory = IrrigationFactory()
    irigation = irrigation_factory.create(20)


Factories can reuse each other to create complex obects:

    field_factory = FieldFactory()
    farm_factory = FarmFactory(field_actory)
    
    farm = farm_factory.create(20)


All factories can be combined into FarmedCropFactory which is responsibe for constructing a final object that can be used for 
calculating emissions.

    crop_builder.py
    
    ...
    mainFactory = FarmedCropFactory()
    model = mainFactory.create(20)
