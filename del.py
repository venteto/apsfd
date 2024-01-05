#!/usr/bin/env python3

"""
feed URL, per SkyFeed UI:
https://bsky.app/profile/did:plc:wecucphzbhaznb64qmvto5oj/feed/aaaace25sbydy
"""

from atproto import Client, models
import conf

HANDLE = 'venteto.bsky.social'
RECORD_NAME = 'aaaace25sbydy'

def main():
    client = Client()
    client.login(HANDLE, conf.PASSWORD)

    # feed_did = f'did:web:{HOSTNAME}'

    response = client.com.atproto.repo.delete_record(
        models.ComAtprotoRepoDeleteRecord.Data(
            repo=client.me.did,
            collection=models.ids.AppBskyFeedGenerator,
            rkey=RECORD_NAME,
        )
    )
    print('Success:', response)


if __name__ == '__main__':
    main()
