# node-list

[![Build Status](https://travis-ci.org/tomeshnet/node-list.svg?branch=master)](https://travis-ci.org/tomeshnet/node-list)

This repository contains the list of nodes and that are part of the Toronto Community Network.
Each node is recorded with geolocation and technical information as according to [schema/v0.6/schema.json](schema/v0.6/schema.json).
The list is organized as a JSON file at [nodeList.json](nodeList.json).

## Validation

In this repository, [Travis CI](.travis.yml) is configured to validate [nodeList.json](nodeList.json) against [schema/v0.6/schema.json](schema/v0.6/schema.json) using [Ruby JSON Schema Validator](https://github.com/ruby-json-schema/json-schema).
The validation tool currently supports up to [JSON Schema Draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04), so schema files must conform to the Draft 4 standard.

You can use [JSON Schema Lint](https://jsonschemalint.com) to validate manually.