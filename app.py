import asyncio
from quart import Quart
from futu import SysConfig, OpenQuoteContext, ContextStatus
import os

app = Quart(__name__)

host = os.environ.get('FUTU_OPEND_HOST')
port = int(os.environ.get('FUTU_OPEND_PORT'))
rsa_file = os.environ.get('FUTU_OPEND_RSA_FILE')

if rsa_file and len(rsa_file) > 0:
    SysConfig.enable_proto_encrypt(True)
    SysConfig.set_init_rsa_file(rsa_file)

quote_ctx  = OpenQuoteContext(host=host, port=port, is_async_connect=True)
quote_ctx.start()

async def ping():
    status_ok = False
    while True:
        if quote_ctx.status == ContextStatus.READY:
            status_ok = True
            break
        await asyncio.sleep(0.1)
    if not status_ok:
        return 'Fail', 500
    return 'OK'

@app.route('/healthz')
async def healthz():
    try:
        async with asyncio.timeout(8):
            return await ping()
    except asyncio.TimeoutError:
        return 'Timeout', 500


if __name__ == "__main__":
    app.run()
