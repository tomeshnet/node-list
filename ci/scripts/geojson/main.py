# This file is formatted with black.
# https://github.com/psf/black

import os
import json
import subprocess
import sys

# Current commit

if os.environ.get("TRAVIS"):
    COMMIT = os.environ["TRAVIS_COMMIT"]
else:
    # For local dev
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, cwd="../../../", text=True
    )
    if proc.returncode != 0:
        print("Git command failed")
        sys.exit(1)
    COMMIT = proc.stdout.strip()

with open("../../../nodeList.json", "r") as f:
    nodes = json.load(f)["nodeList"]

# GeoJSON is stored in a FeatureCollection.
# See Wikipedia for an example: https://eng.wikipedia.org/wiki/GeoJSON#Example

gj = {"type": "FeatureCollection", "features": []}

for node in nodes:
    feat = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [node["longitude"], node["latitude"], node["altitude"]],
        },
        "properties": {},
    }

    # Add all other parts of the JSON as properties
    for k, v in node.items():
        if k in ["longitude", "latitude", "altitude"]:
            continue
        feat["properties"][k] = v

    gj["features"].append(feat)

with open("../../build/geo.json", "w") as f:
    json.dump(gj, f, indent=2)
