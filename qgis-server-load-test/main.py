import json
import uuid

import pytest
import requests


# prep input
bboxes = []
with open("grid_fine_grained.geojsonl.json", "r") as f:
    for i in f.readlines():
        d = json.loads(i)["properties"]

        bboxes.append(d)

# bboxes = bboxes[:4]


@pytest.mark.parametrize("bbox", bboxes)
def test(bbox):
    left = bbox["left"]
    bottom = bbox["bottom"]
    right = bbox["right"]
    top = bbox["top"]

    # left = 100.68176057800001
    # top = 13.849433233000001
    # right = 100.731760578
    # bottom = 13.799433233

    wms_url = (
        # "https://foo.bar.com/project/xxxxxx/?"
        +"&service=WMS&request=GetMap&version=1.1.1&layers=Carto,urbanplan&styles=&format=image/png&transparent=true&tileSize=512&dpi=96&width=614&height=767&srs=EPSG:4326&"
        + f"bbox={left},{bottom},{right},{top}"
    )

    session = requests.Session()
    session.auth = ("username", "password")

    # auth = session.post("https://mapserver.karnwong.me")
    r = session.get(wms_url)

    with open(f"images/{uuid.uuid4()}.png", "wb") as f:
        f.write(r.content)

    assert r.status_code == 200


if __name__ == "__main__":
    test(bboxes[3])
