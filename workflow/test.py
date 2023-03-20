from aqueduct import Client, op
import os

client = Client(aqueduct_address=os.environ['AQUEDUCT_SERVER_ADDRESS'], api_key=os.environ['AQUEDUCT_API_KEY'])

@op
def test():
    return "hello"

result = test()


client.publish_flow(name="test", artifacts=[result])