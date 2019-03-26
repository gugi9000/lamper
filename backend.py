import json
import urllib.request
from credentials import home


def set_lamp_on(lamp, light=True):
    """
    Toggle the state of a lamp based in `lamp` and `light`
    Lamp with id `lamp` is turned on or off.
    `light` indicates whether or not to turn it on, if false it's turned off.
    Returns whether the command was send successfully.
    :param lamp: string
    :param light: boolean
    :return: boolean
    """
    bridge, _, api_key = home.get(home)
    state_url = f"http://{bridge}/api/{api_key}/lights/{lamp}/state/"
    on = b"""{"on": true}"""
    off = b"""{"on": false}"""
    if light:
        req = urllib.request.Request(url=state_url, data=on, method="PUT")
    else:
        req = urllib.request.Request(url=state_url, data=off, method="PUT")

    with urllib.request.urlopen(req) as f:
        pass
    if f.status == 200:
        return True
    else:
        return False


def find_lamps() -> list:
    """
    Contacts the Hue controller and query for lamps that a are reachable
    :return: a list with `id`, `name`, `state`
    """
    bridge, _, api_key = home.get(home)
    data = urllib.request.urlopen("http://" + bridge + "/api/" + api_key + "/lights/")
    data = data.read().decode("UTF-8")
    parsed_json = json.loads(data)

    lamps = []
    for lamp in parsed_json:
        lamps.append(lamp)

    res = []
    for lamp in lamps:
        if parsed_json[lamp].get("state").get("reachable"):
            name = parsed_json[lamp].get("name")
            state_on = parsed_json[lamp].get("state").get("on")
            state = "on" if state_on else "off"
            res.append([lamp, name, state])
            # print(f"Lamp {lamp} is called {name} and is {state}")

    res = sorted(res, key=lambda x: x[1])
    return res


def find_groups() -> list:
    """
    Contacts the Hue controller and query for groups
    :return: list
    """
    bridge, _, api_key = home.get(home)
    data = urllib.request.urlopen("http://" + bridge + "/api/" + api_key + "/groups/")
    data = data.read().decode("UTF-8")
    parsed_json = json.loads(data)

    groups = []
    for group in parsed_json:
        num = group
        name = parsed_json[group].get("name")
        # lamps = parsed_json[group].get("lights")
        all_on = parsed_json[group].get("state").get('all_on')
        any_on = parsed_json[group].get("state").get('any_on')
        if name[0] not in 'abcdefghijklmnopqrstuvwxyz':
            groups.append([num, name, all_on, any_on])

    res = sorted(groups, key=lambda x: x[1])

    return res


def get_lamps_by_group(num) -> list:
    """
    Contacts the Hue controller and query group for lamps
    :return: list
    """
    bridge, _, api_key = home.get(home)
    data = urllib.request.urlopen("http://" + bridge + "/api/" + api_key + "/groups/" + str(num))
    data = data.read().decode("UTF-8")
    parsed_json = json.loads(data)

    return parsed_json.get("lights")


if __name__ == "__main__":
    # set_lamp_on("14", False)
    # for lamp in find_lamps():
    #     # print(lamp)
    #     if lamp[1][0] == "G":
    #         set_lamp_on(lamp[0], True)
    print(get_lamps_by_group(1))
