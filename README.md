Django Tastypie Client
======================

This is a client library for fluidly working with a Django [Tastypie](https://github.com/toastdriven/django-tastypie) REST API.
It is _very_ preliminary.

This library is somewhat analogous to Backbone.js, but with important differences:

 * Python :-)
 * The client is generated from the tastypie schema.
 * The API is instantiated with a base URL and relative links are automatically followed.

In other words, it is a "web crawler" but instead of HTML and hrefs, it handles the much-simpler case 
of JSON with pointers implemented as URLs, and undestands the particular schema flavor included in 
Tastypie.

Contributors
------------
 * [Kenneth Knowles](https://github.com/kennknowles) ([@KennKnowles](https://twitter.com/KennKnowles))

Copyright & License
-------------------
Copyright 2012 Kenneth Knowles

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
