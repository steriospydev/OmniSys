
## Category 
- ID [PK, UUID4, UNIQUE]
- category_name [NN,varchar(100), UNIQUE]
## Brand 
- ID [PK, UUID4, UNIQUE]
- brand_name [NN,varchar(100), UNIQUE]

## Package 
- ID [PK, UUID4, UNIQUE]
- material [choice, default='Other']
- package_unit [choice ]
- package_quantity 

## Tax_rate 
- ID [PK, UUID4, UNIQUE]

## Product [ TimeStamp ]
- ID [PK, UUID4, UNIQUE]


* [TimeStamp](/app/backend/apps/tools/docs/Models.md) 
* [Material, Package Units](/app/backend/apps/tools/docs/ChoiceFields.md) 



#### [Back to Readme.md](/app/docs/Readme.md) 
#### [Back to Models.md](/app/docs/backend/Models.md) 