pine API
========

A REST API for the ``pine`` benchmark service.

.. contents:: Table of Contents
   :local:
   :depth: 2

Versioning
----------

The ``pine`` REST API is versioned using the ``Accept`` header, enabling
stable URLs for clients.

The current version is ``v1``, and the applicable header value is
``application/vnd.pine.v1+json``.

.. http:example:: curl python-requests

   GET /version HTTP/1.1
   Host: pinebench.io/api
   Accept: application/vnd.pine.v1+json

Authentication
--------------

All resources require authentication via the (unfortunately named, but
`standard <https://tools.ietf.org/html/rfc7235#section-4.2>`_)
``Authorization`` header. This is where a request identifies itself
with its authentication token.

.. http:example:: curl python-requests

   GET /version HTTP/1.1
   Host: pinebench.io/api
   Accept: application/vnd.pine.v1+json
   Authorization: Token YWxhZGRpbjpvcGVuc2VzYW1l

Resources
---------

Version
+++++++

.. http:get:: /version

   Get information about this version of the API

   .. http:example:: curl python-requests
      :response: responses/version_get.json

      GET /version HTTP/1.1
      Host: pinebench.io/api
      Content-Type: application/json
      Accept: application/vnd.pine.v1+json
