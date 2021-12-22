#!/usr/bin/env python3

import sys
from workflow import Workflow3

def add_item(wf, title, value):
  it = wf. add_item(title,
                   valid    = True,
                   subtitle = value,
                   arg      = value)

def main(wf):
  from urllib import quote, quote_plus
  from html import escape
  from base64 import b64encode, urlsafe_b64encode

  text = wf.args[0].encode('utf-8')

  encoded = quote(text)
  if encoded != text: add_item(wf, u'URLEncode', encoded)
  encoded = quote_plus(text)
  if encoded != text: add_item(wf, u'URLEncode(+)', encoded)
  encoded = escape(text)
  if encoded != text: add_item(wf, u'HTMLEncode', encoded)
  add_item(wf, u'Base64', b64encode(text))
  add_item(wf, u'Base64(URLSafe)', urlsafe_b64encode(text))
  encoded = text.encode('hex')
  add_item(wf, u'Hex', encoded)
  add_item(wf, u'Escaped Hex', '\\x' + '\\x'.join(encoded[i:i+2] for i in range(0, len(encoded), 2)))
  wf.send_feedback()

if __name__ == '__main__':
  wf = Workflow3()
  sys.exit(wf.run(main))
