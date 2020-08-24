# This file has been formatted with black.
# https://github.com/psf/black

import json
import simplekml


ALTITUDE_MODE = "absolute"  # "absolute" altitude means from sea floor

with open("../../../nodeList.json", "r") as f:
    nodes = json.load(f)["nodeList"]

kml = simplekml.Kml(name="Toronto Community Network")

active = kml.newfolder(name="Active Nodes")
proposed = kml.newfolder(name="Proposed Nodes")
inactive = kml.newfolder(name="Inactive Nodes")

for node in nodes:
    # TODO: Add node data: image, addresses, model, etc

    if node["status"] == "active":
        active.newpoint(
            name=node["name"],
            altitudemode=ALTITUDE_MODE,
            coords=[(node["longitude"], node["latitude"], node["altitude"])],
        )
