File for testing vale without typos
###################################


Tests
=====

Find typos
----------

Vale shall give me a hint that, there are typos in my text.


Find typos in notes
-------------------

.. note::

   Vale shall give me a hint that, there are typos in my note.


Find typos in notes inside notes
--------------------------------

.. note::

   Vale shall give me a hint that, there are typos in my note.

   .. note::

      Vale shall give me a hint that, there are typos in my second note.


Find typos in literal blocks
----------------------------

..

   Vale shall give me a hint that, there are typos in my literal blocks.


Find typos in literal quotes inside literal quotes
--------------------------------------------------

..

   Vale shall give me a hint that, there are typos in my literal quote.

   ..

      Vale shall give me a hint that, there are typos in my literal quote inside a literal quote.


Find typos in block quotes
--------------------------

   Vale shall give me a hint that, there are typos in my block quote.


Find typos in block quotes inside block quotes
----------------------------------------------

   Vale shall give me a hint that, there are typos in my block quote.

      Vale shall give me a hint that, there are typos in my block quote inside a block quote.

End of Tests
============
