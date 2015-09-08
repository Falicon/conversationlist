import contextio as c
import csv

############################################
### Script configuration (customize to your details)
############################################
CONSUMER_KEY = 'YOUR_CONTEXTIO_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONTEXTIO_CONSUMER_SECRET'
CONTEXTIO_AUTHED_EMAIL = 'THE EMAIL YOU WANT TO BUILD YOUR LIST FROM'
# ignore email addresses that contain any of the following words
ignores = [
  'buzz+','help','notify','info',
  'admin','no-reply','noreply',
  'service','notifications'
]
# the address fields you want to grab emails from
address_keys = ['to','cc','bcc','from']

############################################
### Script 
############################################
context_io = c.ContextIO(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

emails = {}
accounts = context_io.get_accounts(email=CONTEXTIO_AUTHED_EMAIL)
for account in accounts:
  has_more = True
  offset = 0
  page = 0
  while has_more:
    page += 1
    messages = account.get_messages(limit=100, offset=offset)
    added = 0
    for message in messages:
      for address_key in address_keys:
        try:
          if address_key == 'from':
            users = [message.addresses[address_key]]
          else:
            users = message.addresses[address_key]
          for user in users:
            email = user['email']
            skip = False
            for ignore in ignores:
              if email.find(ignore) > -1:
                skip = True
            if not skip:
              if email not in emails.keys():
                added += 1
                try:
                  emails[email] = {'name':user['name'],'count':1}
                except:
                  emails[email] = {'name':'','count':1}
              else:
                emails[email]['count'] += 1
        except:
          pass

    print "page %s added %s email address" % (page, added)
    offset += 100
    if len(messages) < 100:
      has_more = False

# sort the emails by count and write to a csv file
with open('emails.csv', 'wb') as csvfile:
  fieldnames = ['EMAIL', 'NAME', 'COUNT']
  emailwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
  emailwriter.writerow(fieldnames)
  for email in sorted(emails.iteritems(), key=lambda (x, y): y['count']):
    try:
      emailwriter.writerow([email[0], email[1]['name'], email[1]['count']])
    except:
      pass

