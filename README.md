# chc
**Description:** As specified in the requirement doc , Implemented a web application using Python flask. The web app returns a string , version and environment as per the specified requirements.

**Application:** This application is a simple flask service runs on a docker container.

**Softwares and packages:** Python 3.8 , flask , requests.

**Conterisation:** Used docker compose for container orchestration. The container runs on a AWS EC2 instance exposed on port:5000

**Diagrams:** 

CHC-INFRA.png - Infrastructure diagram of the deployed application

CHC-PROD.jpeg - Deployment Lifecycle

**How to Run the application:**

Step 1: Clone the Git repo

Step 2: navigate to dir chc-main

Step 3: Run the below command to launch the application

_$docker-compose up --build_

Step 4: check container status 

_$docker ps_

Step 5: copy and paste the url in a browser  and keep refreshing to see the page to see different results

http://54.173.9.239:5000/getString
