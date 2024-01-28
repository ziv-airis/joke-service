# chuck-norris-jokes
Chuck Norris Jokes server

### Endpoints
**GET /joke**</br>
Get Chuck Norris joke 

**Headers**
|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `Authorization` | required | string  | Your account authorization.                                                                     |
**Response**
```
{
    "id": "F6v0fEXeREek9FnF6_9k4A",
    "categories": ["some category"],
    "createdAt": "2020-01-05 13:42:25.352697",
    "joke": "Chuck Norris' first car was Optimus Prime."
}
```
First you will need to run the service locally.
In order to run a requst run one you can use the following request request
```bash
curl --location --request GET 'http://localhost:8000/joke' \
--header 'Authorization: 1111-2222-3333'
```
*******
The project is under the `joke-service` folder.
First create virtualenv and activate it

#### Installation
`pip install -r /path/to/requirements.txt`

#### Run tests
To run the service tests
`pytest`

#### Run the server
To run the service you can use this command
`uvicorn main:app`


## Solution:
### First phase:
#### Create new docker image
To create new image you can use this command from root directory
Need to choose a version i.e 1.0 instead of <version>
`docker build -t joke-service:<version> .`

#### Run the server using docker
To run the service you can use this command from root directory
Need to choose a version i.e 1.0 instead of <image_version>
and i.e 1 instead of <container_version>
`docker run -p 8000:8000 --name joke-service<container_version> joke-service:<image_version>`

#### CI pipeline
For every push to master a github action will be triggered and will run the following:
    1. Run unit tests for the Joke Service. (pytest)
    2. Build a Docker image of the service withot pushing it.

### Second phase:
#### Docker compose
To run all the services you can use this command from root directory:
docker compose up
To make the ELK run I needed to create a docker compose with the following services:
1. joke-service
2. filebeat
3. elasticsearch 
4. kibana

#### Logs:
To see the logs inside the sqlite DB Run:
1. docker exec -it <joke-service-container-id> /bin/bash
2. sqlite3 /path/to/your/log.db
3. SELECT * FROM logs;

#### Kibana
Uploaded to: port 5601, you can see in discover logs after you will create a few requests:
http://localhost:5601/app/discover