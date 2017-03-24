import asyncio, aiocoap

@asyncio.coroutine
def coap_get_with_observe():
    protocol = yield from aiocoap.Context.create_client_context()

    request = aiocoap.Message(code = aiocoap.PUT)
    request.set_request_uri('coap://[aaaa::212:4b00:aff:2781]:5683/lt/r')
    # set observe bit from None to 0
    request.opt.observe = 0

    try:
        protocol_request = protocol.request(request)
        protocol_request.observation.register_callback(observation_callback)
        response = yield from protocol_request.response
    except Exception as e:
        print("request failed: %s" % str(e))
    else:
        print("request ok: %r" % response.payload)
def observation_callback(response):
    print("callback: %r" % response.payload)

event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)
event_loop.create_task(coap_get_with_observe())
asyncio.get_event_loop().run_forever()

