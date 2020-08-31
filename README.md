# node-list


[![Build Status](https://travis-ci.org/tomeshnet/node-list.svg?branch=master)](https://travis-ci.org/tomeshnet/node-list)

This repository contains the list of nodes that are part of the Toronto Community Network.
Each node is recorded with geolocation and technical information as according to [schema.json][schema-json].
The list of nodes is organized as a JSON file at [tomeshnet-node-list.json](tomeshnet-node-list.json).

## Other Formats

[Travis CI](.travis.yml) converts the [tomeshnet-node-list.json](tomeshnet-node-list.json)) file into several formats.

Currently:
- Keyhole Markup Language ([KML](https://developers.google.com/kml/))
    - Good for viewing the nodes in mapping programs like Google Earth/Maps
- [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON)
    - Good for applications that are already expecting GeoJSON, like [Leaflet](https://leafletjs.com/)

These files are always available on the [Releases page](https://github.com/tomeshnet/node-list/releases).

### Latest Files

If you want to link to the latest version of these files, use these special URLs.

- https://raw.githubusercontent.com/tomeshnet/node-list/master/tomeshnet-node-list.json
- https://raw.githubusercontent.com/tomeshnet/node-list/assets/tomeshnet-node-list-kml.kml
- https://raw.githubusercontent.com/tomeshnet/node-list/assets/tomeshnet-node-list-geojson.json

## Images

The [images](images) folder contains images referenced in [tomeshnet-node-list.json](tomeshnet-node-list.json).
The images are named according to their associated node, with the following naming convention.

| Name | Description | Example |
|:-----|:------------|:--------|
| `[nodename].[ext]` | The view from that node | `sn1a1.jpg` |
| `[nodename]-[type].[ext]` | With picture type | `sn1a1-hw.jpg` for hardware |
| `[nodename]-[type]-[index].[ext]` | With multiple pictures of the same type | `sn1a1-hw-2.jpg` for the second  hardware picture |

## Validation

In this repository, [Travis CI](.travis.yml) is configured to validate [tomeshnet-node-list.json](tomeshnet-node-list.json)) against [schema.json][schema-json] using [Ruby JSON Schema Validator](https://github.com/ruby-json-schema/json-schema).
The validation tool currently supports up to [JSON Schema Draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04), so schema files must conform to the Draft 4 standard.

You can use [JSON Schema Lint](https://jsonschemalint.com) to validate manually.

[schema-json]: schema/v0.7/schema.json
