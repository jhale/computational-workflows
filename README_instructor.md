# Instructor instructions

## Technical setup

1. Switch to ``/bin/bash`` shell.
2. Run ``swc-shell-split-window``.
3. Go to: https://pad.carpentries.org/comp-workflows

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


