A set of modules for creating structured data models from LCA observations and evaluating environmental aspects of specific farming cycle

This library is semnticaly structured to a set of modules that represent diferrent objects actions and results of LCA:

# Models

## Farm observations
Contains models that semanticaly grop properties that describe farming activities, inputs, environment and crop characteristics. The 
model used has the following structure:
├───activities
│   ├───fertilizers
│   │   ├───excreta
│   │   │   └───__pycache__
│   │   ├───organic
│   │   │   └───__pycache__
│   │   ├───synthetic
│   │   │   └───__pycache__
│   │   └───__pycache__
│   ├───irrigation
│   │   └───__pycache__
│   ├───pesticides
│   │   └───__pycache__
│   ├───processing
│   │   └───__pycache__
│   └───__pycache__
├───coefficients
│   ├───conversions
│   ├───crop
│   ├───residue
│   ├───residue_burn
│   ├───soil
│   ├───weather
│   └───__pycache__
├───crops
│   ├───residue
│   │   └───__pycache__
│   └───__pycache__
├───emissions
│   ├───activities
│   ├───chemical
│   │   └───__pycache__
│   ├───environment
│   └───sources
├───farm
│   ├───irrigation
│   ├───machinery
│   │   └───__pycache__
│   └───__pycache__
├───geospatial
│   └───__pycache__
├───measures
│   ├───irrigation_types
│   └───__pycache__
├───references
│   └───__pycache__
└───__pycache__


farmed crop:
  |--seed
  |--farming_period
  |--Field
     |--Land
       |--area
       |--sp
       |--country
       |--geography
       |--Location
       |  |--slope
       |  |--slope_length
       |  |--Position
       |     |--lat
       |     |--lon
       |--soil
          |--phH20
          |--clay
         - sand
         - nitrogen
         - phosphorus
         - org_carbon
         - drainage_class
         - loss_to_auqatics
         - erodibility
       - weather
         - precipitation
         - average_temperature
         - winter_type_corr
         - pet
         - eco_clim_zone
           - name
           - value
           - c_class
           - c_nox_N
           - c_n2o_N
  - infrastructure
     - 
  - activities
     - fertilizing
     - irrigation
     - pest_management
     - residue_management
     - land_management
     - crop_processing
  - crop_yield
     - dry_matter
     - marketable
  - 

## References
This includes scalar values, vectors and tables that represent standardisationvalues that can be used to calculate emissions.


## Emisssions:
All emissions are being divided into 2 groups chemical emissions  and activity emissions

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

Each of emission models exposes a single public method that can be used to calculate it's properties based on the lifecyle model:

    crop = FarmedCrop()
    ch4_emissions = Ch4Emissions(references)
    
    ch4_emissions.calculate_for(crop)
    
    print(ch4.residue_burn)
    # 0.342

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

# Data clients:
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
