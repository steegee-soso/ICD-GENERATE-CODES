# ICD-GENERATE-CODES
# APP SETUP COMMANDS

###### Run the Following comand below
####  THE application is serve on  127.0.0.1:5000/api/v1/

Some basic  commands to set the app up:
```
git clone https://github.com/steegee-soso/steegee-soso-generate-ICD-10-CODES-APP-.git
cd  steegee-soso-generate-ICD-10-CODES-APP-
docker-compose build
docker-compose up 


Documentation of ICD-1O Codes Endpoint

BACKEND LANGAUGE: Python
RDBMS: MYSQL
Framework:  Flask
Deployment Container: Docker

ENDPOINT= http://127.0.0.1:5000/

ENDPOINST	REQUEST METHODS	PAYLOADS	RESPONSE CODE	PAYLOADS FORMAT	ACTION
/api/v1/list	GET 	NONE	200	NONE	LIST ALL RECORDS
/api/v1/create	POST	PAYLOADS	201	JSON OBJECT	CREATE A NEW RECORD
/api/v1/delete/{id}	DELETE	NONE	200		DELETE A RECORD
/api/v1/update/{id}	PUT	PAYLOADS	200	JSON OBJECT	UPDATE A RECORD 
/api/v1/list/{id}	GET	NONE	200		LIST RECORDS WITH A SPECIFIC ID
/api/v1/list?start={0}&limit={20}	GET	NONE	200		LIST RECORD IN A PAGINATED FORM 
					

ENDPOINT PAYLOADS REQUEST BODY

ENDPOINT: http://127.0.0.1:5000/api/v1/create
 {
      "category_code": "A00", "diagnosis_code": "1235",
      "full_icd_code": "A001235", "abbreviated_description": "Comma-ind anal dop",
      "full_description": "Comma-induced anal retention",
      "category_title": "Malignant neoplasm of anus and anal canal",
       "icd_type": "ICD-10”
 }

 ENDPOINT: http://127.0.0.1:5000/api/v1/update /1
 {
      "category_code": "A00", "diagnosis_code": "1235",
      "full_icd_code": "A001235", "abbreviated_description": "Comma-ind anal dop",
      "full_description": "Comma-induced anal retention",
      "category_title": "Malignant neoplasm of anus and anal canal",
       "icd_type": "ICD-10”
 }

NB:
http://127.0.0.1:5000/api/v1/delete/1 
This endpoint Flag’s a status to “inactive” without deleting the record or removing the entire record from the row of the schema

INCREMENTATION OF ICD-10, ICD-9 CODES PROBLEM
An Additional schema table was introduce to associate or link  each ICD CODE   to their respective ICD-10  or ICD-9 code .This method will help to track various code and to support changes.
For Data integrity and consistence ICD_MIN_LENE, ICD_MAX_LEN are used validate the submitted ICD CODE submitted by user.
e.g
TABLE NAME : icd_records
ID(PK)	ICD_NAME	ICD_MIN_LEN	ICD_MAX_LEN	
1	ICD-10	3	7	

Id	Code_category	Diagnosis_code	Fullcode	Diagnosis 	Icd_record_id	
1	A00	123	A00123		1	



Deployment Instruction
git clone repo
cd ICD-GENERATE-CODES
docker-compose build 
docker-compose up


Local Deployment
1. Git clone repository to local machine
2. Change directory into the Project CD / product repo
4.Set up Local db(MSQL)
5. located a folder in the app directory called db.
6.Import the db.sql using any mysql client
3. Install venn env container to host app in a virtual container: Windows(python –m venv env ) Linux/MAC ( virtualenv venv ) pip install virtualenv
4. Activate the env folder: Windows command :(env\Scripts\Activate)  linux/mac/UNIX(venv/bin/activate )
5. Install Flask(Python Frame Work)  : pip install Flask
6. Run command python app.py to start the Flask app
7. To run a Test open a CMD /TERMINAL
8. Run command: python test.py  to run the test.
9.Test the Endpoints  with Postman 





 	



















