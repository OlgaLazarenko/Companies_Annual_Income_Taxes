# Companies_Annual_Income_by_Income_Type

The project uses the data available here: [Income of Companies by Income Type, Annual](https://data.gov.sg/dataset/income-of-companies-by-income-type-annual?resource_id=3b64eaf4-78d7-4312-8167-1a423b83d0db)

#### The dataset consists of the files:
- [Chargeable Income of Companies](https://data.gov.sg/dataset/income-of-companies-by-income-type-annual?resource_id=3b64eaf4-78d7-4312-8167-1a423b83d0db)
- [Chargeable Income of Companies by Tax Group](https://data.gov.sg/dataset/income-of-companies-by-income-type-annual?resource_id=ec8ed20b-707f-41a6-80d0-1f2be8025261)
- [Income of Companies by Income Type](https://data.gov.sg/dataset/income-of-companies-by-income-type-annual?resource_id=83b36d2e-6d2a-47d0-8042-415db84442e9)
- [Income of Companies by Tax Group and Income Type](https://data.gov.sg/dataset/income-of-companies-by-income-type-annual?resource_id=be33c464-7566-402d-87e2-07ccf07c251d)

### The purpose of the project:
Read the initial datasets, perform data cleansing, create visualizations 
#### Using Python
- [x] Read the data from the dataset creating Python code
- [] Validate data, remove the rows with errors
- [] Save the validated data in the output file; invalid data will be saved in the error file
#### Using Pandas
- [] Read the output file with validated data using Pandas
- [x] Remove rows with duplicates at the column 'year_of_assessment'
- [x] Sort the data by the column 'year_of_assessment' ascening order 
- [] Create new columns, calculate the values 
- [] Choose columns to create visualizations
- [] Create the data visualizaitons to show the trends
#### Because of the need to validate integer/ or decimal values, create global functions which can called for different projects 
- [] to validate years
- [] to validate numeric values
- [] create global variables
