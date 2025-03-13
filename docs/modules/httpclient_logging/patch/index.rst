:py:mod:`httpclient_logging.patch`
==================================

.. py:module:: httpclient_logging.patch

.. autoapi-nested-parse::

   httpclient_logging.patch.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   httpclient_logging.patch.set_httpclient_debuglevel
   httpclient_logging.patch.patch_httpclient_print
   httpclient_logging.patch.unpatch_httpclient_print
   httpclient_logging.patch.configure
   httpclient_logging.patch.cancel



Attributes
~~~~~~~~~~

.. autoapisummary::

   httpclient_logging.patch.pre_patched_value
   httpclient_logging.patch.log


.. py:data:: pre_patched_value



.. py:data:: log



.. py:function:: set_httpclient_debuglevel(debug_level=None)

   if http-debuglevel > 0, debug messages in the
   http.client.HTTPConnection-class will be printed to STDOUT.


.. py:function:: patch_httpclient_print()

   Patch the print-function used in http.client to use a log-call.


.. py:function:: unpatch_httpclient_print()

   Unpatch the print-function used in http.client to use a log-call.


.. py:function:: configure()

   Configure the http.client.HTTPConnection-class

   Configure this class to use the debuglevel from an environment-variable DEBUGLEVEL_HTTPCONNECTION
   and to use a logger instead of a print-statements to output to standard output.


.. py:function:: cancel()

   Dummy function to cancel (override) the entrypoint-registration.


