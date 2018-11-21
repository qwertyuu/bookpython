# bookpython
Some selenium-based software to monitor your Saguenay library books


`pip install -r requirements.txt`

Create a "logs" folder in the root directory. It will hold all log files and rotate daily.


## Airtable

The "base" you use for airtable is yours to include.
 
Use the `.env.example` file to get started. (copy it as `.env`)

Your airtable table name should be `books` (case-sensitive) and have the following structure

| Column          |  Type   |
|-----------------|---------|
| ID              | Text    |
| Author          | Text    |
| Title           | Text    |
| Pages           | Integer |
| Renewed         | Integer |
| ScheduledReturn | Date    |
| ReturnedAt      | Date    |

The "updates" will be done automatically.
