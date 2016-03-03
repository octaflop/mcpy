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


PYTHON!
-------

Modules or: Why write the same code twice?
++++++++++++++++++++++++++++++++++++++++++

Your fellow pythonistas have probably already solved the problem your trying to solve. Or at least something similar.
Rather than copying all of their code, or keeping all code in one file, you can import it with the ``from`` and ``import`` keywords.

Once you've imported, you can write ``help(<imported module>)`` to see the many functions of that code.

Our main import is ``mcpi`` but we don't want to import the whole library and all of its functions, so we use ``from`` to help specify exactly what we're importing. If we want to import as a different word, we can use the ``as`` keyword:

.. code-block:: python

    from mcpi.minecraft import Minecraft
    import mcpi.blocks as blocks

Examples
********

``hello_world.py``


Loops
+++++

Loops are more than just a way to repeat something, they're also a way to dig through a list of things.

Examples
********

In our tower examples, we use loops for both height and for digging through a list of color blocks.


Functions
+++++++++


Classes
+++++++
