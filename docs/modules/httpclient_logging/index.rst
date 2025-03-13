:py:mod:`httpclient_logging`
============================

.. py:module:: httpclient_logging

.. autoapi-nested-parse::

   httpclient_logging.__init__.



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   patch/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   httpclient_logging.configure



Attributes
~~~~~~~~~~

.. autoapisummary::

   httpclient_logging.__version__
   httpclient_logging.__copyright__


.. py:data:: __version__
   :value: '0.0.0'



.. py:data:: __copyright__
   :value: 'Copyright 2023 Libranet - MIT License.'



.. py:function:: configure()

   Configure the http.client.HTTPConnection-class

   Configure this class to use the debuglevel from an environment-variable DEBUGLEVEL_HTTPCONNECTION
   and to use a logger instead of a print-statements to output to standard output.


