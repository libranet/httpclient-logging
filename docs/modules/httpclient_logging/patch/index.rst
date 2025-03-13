httpclient_logging.patch
========================

.. py:module:: httpclient_logging.patch

.. autoapi-nested-parse::

   httpclient_logging.patch.



Attributes
----------

.. autoapisummary::

   httpclient_logging.patch.pre_patched_value
   httpclient_logging.patch.log


Classes
-------

.. autoapisummary::

   httpclient_logging.patch.Foo


Functions
---------

.. autoapisummary::

   httpclient_logging.patch.set_httpclient_debuglevel
   httpclient_logging.patch.patch_httpclient_print
   httpclient_logging.patch.unpatch_httpclient_print
   httpclient_logging.patch.configure
   httpclient_logging.patch.undo


Module Contents
---------------

.. py:data:: pre_patched_value

.. py:data:: log

.. py:function:: set_httpclient_debuglevel(debuglevel = '0')

   Set debug-level for http.client.

   If http-debuglevel > 0, debug messages in the  http.client.HTTPConnection-class will be printed to STDOUT.


.. py:function:: patch_httpclient_print()

   Patch the print-function used in http.client to use a call to log.debug() instead.


.. py:function:: unpatch_httpclient_print()

   Unpatch the print-function used in http.client.


.. py:function:: configure()

   Configure the http.client.HTTPConnection-class.

   Configure this class to use the debuglevel from an environment-variable DEBUGLEVEL_HTTPCONNECTION
   and to use a logger instead of a print-statements to output to standard output.


.. py:function:: undo()

   Undo the configured steps.


.. py:class:: Foo

   Test class for FOO.


   .. py:attribute:: _foo
      :value: 'foo'



