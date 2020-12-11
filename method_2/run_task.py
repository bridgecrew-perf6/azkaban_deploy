import argparse


def fun():
    pass


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--es-host", type=str, default="")
    PARSER.add_argument("--es-port", type=str, default="")

    ARGS = PARSER.parse_args()

    es_host = str(ARGS.es_host)
    es_port = int(ARGS.es_port)

    fun()
