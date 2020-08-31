# This file is formatted with black.
# https://github.com/psf/black

import os
import json
import subprocess
import sys
import simplekml

ALT_MODE = simplekml.AltitudeMode.absolute  # Absolute altitude means from sea floor

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


def get_desc(node):
    """Generate HTML description for a node."""

    # Required keys
    desc = f"<h1>{node['name']}</h1>"
    desc += f"<h2>{node['status']}</h2>"
    desc += f"Type: {node['type']}<br>"
    desc += f"Altitude: {node['altitude']}<br>"
    desc += f"Date Added: {node['dateAdded']}<br>"
    desc += f"Group: {node['group']}<br>"

    # Optional keys
    desc += f"Model: {node.get('model')}<br>"
    desc += f"IPv4: {node.get('ipv4')}<br>"
    desc += f"IPv6: {node.get('ipv6')}<br>"
    desc += f"Mode: {node.get('mode')}<br>"
    if node["type"] != "router":
        desc += f"Connected Router: {node.get('router')}<br>"

    # Antenna specific keys
    if node["type"] == "antenna":
        desc += f"SSID: {node.get('ssid')}<br>"
        desc += "<br>"
        desc += f"Antenna Type: {node.get('antennaType')}<br>"
        desc += f"Antenna Cone: {node.get('antennaCone')}<br>"
        desc += f"Antenna Direction: {node.get('antennaDirection')}<br>"
        desc += f"Antenna Distance: {node.get('antennaDistance')}<br>"
        desc += f"Antenna Protocol: {node.get('antennaProtocol')}<br>"

    desc += "<br>"

    # Images
    if node.get("images") is not None:
        for image in node["images"]:
            url = (
                "https://raw.githubusercontent.com/tomeshnet/node-list/"
                + COMMIT
                + "/images/"
                + image
            )
            desc += f'<a href={url}><img alt={image} src={url} width="300"></a><br>'

    return "<![CDATA[" + desc + "]]>"


with open("../../../tomeshnet-node-list.json", "r") as f:
    nodes = json.load(f)["nodeList"]

kml = simplekml.Kml(name="Toronto Community Network")

active = kml.newfolder(name="Active Nodes", open=0, visibility=1)
proposed = kml.newfolder(name="Proposed Nodes", open=0, visibility=1)
inactive = kml.newfolder(name="Inactive Nodes", open=0, visibility=0)

for node in nodes:
    if node["status"] == "active":
        folder = active
        vis = 1  # Active nodes always visible
        # Yellow
        icon_url = "http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png"
    elif node["status"] == "proposed":
        folder = proposed
        vis = 1
        # Light Blue
        icon_url = "http://maps.google.com/mapfiles/kml/pushpin/ltblu-pushpin.png"
    else:
        # All other nodes are considered inactive
        folder = inactive
        vis = 0
        # Red
        icon_url = "http://maps.google.com/mapfiles/kml/pushpin/red-pushpin.png"

    pnt = folder.newpoint(
        name=node["name"],
        altitudemode=ALT_MODE,
        coords=[(node["longitude"], node["latitude"], node["altitude"])],
        visibility=vis,
        description=get_desc(node),
        snippet=simplekml.Snippet(),  # Empty snippet
    )
    pnt.style.iconstyle.icon.href = icon_url

kml.save("../../build/tomeshnet-node-list-kml.kml")
