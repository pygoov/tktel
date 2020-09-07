# tktel
Tkinter Telegram Client

## Requirements

- python 3.7>=
- tkinter lib
- telethon lib
- brains


## Command line

example used:
```bash
python .\main.py -I <YOUR API ID> -H <YOUR API HASH> -S <YOUR SESSION> -U <TARGET USER>
```
help:
```
usage: main.py [-h] --api_id [API_ID] --api_hash [API_HASH] --session [SESSION] --user_id [USER_ID]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  --api_id [API_ID], -I [API_ID]
                        Api id for telegram connection
  --api_hash [API_HASH], -H [API_HASH]
                        Api hash for telegram connection
  --session [SESSION], -S [SESSION]
                        Session for telegram connection
  --user_id [USER_ID], -U [USER_ID]
                        User id for messaging
```