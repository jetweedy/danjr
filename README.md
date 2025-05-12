# DANJR: a Django, Ansible, NoSQL, Jenkins and React learning project.

There's not much to this app other than the deployment learning under the hood. 
I wanted to put together something I could work on to give myself a better introduction to some tools that I don't use much (or at all) in my everyday work. 
There are three folders in this repository:
 - a backend folder with the Python/Django piece acting as an API for the frontend (and including some admin pieces)
 - a frontend folder with the ReactJS front end
 - a deployment folder with some pieces related to deploying this thing to AWS EC2

I can't promise that the instructions are very clear in each folder yet. 
The backend readme contains some info on setting up a Mongo Atlas DB to connect to and getting the Django app up and running locally.
The deploy readme goes into getting the WSL environment set up (if in Windows) so you can use Ansible and Jenkins more easily, and then details about using Ansible to deploy to AWS EC2.
The frontend readme is just the stock React-installed readme, and you can pretty much ignore it for testing purposes.

**NOTE:** 
There may be a few path or environment settings in this specific to *my* setup, so you'd need to swap some of those out for your own as you set things up.
I can't say they're necessarily well-documented, but if you overlook any, errors should point you in the right direction.

