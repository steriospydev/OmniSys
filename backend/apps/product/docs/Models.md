
## Category 
- ID [PK, UUID4, UNIQUE]
- category_name [NN,varchar(100), UNIQUE]
## Brand 
- ID [PK, UUID4, UNIQUE]
- brand_name [NN,varchar(100), UNIQUE]
## Package 
- ID [PK, UUID4, UNIQUE]
- material [choice, default='Other']
- package_unit [choice NN]
- package_quantity [decimal NN]
* Unique thogether: [material, package_unit, quantity]

## Tax_rate 
- ID [PK, UUID4, UNIQUE]
- value [decimal NN Unique]

## Product [ TimeStamp ]
- ID [PK, UUID4, UNIQUE]
- category [FK many->many]
- brand [FK]
- tax_rate [FK]
- summary [varchar, null]
- is_active [bool, default=true]
- available [bool, default=true]


* [TimeStamp](/app/backend/apps/tools/docs/Models.md) 
* [Material, Package Units](/app/backend/apps/tools/docs/ChoiceFields.md) 



#### [Back to Readme](/app/docs/Readme.md) 
#### [Back to Models](/app/docs/backend/Models.md) 