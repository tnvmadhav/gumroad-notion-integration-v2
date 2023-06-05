import json
import time
import requests
import traceback
import sys
import os


class MyIntegration:

    def __init__(self):
        """
        Gets required secrets from environment variables.
        """
        self.my_variables_map = {
            "MY_NOTION_SECRET_TOKEN": os.getenv("MY_NOTION_SECRET_TOKEN"),
            "MY_GUMROAD_SECRET_TOKEN": os.getenv("MY_GUMROAD_SECRET_TOKEN"),
            "NOTION_ENTRIES": {},
        }
        self.fallback_cover_image_url = (
            "https://assets-global.website-files.com/6171b265e5c8aa59b42c3472/6195275a9e5f4655891de886_gum-coins.svg"  # noqa: E501
        )
        self.get_page_and_database_data()

    def get_page_and_database_data(self):
        url = "https://api.notion.com/v1/search"
        headers = {
            "Content-Type": "application/json",
            'Notion-Version': '2022-02-22',
            'Authorization':
                'Bearer ' + self.my_variables_map["MY_NOTION_SECRET_TOKEN"]
        }
        payload = json.dumps({
            "query": 'Store',
            "filter": {
                "value": "database",
                "property": "object"
            }
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        self.my_variables_map["DATABASE_ID"] = \
            response.json()["results"][0]["id"]
        # Database Entries
        url = f"https://api.notion.com/v1/databases/"\
              f"{self.my_variables_map['DATABASE_ID']}/query"
        response = requests.request("POST", url, headers=headers)
        resp = response.json()
        for v in resp["results"]:
            self.my_variables_map["NOTION_ENTRIES"].update({
                v["properties"]["id"]["rich_text"][0]["plain_text"]: {
                    "Sales Count": v["properties"]["Sales Count"]["number"],
                    "Price": v["properties"]["Price"]["number"],
                    "Revenue": v["properties"]["Revenue"]["number"],
                    "Link": v["properties"]["Link"]["url"],
                    "Name": v["properties"]["Name"]["title"][0]["plain_text"],
                    "id": v["properties"]["id"]["rich_text"][0]["plain_text"],
                    "cover": v["cover"]["external"]["url"],
                    "page_id": v['id']
                }
            })

    def get_gumroad_products(self):
        url = "https://api.gumroad.com/v2/products/"
        headers = {
            'Authorization': 'Bearer ' +
            self.my_variables_map["MY_GUMROAD_SECRET_TOKEN"],
        }
        response = requests.request("GET", url, headers=headers)
        for i in response.json()["products"]:
            self.update_notion_entries(i)

    def update_notion_entries(self, data):
        or_data_page_id = self.my_variables_map["NOTION_ENTRIES"].get(
            data['id'], {}
        ).get('page_id', None)
        self.my_variables_map["NOTION_ENTRIES"].update({
            data["id"]: {
                "Name": data["name"],
                "Price": float(data["price"]) / 100,
                "Sales Count": data["sales_count"],
                "Revenue": float(data["sales_usd_cents"]) / 100,
                "Link": data["short_url"],
                "id": data["id"],
                "cover": data.get(
                    "preview_url", self.fallback_cover_image_url
                ) or self.fallback_cover_image_url,
                "page_id": or_data_page_id
            }
        })

    def update_notion_database(self, database_id, data):
        if data.get("page_id"):
            url = "https://api.notion.com/v1/pages/" + str(data.get("page_id"))
            method = "PATCH"
        else:
            url = "https://api.notion.com/v1/pages/"
            method = "POST"
        headers = {
            'Authorization':
                'Bearer ' + self.my_variables_map["MY_NOTION_SECRET_TOKEN"],
            'Notion-Version': '2022-02-22',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "cover": {
                "type": "external",
                "external": {
                    "url": data["cover"]
                }
            },
            "parent": {
                "database_id": database_id
            },
            "properties": {
                "Sales Count": {
                        "type": "number",
                        "number": float(data["Sales Count"])
                },
                "Revenue": {
                    "type": "number",
                    "number": float(data["Revenue"])
                },
                "id": {
                    "type": "rich_text",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": data["id"],
                                "link": None
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": data["id"],
                            "href": None
                        }
                    ]
                },
                "Link": {
                    "type": "url",
                    "url": data["Link"]
                },
                "Price": {
                    "type": "number",
                    "number": float(data["Price"])
                },
                "Name": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": data["Name"],
                                "link": None
                            },
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default"
                            },
                            "plain_text": data["Name"],
                            "href": None
                        }
                    ]
                }
            }
        })
        response = requests.request(method, url, headers=headers, data=payload)
        return response.json()["id"]

    def update_indefinitely(self):
        while True:
            try:
                self.get_gumroad_products()
                for _, data in self.my_variables_map["NOTION_ENTRIES"].items():
                    data["page_id"] = self.update_notion_database(
                        data=data,
                        database_id=self.my_variables_map["DATABASE_ID"]
                    )
                    time.sleep(5)
                time.sleep(10)
            except Exception:
                traceback.print_exception(*sys.exc_info())
                # Drop memory and rebuild from existing notion server state
                self.my_variables_map["NOTION_ENTRIES"] = {}
                self.get_page_and_database_data()


if __name__ == "__main__":
    # With 😴 sleeps to prevent rate limit from kicking in.
    MyIntegration().update_indefinitely()
