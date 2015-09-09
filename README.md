# conversationlist
Open source version of email address collection script. 

## Requirements & installation

1. A context.io 2.0 api account ( https://context.io/ )
2. An account auth'ed with the context.io 2.0 api
3. The contextio python library ( pip install contextio )
4. The python csv library ( pip install csv )

## Usage

1. Edit the build_email_list.py script configuration section to contain your credentials
2. Run python build_email_list.py (if all goes well it will report as it builds the list and the final result will be the creation of a emails.csv file)

### After completion

This script simply builds a csv file of any email address you've interacted with over the years (and tells you how many emails you've exchanged with the given address).

You will most likely want to scrub it for any known bad addresses or email lists that may slip through and de-dup it for those who use multiple email addresses when interacting with you.

**Note:** This script relies on the contextio api and can only collect email addresses from the emails that you have granted them access to and that they've then been able to index. It does not represent a complete history of your email activity (i.e. it won't include things you've deleted or most likely anything from a spam folder).
