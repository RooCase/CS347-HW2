# Alpine is a very small/lightweight Linux distribution
# We are starting from an alpine image with Python 3 installed
FROM postgres

# The WORKDIR command both creates a directory in the container 
# and sets that directory to be the current directory for all further commands
WORKDIR /tests

# We set some Environment variables in the container which Flask uses
# ENV POSTGRES_USERNAME=admin
ENV POSTGRES_PASSWORD=CS347
ENV POSTGRES_DB=test

# We want port 5000 (the default Flask port) to be used outside the container
# expose postgre's port
EXPOSE 8000

# We copy everything in the current directory on our machine 
# ... into the working directory in the container 
# (In particular, this includes api.py)
# COPY . . 
COPY tests.sql /docker-entrypoint-initdb.d/

 
