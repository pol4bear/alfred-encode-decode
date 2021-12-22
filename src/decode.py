#!/usr/bin/env python

import sys
from workflow import Workflow3

def add_item(wf, title, value):
  it = wf. add_item(title,
                   valid    = True,
                   subtitle = value,
                   arg      = value)

def main(wf):
  from urllib import unquote, unquote_plus
  import HTMLParser
  from base64 import b64decode, urlsafe_b64decode
  from binascii import unhexlify

  item_count = 0
  text = wf.args[0].encode('utf-8')

  decoded = unquote(text)
  if decoded != text:
    item_count += 1
    add_item(wf, u'URLDecode', decoded)
  decoded = unquote_plus(text)
  if decoded != text:
    item_count += 1
    add_item(wf, u'URLDecode(+)', decoded)
  decoded = HTMLParser.HTMLParser().unescape(text)
  if decoded != text:
    item_count += 1
    add_item(wf, u'HTMLDecode', decoded)
  try:
    decoded = b64decode(text).decode('utf-8')
    item_count += 1
    add_item(wf, u'Base64', decoded)
  except:
    pass
  try:
      decoded = urlsafe_b64decode(text).decode('utf-8')
      item_count += 1
      add_item(wf, u'Base64(URLSafe)', decoded)
  except:
    pass
  try:
    decoded = text.replace(' ', '')
    decoded = decoded.replace('0x', '')
    decoded = bytearray.fromhex(decoded).decode('utf-8')
    item_count += 1
    add_item(wf, u'Hex', decoded)
  except:
    try:
      decoded = decoded.decode('unicode-escape')
      if decoded != text:
        add_item(wf, u'Hex', decoded)
        item_count += 1
    except:
      pass

  if item_count == 0: wf.add_item(u'No decode available for "{}".'.format(text))
  wf.send_feedback()

if __name__ == '__main__':
  wf = Workflow3()
  sys.exit(wf.run(main))
