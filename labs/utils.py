# -*- coding: utf-8 -*-


import docker

from courses.constants import (
    PYTHON, RUBY, PHP, NODEJS
)


BASE_URL_TCP = "tcp://127.0.0.1:2375"
INIT_COMMAND = "node /usr/bin/server.js"

IMAGE = {
    PYTHON: "codefunland/python",
    RUBY:   "codefunland/ruby",
    PHP:    "codefunland/php",
    NODEJS: "codefunland/nodejs"
}

CLI = docker.Client(base_url=BASE_URL_TCP)

MOUNTPOINT = r"/mysite"
HOST_DIR = ''

HOST_ADDR = "127.0.0.1"
CONTAINER_PORTS = 9999

LOGIN_USER = "code"
WORKING_DIR = "/home/code"


def docker_ps():
    return CLI.containers(all=True)


def docker_init_container(image):
    """
    Just only test docker server.
    """
    c = CLI.create_container(
        image=IMAGE[image],
        command="/bin/bash",
        stdin_open=True,
        tty=True,
        mem_limit="128m",
        working_dir="/home",
        )
    CLI.start(container=c.get('Id'))
    return c


def docker_init_container_ports(image, host_addr=HOST_ADDR):
    """
    Init a docker container and allots a port to it.
    """
    c = CLI.create_container(
        image=IMAGE[image],
        command=INIT_COMMAND,
        stdin_open=True,
        tty=True,
        mem_limit="128m",
        user=LOGIN_USER,
        working_dir=WORKING_DIR,
        ports=[CONTAINER_PORTS]
    )
    CLI.start(
        container=c.get("Id"),
        port_bindings={
            CONTAINER_PORTS: (HOST_ADDR, )
        },
        restart_policy={
            "MaximumRetryCount": 0,
            "Name": "always"
        }
    )
    return c


def docker_stats(container_id):
    return CLI.stats(container_id)


def docker_container_inspect(container_id):
    return CLI.inspect_container(container_id)


def docker_port(container_id):
    container_port_mapper = CLI.port(container_id, CONTAINER_PORTS)[0]
    host_ip = container_port_mapper.get("HostIp")
    host_port = container_port_mapper.get("HostPort")
    return "%s:%s" % (host_ip, host_port)


def docker_rm_container(container_id):
    status = CLI.remove_container(
        container=container_id,
        force=True
    )
    return status


if __name__ == "__main__":
    # print docker_init_container()
    print docker_ps()
