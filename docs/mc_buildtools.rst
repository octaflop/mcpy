Minecraft Build Tools
=====================

Download and install build tools
--------------------------------

I wrote a python invoke task to handle this:

.. code-block:: bash

    inv get_build_tools

The build tools will install in the ``mcbuild`` directory. This directory has been excluded from the git repo.

The build tools will download a bunch of repos including ``CraftBukkit``.

