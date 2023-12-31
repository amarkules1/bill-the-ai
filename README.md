# bill-the-ai

## Development

### Requirements
* Python 3.10
* pipenv
* Node.js/NPM

### Setup
* `pipenv install` - install python dependencies
* from `bill-ai-frontend` directory:
  * `npm install` - install frontend dependencies
  * `npm run build` - build frontend
* A postgres database with the vector extension is required. Run the table definitions in `/db_table_defs/` to create the necessary tables.
* create `.env` file in root directory with the following contents:
  ```
  OPENAI_API_KEY=<your openai api key>
  SENDGRID_API_KEY=<only needed for email interactions, you may need to change template IDs in /email_verification/ for this to work>
  LINODE_CONN_STRING=<connection string for a postgres database with the vector extension enabled>
  ```
* load vectors into the database using the jupyter notebook `setup_notebooks/bill_vector_setup.ipynb`

### Running

1. run app: `pipenv run flask --app main:app run`
2. Rebuild Front End: `npm run build` from `bill-ai-frontend` directory

## Deployment

Deployement is done using the provided dockerfile and startup script `start.sh`
In addition to the development requirements, you will need docker installed on the deployment server.
You will also need SSL Cert files `fullchain.pem` and `privkey.pem` in the root directory of the project.