## TimeStamp [ Abstract]
- created_at [ Datetime ]
- updated_at [ Datetime ]
## Contact [ Abstract]
- ID [PK, UUID4, UNIQUE]
- address [varchar(100), Null]
- city [varchar(100), Null]
- area [varchar(100), Null]
- zipcode [varchar(5), Null]
- email [varchar(100), Null]
- phone [varchar(10), Null]

# AmountValidation
- Provides validation of the amount field in Income and Payment models