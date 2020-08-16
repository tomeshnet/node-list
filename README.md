# node-list

[![Build Status](https://travis-ci.org/tomeshnet/node-list.svg?branch=master)](https://travis-ci.org/tomeshnet/node-list)

This repository contains the list of nodes that are part of the Toronto Community Network.
Each node is recorded with geolocation and technical information as according to [schema.json][schema-json].
The list of nodes is organized as a JSON file at [nodeList.json](nodeList.json).

## Images

The [images](images) folder contains images referenced in [nodeList.json](nodeList.json).
The images are named according to their associated node, with the following naming convention.

| Name | Description | Example |
|:-----|:------------|:--------|
| `[nodename].[ext]` | The view from that node | `sn1a1.jpg` |
| `[nodename]-[type].[ext]` | With picture type | `sn1a1-hw.jpg` for hardware |
| `[nodename]-[type]-[index].[ext]` | With multiple pictures of the same type | `sn1a1-hw-2.jpg` for the second  hardware picture |

## Validation

In this repository, [Travis CI](.travis.yml) is configured to validate [nodeList.json](nodeList.json) against [schema.json][schema-json] using [Ruby JSON Schema Validator](https://github.com/ruby-json-schema/json-schema).
The validation tool currently supports up to [JSON Schema Draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04), so schema files must conform to the Draft 4 standard.

You can use [JSON Schema Lint](https://jsonschemalint.com) to validate manually.

[schema-json]: schema/v0.7/schema.json