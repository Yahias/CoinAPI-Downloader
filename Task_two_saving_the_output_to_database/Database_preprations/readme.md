
## Prepration for the database.
#### The below steps for database and tables creations.


#### Add the bin of postgreSQL to the path to be able to run pg commands:
    export PATH=/Library/PostgreSQL/{Postgree_version}/bin:$PATH
#### For example postgreSQL  version 10  :
    export PATH=/Library/PostgreSQL/10/bin:$PATH

#### 01- Create the database 
    - Open Terminal:
    Type the below command:
    (base) $ psql -h localhost -U postgres -d coin_api  -a -f TablesCreation.sql 

    - Enter the password of postgres user:
    Password for user postgres:
    



#### 02- Create the the tables 
    - Open Terminal:
    Type the below command:
 $ psql -h localhost -U postgres -d coin_api  -a -f TablesCreation.sql
    - Enter the  password of postgres user when promopted :
Password for user postgres:  


#### 03- Run the insertion Script to insert all our lookup table for currncies :

$ psql -h localhost -U postgres -d coin_api  -a -f cryptocurrencies_insertion.sql 