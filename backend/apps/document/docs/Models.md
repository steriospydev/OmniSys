# Document Models
---
## Invoice [ [TimeStamp](/backend/apps/tools/docs/Models.md) ]
- ID [PK, UUID4, UNIQUE]
- supplier [FK to Supplier m->m]
- invoice_no [int, NN]
- issue_date [datetime, NN]

- subtotal [decimal, Null]
- tax [decimal, Null]
- total [decimal, Null]

- unique_together [invoice_no, supplier ]

## InvoiceItem
- ID [PK, UUID4, UNIQUE]
- product [FK to Product, m->m]
- quantity [decimal, NN]
- unit_price [decimal, NN]

- tax [decimal, Null]
- subtotal [decimal, Null]
- total  [decimal, Null]

---
##### [Supplier Model](/docs/apps/product/docs/Models.md)
##### [Product Model](/docs/apps/product/docs/Models.md)
---
#### [Back to Readme.md](/docs/Readme.md) 
#### [Back to Models.md](/docs/backend/Models.md) 