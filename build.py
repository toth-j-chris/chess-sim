import os
import sys


def docker_build():
    os.system('docker build -t chess-sim .')


def docker_run():
    os.system('docker run --name chess-sim -it chess-sim bash')


def run_main():
    os.system('python main.py')


def docker_stop():
    os.system('docker container stop chess-sim')


def docker_rm():
    os.system('docker container rm chess-sim')


def main():
    docker_build()
    docker_run()
    docker_stop()
    docker_rm()


if __name__=='__main__':
    main()
