simple script to collect data from twitter and presist it in postgress database
Before running the script make sure you create env.py file in your director and add the following variables:

- Twitter API Bearer Token
bearer_token="XXXX"
- Postgress Database URI:
DB_URI=engine = f'postgresql://user:pass.@host:port/Database_Name'