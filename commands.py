# DOCKER COMMANDS

'''
1. To Build image :- 
    $ command :- docker build -t name:tag .
        " adding . at the last is necessary to specify the dir(current) from which the docker should start copying"

2. Verify images :- 
    $ command :- docker images

3. Build container :- 
    $ command :- docker run --name container_name -p host_port:container_port image_name:tag
    $ simmple :- docker run -p 8000:8000 image_name:image_tag
         -- " first 8000 is the port is of our local machine and 2nd 8000 is of docker enviornment"
 
4. TO DELETE IMAGE :-
    $ command :- docker rmi image_name:tag
    $ commad :- docker rmi image_id

5. FORCE DELETE EVEN IF A CONTAINER IS RUNNING
    $ command :- docker emi -f iamge_name:tag
    $ command :- docker emi -f image_id

6. LIST ALL CONTAINERS:
    $ command( running container ) :- docker ps
    $ command(all containers) :- docker ps -a

7. STOP A RUNNING CONTAINER:
    $ command :- docker stop <container_id or container_name>

8. START A STOPPED CONTAINER:
    $ command :- docker start <container_id or container_name>

9. REMOVE A CONTAINER:
    $ command :- docker rm <container_id or container_name>

10. VIEW LOGS OF A CONTAINER:
    $ command :- docker logs <container_id or container_name>

11. TO VIEW CONTENT OF A FILE IN A CONTAINER:
    $ command :- cat file_name

12. MOUNT .env ON A CONTAINER
    $ command :- docker run --name name --env-file path/to/.env -p 8000:8000 image_name:tag

13. copy FILES/CHANGES FROM REPO ON LOCAL INTO REPO ON DOCKER CONTAINER
    $ command :- docker cp /path/on/host/file <container_name_or_id>:/path/to/container

14. MOUNT FILES FROM REPO ON DOCKER CONTAINER INTO REPO ON LOCAL
    $ command :- docker cp <container_name_or_id>:/path/to/container/file /path/on/host

'''