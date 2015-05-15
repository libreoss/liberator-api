liberator
=========

E-zine managament platform

Mission:
-------
Kickstart LiBRE! again!
Checkout this PDF: https://atlantic777.lugons.org/liberator_mail.pdf


Contact:
--------
- Atlantic777 - atlantic777 [at] lugons.org
- fantastic001 - stefan [at] lugons.org
- official LiBRE! mail - libre [at] lugons.org

- IRC - #floss-magazin or #lugons on freenode

Requirements:
------------

(Tested and working, may work with other versions)

- fantastic001/pydokuwiki
- Django 1.7
- Ansible 1.8
- Vagrant 1.7

Dev guidlines:
-------------
- Please, use python 3 and Django 1.7.
- Make sure to use space instead of tab.
- Upon `vagrant up` and `vagrant ssh` run `runserver.sh` and go to [Vagrant box](http://192.168.66.6:8000/api/v1/)
- User/Pass is admin@example.com/Sekrit

FAQ:
----
- My user:pass for LiBRE! dokuwiki doesn't work in liberator! (dokuwiki sync will be on stand by for some time)
  - Make sure that you create new user for accessing dokuwiki API and contact admins to give you permissions.
- It's not working!
  - Make sure you have up to date code (do `git pull`) and try to setup vagrant machine again with `vagrant destroy -f; vagrant up`
- Ok, it's running but I don't see anything...
  - Try opening http://192.168.66.6:8000/admin and playing around with http://192.168.66.6:8000/api/v1/
- I can't login.
  - Try creating a super user by yourself. Make sure you're on vagrant box (`vagrant ssh`) and then do `/vagrant/manage.py createsuperuser`
- How many people is contributing to this project?
  - For now 5+ more experienced ones and 15+ new ones which are waiting for things to settle down before they start working.
- This project has only API. Where can I "click on something"?
  - Yup, liberator provides only REST API for other clients. We are working on web client (angular, inuit...) Checkout other libreoss repositories. Maybe once there will be native Android, GTK, Qt or some other client, too.
- There were other Django apps in this project. Code is still here, but you are not using them.
  - Yup, we are moving to a web app which is based on Angular and it's separate project. Old code is still here, but it's disabled and probably will never be enabled again. It will be removed soon.
- My machine has no support for running 64bit guest systems, can i use 32bit version as vagrant machine?
  - Yes, just create file vagrant-conf.local and put `VAGRANT_ARCH = "x32"` in there. Then you need to execute `vagrant up`. If you're using 64bit machine, you have to remove old machine and run `vagrant destroy -f` and then `vagrant up` again.
