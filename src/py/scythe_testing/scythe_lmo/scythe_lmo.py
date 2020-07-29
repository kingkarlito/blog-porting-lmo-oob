import json
import lmo_oob
import uuid
g_client = None

CATEGORY_WORKER = 4
SCYTHE_LMO_MODULE_ID = uuid.UUID('d0aa8880-c78b-11ea-b4ce-81907cc560cc')


def init(client, **kwargs):
    """

    :param client:
    :param kwargs:
    :return:
    """
    global g_client
    g_client = client
    return True


def run(message,  **kwargs):
    """

    :param bytes message:
    :param kwargs:
    :return bytes or None: None if post will happen asynchronously
    """
    
    # Load dict from message
    message_dict = json.loads(message.decode("utf-8"))
    # Get result of main's return
    result = lmo_oob.main(
        ports=message_dict["ports"],
        domain=message_dict["domain"]
    )
    # Turn result into string
    result = "\n".join(result)
    # Turn into bytes
    message = result.encode('utf-8')

    return message


def getinfo():
    """

    :return:
    """
    return { "type": CATEGORY_WORKER, "version" : {"major": 1, "minor": 0}, "id" : SCYTHE_LMO_MODULE_ID}


def deinit(**kwargs):
    """

    :param kwargs:
    :return:
    """
    return True
