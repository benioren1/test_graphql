# readme.md

docker container run -d -p 5437:5437 --name psql-wwii tomer79sagi/wwii_missions
docker exec -it psql-wwii psql -U admin -d missions_db
docker compose down
docker compose build
docker compose up