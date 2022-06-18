from evaluator import Result
from nodes import Node
from moduals.moduals import Module
osc = Module("vrc_osc")
import psutil
from os import getenv
from pathlib import Path
import json

class OscManager:
    def __init__(self):
        self.servers = {} # key : (addr, port)
        self.clients = {}

    def get_default_address(self): # todo untested
        vrc = filter(lambda p: p.name == "vrchat.exe", psutil.process_iter())

    def add_lissner(self, addr, port):
        pass

    def send(self, type, add, port, data):
        pass


class AvatarParm:
    def __init__(self, name,
                 input_address=None, output_address=None,
                 output_type=None, input_type=None):

        self.name = name
        self.input_address = input_address
        self.output_address = output_address
        self.output_type = output_type
        self.input_type = input_type

    @classmethod
    def from_json(cls, data):
        name = data["name"]
        kargs = {}
        if "input" in data:
            kargs["input_address"] = data["input"]["address"]
            kargs["input_type"] = data["input"]["type"]
        if "output" in data:
            kargs["output_address"] = data["output"]["address"]
            kargs["output_type"] = data["output"]["type"]

        return AvatarParm(name, **kargs)


class VrcAvatar:
    def __init__(self, _id, name, parameters):
        self.name = name
        self.parameters = parameters
        self.id = _id


    @classmethod
    def from_path(cls, path):
        with open(path, "r", encoding='utf-8-sig') as file:


            data = json.load(file)

        par = data["parameters"]
        return VrcAvatar(data["id"], data["name"], [AvatarParm.from_json(i) for i in par])


def get_avatars():
    output = []
    p = Path(getenv('APPDATA')).parents[0] / "LocalLow\VRChat\VRChat\OSC"
    if not p.exists():
        print("osc not init")
    for f in p.iterdir():
        first_user = f
        break
    else:
        return
    for f in (first_user / "Avatars").iterdir():
        print("avatatr", f)
        output.append(VrcAvatar.from_path(f))
    return output


@osc.register
class SendF(Node):
    op_name = "send"
    inputs = ("data", "address", "port")
    outputs = ()
    description = "send float to the given address "
    osc: OscManager
    def eval(self, data):
        try:
            self.osc.send()

        return Result()


@osc.register
class SendI(Node):
    op_name = "send"
    inputs = ("data", "address", "port")
    outputs = ()
    description = "send integer to the given address "

    def eval(self, data):
        out = data["a"] + data["b"]
        return Result()

@osc.register
class Receive(Node):
    op_name = "receive"
    inputs = ("address",)
    outputs = ("data",)
    description = "receive osc data from default osc connection "

    def eval(self, data):
        out = data["a"] + data["b"]
        return Result(data=out)

    def update(self):
        pass


if __name__ == "__main__":
    get_avatars()