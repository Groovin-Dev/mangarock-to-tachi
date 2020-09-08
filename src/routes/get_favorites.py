import requests
import json


def get_favorites(id_token: str) -> dict:
    print(id_token)

    # WIP

    # response = requests.post('https://graphql.mangarock.io/graphql', headers={
    #                          'Content-Type': 'application/json', 'Authorization': id_token},
    #                          data=json.dumps({
    #                              "operationName": "listUserReadingHistoryByUpdatedTimeRevised",
    #                              "variables": {
    #                                  "limit": 100000,
    #                                  "updatedAt": "1970-01-01T00:00:00.000Z",
    #                                  "nextToken": ""
    #                              },
    #                              "query": "query listUserReadingHistoryByUpdatedTimeRevised($updatedAt: AWSDateTime, $limit: Int, $nextToken: String) {\n  listUserReadingHistoryByUpdatedTimeRevised(updatedAt: $updatedAt, nextToken: $nextToken, limit: $limit) {\n    items {\n      oid\n      updatedAt\n      lastRead\n      lastReadPage\n      lastReadChapterOID\n      showInRecent\n      __typename\n    }\n    nextToken\n    __typename\n  }\n}\n"}))

    # print(response)
