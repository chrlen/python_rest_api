from pytest import fixture
from mongoengine import connect
from testcontainers.mongodb import MongoDbContainer


def extract_from_mongo_container(mongodb):
    split = mongodb.get_connection_url().split(":")

    host = mongodb.get_container_host_ip()
    port = int(split[-1])
    user = split[1].split("//")[1]
    password = split[2].split("@")[0]

    return host, port, user, password


@fixture(scope="session", autouse=True)
def mongodb():
    mongodb = MongoDbContainer("mongo:7.0.0")
    mongodb.start()

    host, port, username, password = extract_from_mongo_container(mongodb)

    print(f"Using mongo: {host}:{port}")

    connect(
        db='admin',
        host=host,
        port=port,
        username=username,
        password=password
    )

    yield mongodb
    mongodb.stop()


