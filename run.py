# -*- coding: utf-8 -*-

import os
import subprocess
import configparser
from builtins import object


def popen(cmd):
    subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)


def collected_data():
    collection = {}
    config_full_path = "resources/config/config.ini"

    # Config
    config = configparser.ConfigParser()
    config.read(config_full_path)

    collection["scaling_first"] = config["scaling"]["first"]
    collection["scaling_last"] = config["scaling"]["last"]

    collection["path_temp"] = config["temp_setting"]["path"]
    collection["name_temp"] = config["temp_setting"]["name"]

    collection["path_ps1"] = config["ps1_setting"]["path"]
    collection["name_ps1"] = config["ps1_setting"]["name"]

    return collection


class ScalingManager(object):
    @classmethod
    def swap_param(cls, **kwargs):
        last = kwargs.get("last")
        first = kwargs.get("first")
        status = kwargs.get("status")
        return last if int(status) == int(first) else first

    @classmethod
    def read_temp(cls, temp):
        try:
            with open(temp, "r") as f:
                return int(f.read())
        except Exception as err:
            raise Exception(err)

    @classmethod
    def write_temp(cls, temp, status_scaling):
        try:
            with open(temp, "w") as f:
                f.write(str(status_scaling))
            return True
        except Exception:
            return 0


class Worker(object):
    """Responsible for the main work of the desktop scaling change process."""

    def __init__(self):
        self.scaling_manager = ScalingManager()
        self.cmd = 'powershell.exe -noexit -ExecutionPolicy Bypass -File "{}" {}'
        self.data = collected_data()
        self.temp = os.path.join(
            self.data.get("path_temp"),
            self.data.get("name_temp"))
        self.scaling_first = self.data.get("scaling_first")
        self.scaling_last = self.data.get("scaling_last")
        self.ps1 = os.path.join(
            self.data.get("path_ps1"),
            self.data.get("name_ps1"))

    def handler(self):
        status_scaling = self.scaling_manager.read_temp(self.temp)
        cmd = self.cmd.format(self.ps1, status_scaling)
        popen(cmd)
        if self.scaling_manager.write_temp(
            self.temp,
            self.scaling_manager.swap_param(
                first=self.scaling_first, last=self.scaling_last, status=status_scaling
            ),
        ):
            pass

        exit()


if __name__ in "__main__":
    worker = Worker()
    worker.handler()
