import asyncio, aiocoap

@asyncio.coroutine
def coap_get_with_observe():
    protocol = yield from aiocoap.Context.create_client_context()

    request = aiocoap.Message(code = aiocoap.GET)
    request.set_request_uri('coap://[aaaa::212:4b00:aff:2781]:5683//net/parent/RSSI')
    # set observe bit from None to 0
    request.opt.observe = 0

    try:
        response = yield from protocol.request(request).response
    except Exception as e:
        print("request failed: %s" % str(e))
    else:
        print("request ok: %r" % response.payload)

event_loop = asyncio.new_event_loop()
asyncio.set_event_loop(event_loop)
event_loop.create_task(coap_get_with_observe())
asyncio.get_event_loop().run_forever()


