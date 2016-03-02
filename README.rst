Minecraft Python
================

This guide and talk are structured around a linux ubuntu installation. Installation and setup are a lot easier on a raspberry pi, but the ubuntu installation is a lot more powerful.

Unfortunately, there's still lot of outdated documentation on the web, so I'm hoping to compile the most useful info into the ``docs`` folder.

Meetup Talk Link: http://www.meetup.com/SLCPython/events/227895854/

Basic Installation
------------------

.. code-block:: bash

  mkvirtualenv -p /usr/bin/python3 mcpy && workon mcpy && pip install -r requirements.txt && inv docs
