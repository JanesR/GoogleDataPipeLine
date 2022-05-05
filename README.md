# GoogleDataPipeLine
Data pipeline  with Python to Google Cloud Plataform

pt-br
## Components

- Fornece os objetos e métodos para geração de arquivos parquet, envio para Google cloud storage e cargas de arquivos em tabelas do Big query.

### Components.OperationFiles

- Responsável pela manipulação de arquivos.

### Components.DataBase

- Responsável pela comunicação com as bases de dados. Podendo se comunicar com 3 tipos diferentes de banco:
    - Sql Server
    - MySQL
    - PostgreSQL

### Components.CloudStorage

- Responsável pela comunicação o Google Cloud Storage para envio de arquivos para buckets especificos.

## Dependencias
- google-cloud-bigquery
- google-cloud-storage
- pandas
- sqlalchemy
- pyarrow
- fastparquet
- configparser
- pymssql
- pymysql
- pyodbc

___

English

## Components

- Provides the objects and methods for generating parquet files, sending them to Google cloud storage and loading files into Big Query tables.

### Components.OperationFiles

- Responsible for handling files.

### Components.DataBase

- Responsible for communication with the databases. Being able to communicate with 3 different types of bank:
    - sql server
    - MySQL
    - PostgreSQL

### Components.CloudStorage

- Responsible for communicating Google Cloud Storage to send files to specific buckets.

___

## Dependencies
- google-cloud-bigquery
- google-cloud-storage
- pandas
- sqlalchemy
- pyarrow
- fastpark
- configparser
- pymssql
- pymysql
- pyodbc