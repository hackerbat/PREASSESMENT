### Q1 - Run a flask app inside docker container.Your local should run on 5000 and flask should run on 8080.

* Build a docker image using the command 

		docker build -t flask:v1
* We have to map our local 5000 port with 8080 because our app is running on 8080. We can do that with the following command.
		
		docker run -d -p 5000:8080 flask:v1
		
* Run the following command to check the existing containers.

		docker ps
		
Screenshots :

* Browser output :

![](https://raw.githubusercontent.com/hackerbat/PREASSESMENT/master/Docker/images/browser-output.png)

* Commands : 

![](https://raw.githubusercontent.com/hackerbat/PREASSESMENT/master/Docker/images/commands-history.png)						