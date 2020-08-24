# node-list

[![Build Status](https://travis-ci.org/tomeshnet/node-list.svg?branch=master)](https://travis-ci.org/tomeshnet/node-list)

This repository contains the list of nodes that are part of the Toronto Community Network.
Each node is recorded with geolocation and technical information as according to [schema.json][schema-json].
The list of nodes is organized as a JSON file at [nodeList.json](nodeList.json).

## Other Formats

[Travis CI](.travis.yml) converts the [nodeList.json](nodeList.json) file into several formats.

Currently:
- Keyhole Markup Language ([KML](https://developers.google.com/kml/))
    - Good for viewing the nodes in mapping programs like Google Earth/Maps
- [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON)
    - Good for applications that are already expecting GeoJSON, like [Leaflet](https://leafletjs.com/)

These files are always available on the [Releases page](https://github.com/tomeshnet/node-list/releases).

You can always get the most recent version using the special "latest" URL. For example, if you want to download the `kml.kml` file, the URL is `https://github.com/tomeshnet/node-list/releases/latest/download/kml.kml`.

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
