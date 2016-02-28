Minecraft Python Presentation Outline for SLCPython March 2016
==============================================================

Installation
------------

Ensure you've created a virtualenv and installed the requirements.

* :doc:`java_installation`
* :doc:`mc_buildtools`

Start er up!
------------

* Start your server: ``inv start_server``
* Start your client: ``java -jar Minecraft.jar``

In the client, connect to multiplayer, and connect to the server ip: ``127.0.0.1``

Test it
-------

Run ``python examples/hello_world.py``

Play Around
-----------

Run ``ipython`` and import the minecraft api:

.. code-block:: python

  from mcpi.minecraft import Minecraft; mc = Minecraft.create()

``ipython`` is awesome because you can start writing some code, and then hit
tab to see what functions are available in that module. You can also use ``help(<module>)`` to see more details about the module (Use ``q`` to quit).
