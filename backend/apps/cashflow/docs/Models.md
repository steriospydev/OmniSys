## PayeeLabel [TimeStamp]
- ID [PK, UUID4, UNIQUE]
- label_name [NN,varchar(100), UNIQUE]

## Payee [TimeStamp]
- ID [PK, UUID4, UNIQUE]
- label_id [FK to PayeeLabel]
- name [NN,varchar(100), UNIQUE]
- summary [varchar(150), NULL]

## Payment [TimeStamp]
- ID [PK, UUID4, UNIQUE]
- payee_id [FK to Payee]
- amount [Decimal, NN]
- payment_day [datetime, NN]
- paid [bool, default=true] 
- summary [varchar(150), NULL]

## Source [TimeStamp]
- ID [PK, UUID4, UNIQUE]
- source [varchar(50) ,NN, Unique]
- summary [varchar(150), NULL]

## Income [TimeStamp]
- ID [PK, UUID4, UNIQUE]
- source_id [FK to Source]
- amount [Decimal, NN]
- income_day [datetime, NN]
- summary [varchar(150), NULL]



- [TimeStamp](/app/backend/apps/tools/docs/Models.md) 


























#### [Back to Readme.md](/app/docs/Readme.md) 
#### [Back to Models.md](/app/docs/backend/Models.md) 