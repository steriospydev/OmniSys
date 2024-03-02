## PayeeLabel [TimeStamp]
- ID [PK, UUID4, UNIQUE]
- name [NN,varchar(100), UNIQUE]

## Payee [TimeStamp]
- ID [PK, UUID4, UNIQUE]
- label [FK to PayeeLabel]
- name [NN,varchar(100), UNIQUE]
- summary [varchar(150), NULL]
- active [bool, default=True]

## Payment [TimeStamp, AmountValidation]
- ID [PK, UUID4, UNIQUE]
- payee [FK to Payee]
- amount [Decimal, NN]
- payment_day [datetime, NN]
- paid [bool, default=true] 
- summary [varchar(150), NULL]

## Source [TimeStamp]
- ID [PK, UUID4, UNIQUE]
- source [varchar(50) ,NN, Unique]
- summary [varchar(150), NULL]

## Income [TimeStamp, AmountValidation]
- ID [PK, UUID4, UNIQUE]
- source [FK to Source]
- amount [Decimal, NN]
- income_day [datetime, NN]
- summary [varchar(150), NULL]



##### [TimeStamp, AmountValidation](/backend/apps/tools/docs/Models.md) 
#### [Back to Models.md](/app/docs/backend/Models.md) 
