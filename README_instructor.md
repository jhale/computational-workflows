# Instructor instructions

## Preparation instructions

1. Get an account on https://github.com
2. Make sure you have the git version control system setup: https://help.github.com/en/github/getting-started-with-github/set-up-git
3. Clone the repository ``git@github.com:jhale/computational-workflows.git``.
4. Install Docker on your computer https://www.docker.com/products/docker-desktop or https://docs.docker.com/install/
5. Please read the paper https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005510&type=printable

## Technical setup

1. Switch to ``/bin/bash`` shell.
2. Run ``swc-shell-split-window``.
3. Instruct students to go to: https://pad.carpentries.org/comp-workflows

## Overview

* 2 hours: Docker. *Specifying and running software anywhere*.
* 2 hours: Unit testing with Python and pytest.
* 2 hours: Continuous integration on github.

* We will learn together by *doing* things.
* We will use a top-down learning style (broad picture first, details last).

## Docker

Reference material:

* The docker cheat sheet: https://github.com/wsargent/docker-cheat-sheet
* https://ieeexplore.ieee.org/document/7933304 Containers for Portable, Productive, and Performant Scientific Computing (Hale et al.)
* https://docs.docker.com/
* https://fenics.readthedocs.io/projects/containers/en/latest/

Points to cover:

* What is Docker?
  * Docker is a software tool designed to make it easy to create, deploy
    and run applications by using containers.
* What is a container.
  * Package up an application and all of the parts it needs (libraries, configuration)
    into a *single* package.
* Ensures that the application runs *identically* on any machine, regardless
  of any customisations on that machine.

* What *problems* does Docker solve *in a scientific computing context*?
  * *Portability, collaboration.*
    * My colleague wants to run my code, but:
      * he is running a different operating system.
      * she has installed a different version of software package x.
  * *Reproducibility.*
    * I want to publish my code and software so that someone else can run them.
    * I want to be able to reproduce my results in 5 years.
  * *High-performance computers (HPC)*
    * I won't cover this in this course, see Hale et al. and https://sylabs.io/docs/

## Installing Docker

Docker is available for Linux, Mac OS and Windows.

https://www.docker.com/products/docker-desktop
https://docs.docker.com/install/linux/docker-ce/ubuntu/
https://docs.docker.com/install/linux/docker-ce/debian/
https://docs.docker.com/install/linux/docker-ce/fedora/

## Testing Docker for the first time

    docker run hello-world

## Getting a bit more interesting

    docker run -it ubuntu bash

* `docker` the docker *client*.
* `run` Run a *container*.
* `-it`: Interactive (e.g. terminal) session.
* `ubuntu`: Name of the image (https://hub.docker.com/).
* `bash`: Program to execute inside the container.

    exit

## Exercises

1. Run the executable `python` within the `python` image.
        
        docker run -ti <> <>

To exit:

    >>> exit()

2. Tags. Run the executable `python` within the `python:3.7` image.

        docker run -ti <> <>

To exit:

    >>> exit()

## Sharing files from the host (e.g. your laptop) to the container

* Key point: By default, Docker containers are *completely isolated* from your
own system.
* You must *manually* specify which directories you want to share
into a container.

    docker run -ti -v $(pwd):/root/shared ubuntu bash

Inside the running container:

    # cd /root/shared
    # ls
    # exit

* `-v /host/path:/container/path` share the path at `/host/path` on the host,
to the path `/container/path` inside the container.

## Exercise: Running a `python` script

There is a python script at ``python/hello_world.py``. Modify it to read:

```
print("Hello world!")
```

Make sure you are in the root of the git repository.

```
# pwd
/Users/jack.hale/code/computational-workflows
```

Now run the script using a Docker container:

```
docker run -ti -v $(pwd):/root/shared <> "<> <>"
```

* <> Image name.
* <> Command to run in container.

## Exercise: `bash` then `python`

Instead, run ``bash`` inside a container and then run ``python
/root/shared/python/hello_world.py``.

## Making your own Docker image

Full documentation: https://docs.docker.com/engine/reference/builder/

Docker can build *new* images by writing a `Dockerfile`.

A `Dockerfile` contains a list of instructions (recipe) explaing how the image should be built.

A very simple `Dockerfile` can be found at `docker/example1/Dockerfile`.

# Exercise: Building your own image

Open `docker/example1/Dockerfile`. What does it do?

You can *build* a docker image following the recipe in the `Dockerfile` by running:

```
cd docker/example1/Dockerfile
docker build .
```

You should see some output like:

```
Successfully built e97420b64647
```

This unique *hash* can be used to run the image.

```
docker run -ti e97420b64647 ipython
```

Note: You need to substitute *your* unique hash.

## Exercise: Changing the default command

Try running:

```
docker run -ti e97420b64647
```

What happens?

We can change the default command to `ipython` using the `CMD` instruction at
the bottom of the `Dockerfile`.

Try adding:

```
CMD ["ipython"]
```

At the bottom of the `docker/example1/Dockerfile` and rebuilding. Then
`docker run` the new container. What do you see?

## Exercise: Tagging an image

*Tagging* (e.g. naming) an image gives us an easier way to refer it to than the
*hash* (e.g. e97420b64647).

```
cd docker/example1/Dockerfile
docker build --help
docker build -t ipython .
docker run -it <>
```

## Exercise: Sharing images with a colleague.

Scenarios:
* You want to share an image with your colleague.
* You want to release the software environment you used for the results in a
  paper as supplementary material.

Please read the documentation here:
https://docs.docker.com/engine/reference/commandline/save/ and construct 
a command that saves the image `ipython` to a file `ipython-image.tar.gz`.

Take a look at https://docs.docker.com/engine/reference/commandline/load/
and find how to load a `*.tar.gz` file back into Docker.

## Extended exercise.

A more convienient way to store Docker images is on a *Docker registry*.  In
this exercise we will *push* (like `git`) to the Docker Hub
(https://hub.docker.com) and your colleague will *pull* (like `git`) your image
to his/her computer.

1. Sign up for an account at https://hub.docker.com.
2. You need to login using:

    docker login

3. Modify the `Dockerfile` to build an image tagged with  `pytest` installed
   (via `pip`). `pytest` is a Python package for writing unit tests (more later).
```
FROM python:3.8

RUN pip install numpy pytest
```

## Ask me anything (about Docker).
