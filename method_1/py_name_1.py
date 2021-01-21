import argparse

from pkgname.configuration import Config

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--operation", type=str, choices=["new", "finish", "get"], default="get")
    PARSER.add_argument("--mysql-host", type=str, default="")
    PARSER.add_argument("--mysql-port", type=int, default=3307)
    PARSER.add_argument("--mysql-username", type=str, default="")
    PARSER.add_argument("--mysql-password", type=str, default="")
    PARSER.add_argument("--mysql-database", type=str, default="")

    ARGS = PARSER.parse_args()
    OPT = ARGS.operation

    Config.MYSQL_HOST = str(ARGS.mysql_host)
    Config.MYSQL_PORT = int(ARGS.mysql_port)
    Config.MYSQL_USERNAME = str(ARGS.mysql_username)
