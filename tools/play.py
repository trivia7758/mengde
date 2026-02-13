#!/usr/bin/env python

import os
import time
import platform
import argparse
from cmd_helpers import *

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("buildtype", default="Debug", help="build type",
                        choices=["Debug", "Release"], nargs="?")
    parser.add_argument("-r", "--rpi", help="Set resolution for Raspberry Pi",
                        action="store_true")
    return parser.parse_args()

def main():
    options = parse_args()

    # Fetch system info
    system, node, release, version, machine, processor = platform.uname()

    build_dir = os.path.join("build", "%s.%s.%s" % (system, machine, options.buildtype))
    os.chdir(build_dir)

    install_folder = "install"
    os.chdir(install_folder)

    if system == "Windows":
        vcpkg_root = os.environ.get("VCPKG_ROOT", r"C:\vcpkg")
        dll_paths = [
            os.path.join(vcpkg_root, "installed", "x64-windows", "debug", "bin"),
            os.path.join(vcpkg_root, "installed", "x64-windows", "bin"),
        ]
        existing = [p for p in dll_paths if os.path.isdir(p)]
        if existing:
            os.environ["PATH"] = os.pathsep.join(existing + [os.environ.get("PATH", "")])

    if (options.rpi):
        check_run_cmd('tvservice', ['-e', 'DMT 16']) # change to 1024x768
        time.sleep(1) # need a little bit of time for graphics to be stable

    game_name = "game.exe" if system == "Windows" else "game"
    game_path = os.path.join(".", game_name)
    check_run_cmd(game_path)

    if (options.rpi):
        check_run_cmd("tvservice", ["-p"]) # change to prefered(default) mode
        time.sleep(1)
        check_run_cmd("fbset", ["-depth", "24"]) # hack to make screen visible
        check_run_cmd("fbset", ["-depth", "32"])

if __name__ == "__main__":
    main()
