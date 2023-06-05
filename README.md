
# How to Track Gumroad Sales in Notion Using Notion API and Python

![A screenshot of Notion Dashboard](https://tnvmadhav.me/guides/how-to-track-gumroad-sales-in-notion-using-notion-api-and-python/img/cover_hu98e002cd453fa9f7425a9edbe546f119_12500271_1280x0_resize_q75_bgffffff_box_3.jpg)

*A screenshot of Notion Dashboard with live API update*

## Introduction

In this tutorial, you’ll learn how to track Gumroad[^1] sales in real-time in Notion[^2] using 🐍 Python.

You will also learn,
- What are APIs?
- How to use Gumroad API?
- How to use Notion API?
- How run a python script in Replit etc

## What are APIs?

APIs stand for Application Programming Interfaces.

Let’s break this term down,

→ An Application is any website or app like Twitter, Facebook, Instagram, Reddit etc.

→ Programming Interfaces  are a way to talk to these applications

APIs are way to for your code to read information from (or) write information to said applications in an instant.


## Why use APIs?

---

APIs are a great way to automate tasks.

For example, if you want to publish a post to social media, you can use a scheduler like HootSuite[^3] (or) Buffer[^4]. 

If you have a social-media post scheduled for 6:00 PM, the scheduling software will write your post to the social media app using their APIs. 

So APIs are a way to do things really quickly and really efficiently.

A way to talk to APIs is to use **a programming language**.

![A mermaid markdown diagram to represent how APIs are called](https://tnvmadhav.me/guides/how-to-track-gumroad-sales-in-notion-using-notion-api-and-python/img/API_huefd04bdd4e5bc258ff782f4372df0b61_10494358_1280x0_resize_q75_bgffffff_box_3.jpg)

*Programming languages like Javascript (or) Python can be used to talk to Apps using API*

Let’s understand this using an example.

## Understanding APIs using a real world analogy

 **Imagine a postal delivery system.** 

An API (Application Programming Interface) acts as **a request receiver's letterbox** in the postal delivery system analogy. 

It is the gateway through which a **sender** (programming language) can send **letter** (the data) to the request **receiver’s letter box** (Application’s API endpoint). 

Once the data is received by the API endpoint, it can be processed by the the Application, which then returns an acknowledgement along with the requested data if any.


> 🔑 Remember:
>
> Just as a postal system has rules and constraints, an API system has a defined set of protocols, standards, and endpoints that determine how data can be transmitted between the sender and the receiver. 
>
> The sender (programming language) needs to conform to these rules to ensure that the data is correctly received and processed by the API.

In this tutorial, you’ll learn about two `applications` and talk to them via their respective `API`s:

1. Notion 
2. Gumroad

At the end of your tutorial, you’ll learn to use Notion API and Gumroad API using Python.

> 🔑 What is Python?
>
> Python is a free and powerful programming language used by millions of software developers to build apps and websites. It’s also super easy to use.


## Get started with Gumroad API

---

We will use Gumroad API to read your store products. This data will be used to update your Notion dashboard automatically using Notion API.

To read your store information, Gumroad needs to know it’s you who are requesting for it. To help gumroad understand this, we will be passing in a shared secret token along with the API request that only you and gumroad know about.

### Mission: Acquire Gumroad API Secret Token

---

If you aren’t already aware, you can generate an API secret token by creating an application from the **Settings** → **Advanced** → **Applications** option from Gumroad’s dashboard.

![A screenshot of Gumroad Dashboard where an application instance can be created](https://tnvmadhav.me/guides/how-to-track-gumroad-sales-in-notion-using-notion-api-and-python/img/gumroad-api-dashboard_huf24d1e597525f44096924be01cfbece9_184573_1280x0_resize_q75_bgffffff_box_3.jpg)

Steps:

1. Provide an Application Name (Any name that you are comfortable with)
2. Redirect UI - we don’t really need this, so you can set the value `http://localhost`
3. Upload any icon you want (optional)
4. Click on `Create application` button
5. Once that’s done, click on a button called `Generate access token` in the next step. Access Token (your API secret key) will be generated.  Copy the text and keep it aside safely.


> 🔑 Do not share your secret key with anyone.

**You have now successfully acquired the Gumroad API secret key.**

Now you can request to read all your Gumroad store products along with this secret key so gumroad can verify and validate that it’s really you who is making this call.

### Mission: Request for your Gumroad store data using Python and your Gumroad secret token

---

Gumroad has an API documentation, a document that let’s developers know what all API endpoints (links) they can request to read or write information.

> ✨ If you want to go deeper into the world of Gumroad API, you can get started with this document → https://app.gumroad.com/api

For the sake of this tutorial, the API endpoint we need,  to read your store products details is as follows:

```
https://api.gumroad.com/v2/products
```

Making a `READ` request to this API endpoint (url) along with your secret token will return you all your Gumroad store products in a JSON format.

#### 🔑 What is JSON format?

Instead of giving you a unreadable paragraph of your store products and their information, JSON is a structured way of passing along data.

A simple json object has 2 things you need to know, key and value. They’re often called key-value pair.

For example, if you want to pass a question and answer to someone, you can pass it as a JSON object.

```json
{
	"Which planet do we live in?": "Earth",
}
```

Here, the key is the question, and the value is the answer.

A JSON usually readable by programming languages and big software pass along complex JSON objects which can be read and processed very fast by programming languages under the hood.

---

Coming back to the Gumroad API, `https://api.gumroad.com/v2/products` returns the lists of products as a JSON notation.

Let’s understand the full flow here,

1. You send a request ot Gumroad to this API endpoint  (`https://api.gumroad.com/v2/products`) along with a secret token
    
    This is how we do it in Python:
    
    ```python
    import requests
    
    url = "https://api.gumroad.com/v2/products"
    
    payload='access_token=ACCESS_TOKEN'
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    print(response.text)
    ```
    
2. Gumroad will verify the request and return a list of your products in JSON format.

    ```json
    {
      "success": true,
      "products": [{
        "custom_permalink": null,
        "custom_receipt": null,
        "custom_summary": "You'll get one PSD file.",
        "custom_fields": [],
        "customizable_price": null,
        "description": "I made this for fun.",
        "deleted": false,
        "max_purchase_count": null,
        "name": "Pencil Icon PSD",
        "preview_url": null,
        "require_shipping": false,
        "subscription_duration": null,
        "published": true,
        "url": "http://sahillavingia.com/pencil.psd",
        "id": "A-m3CDDC5dlrSdKZp0RFhA==",
        "price": 100,
        "purchasing_power_parity_prices": {
          "US": 100,
          "IN": 50,
          "EC": 25
        },
        "currency": "usd",
        "short_url": "https://sahil.gumroad.com/l/pencil",
        "thumbnail_url": "https://public-files.gumroad.com/variants/72iaezqqthnj1350mdc618namqki/f2f9c6fc18a80b8bafa38f3562360c0e42507f1c0052dcb708593f7efa3bdab8",
        "tags": ["pencil", "icon"],
        "formatted_price": "$1",
        "file_info": {},
        "shown_on_profile": true,
        "sales_count": "0", # available with the 'view_sales' scope
        "sales_usd_cents": "0", # available with the 'view_sales' scope
        "is_tiered_membership": true,
        "recurrences": ["monthly"], # if is_tiered_membership is true, renders list of available subscription durations; otherwise null
        "variants": [
          {
            "title": "Tier",
            "options": [
              {
                "name": "First Tier",
                "price_difference": 0, # set for non-membership product options
                "is_pay_what_you_want": false,
                "recurrence_prices": { # present for membership products; otherwise null
                  "monthly": {
                    "price_cents": 300,
                    "suggested_price_cents": null # may return number if is_pay_what_you_want is true
                  }
                }
              }
            ]
          }
        ]
      }, {...}, {...}]
    }
    ```
    
    > 💡 JSON objects are usually complex and are harder to understand for humans but programming languages and computers prefer this over just paragraphs of text to fast processing.
    
    Now, that you’ve understood how Gumroad API works, we will now learn how to upload the store data to Notion. 
    
    We can do this using the aforementioned, Notion API. 
    
    ## Getting started with Notion API
    
    ---
    
    Notion API provides capabilities to read and write data into your Notion workspace using code.
    
    Just like for Gumroad API, NotionAPI needs you to pass a secret token along with API request to verify it’s really you who is requesting an API endpoint.
    
    ### Mission: Generating Notion Integration along with a secret key for NotionAPI
    
    ---
    
    To generate Notion API secret key, follow these steps:
    
    1. Go to https://www.notion.so/my-integrations/
    2. Click on the `+ New Integration` button
    3. Give it a name
    4. Upload a logo (optional)
    5. Select your Notion Account in case you have multiple accounts
    6. Click on `Submit`
    7. You’ll be presented with a secret key. Copy this secret key and keep it aside for later use.
    
    > 🔑 Do not share your secret key with anyone.
    
    ### Mission: Building your Notion Database
    
    ---

    #### Get the Notion Template
    
    → [I’ve already built the Notion Template. You can grab it here](https://madhavtnv.gumroad.com/l/qweky) with discount coupon: `gumnotion` to get 50% off.
    
    If you wan to build one for youself, you can refer to the given python code for the schema design.
    
    ### Mission: Connecting your Notion Database with the Notion Integration
    
    ---
    
    To connect the dupliated notion database with the notion integration, follow these steps:
    
    1. Click on the three dots on the top right of the database page
    2. Click on the `Add Connection` option, search for and select the notion integration you created
    
    > 🔑 Ensure the Notion integration isn’t connected to any other database (or) page to prevent unwanted problems.

    
    ### Mission: Making a write request to store data into your Notion Workspace
    
    ---
    
    Once you’ve duplicated the Notion template containing the database. You can now think of making API requests to Notion to write your product details into it.
    
    If you’re interested to dig deeper into Notion API, you can start here → https://developers.notion.com/reference/intro
    
    The core API endpoint we will be using to write data into Notion will be, 
    
    ```python
    https://api.notion.com/v1/pages/
    ```
    
    Let’s understand the full flow here,
    
    1. You make a WRITE request to [`https://api.notion.com/v1/pages/`](https://api.notion.com/v1/pages/) API endpoint
        
        ```python
        import requests
        import json
        
        url = "https://api.notion.com/v1/pages/"
        
        payload = json.dumps({
          "cover": {
            "type": "external",
            "external": {
              "url": ""
            }
          },
          "parent": {
            "database_id": "<DATABASE-ID>"
          },
          "properties": {
            "Sales Count": {
              "type": "number",
              "number": 0
            },
            "Revenue": {
              "type": "number",
              "number": 0
            },
            "id": {
              "type": "rich_text",
              "rich_text": [
                {
                  "type": "text",
                  "text": {
                    "content": "<product-id>",
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
                  "plain_text": "<product-id>",
                  "href": None
                }
              ]
            },
            "Link": {
              "type": "url",
              "url": "<product-url>"
            },
            "Price": {
              "type": "number",
              "number": 1000
            },
            "Name": {
              "id": "title",
              "type": "title",
              "title": [
                {
                  "type": "text",
                  "text": {
                    "content": "<Your-Gumroad-Product-Name>",
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
                  "plain_text": "<Your-Gumroad-Product-Name>",
                  "href": None
                }
              ]
            }
          }
        })
        headers = {
          'Content-Type': 'application/json',
          'Notion-Version': '2022-02-22',
          'Authorization': 'Bearer <secret-token>',
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        
        print(response.text)
        ```
        
    2. Notion validates and writes received product into your Notion database and returns a sucessful response as a JSON object. This for example:
        
        ```python
        {
          "object": "page",
          "id": "59833787-2cf9-4fdf-8782-e53db20768a5",
          "created_time": "2022-03-01T19:05:00.000Z",
          "last_edited_time": "2022-07-06T19:16:00.000Z",
          "created_by": {
            "object": "user",
            "id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
          },
          "last_edited_by": {
            "object": "user",
            "id": "ee5f0f84-409a-440f-983a-a5315961c6e4"
          },
          "cover": {
            "type": "external",
            "external": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
            }
          },
          "icon": {
            "type": "emoji",
            "emoji": "🥬"
          },
          "parent": {
            "type": "database_id",
            "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce"
          },
          "archived": false,
          "properties": {
            "Store availability": {
              "id": "%3AUPp"
            },
            "Food group": {
              "id": "A%40Hk"
            },
            "Price": {
              "id": "BJXS"
            },
            "Responsible Person": {
              "id": "Iowm"
            },
            "Last ordered": {
              "id": "Jsfb"
            },
            "Cost of next trip": {
              "id": "WOd%3B"
            },
            "Recipes": {
              "id": "YfIu"
            },
            "Description": {
              "id": "_Tc_"
            },
            "In stock": {
              "id": "%60%5Bq%3F"
            },
            "Number of meals": {
              "id": "zag~"
            },
            "Photo": {
              "id": "%7DF_L"
            },
            "Name": {
              "id": "title"
            }
          },
          "url": "https://www.notion.so/Tuscan-Kale-test"
        }
        ```
        
    
> 🔑 The requests and responses look a bit intimidating because Notion is a complex data store. If everything is done right, you don’t have to personally deal with these responses.
    

## Connecting both Notion and Gumroad APIs

---

Now that that you’ve gotten some idea on how APIs can be used, let’s try to combine the request and responses to do exactly what we need.

![A sequence diagram of how we plan to talk to gumroad and notion using APIs](https://tnvmadhav.me/guides/how-to-track-gumroad-sales-in-notion-using-notion-api-and-python/img/sequence_hu8d43d2b8e08806351bbb7cdaa356ff71_8367419_1280x0_resize_q75_bgffffff_box_3.jpg)
*A sequence diagram of how we plan to talk to gumroad and notion using APIs*

The following is the python script that I wrote ,that you can run to pull product information from gumroad save it to your notion database.

```python
import json
import time
import requests
import traceback
import sys
import os

class MyIntegration:

    def __init__(self):
        """
        Gets required variable data from config yaml file.
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
```

Now, I’ll show you how to run this code on Replit, a popular cloud based code hosting and execution environment.

## Running the Python script on Replit:

---

1. Create a free account on [Replit](https://replit.com/) and login,
2. Fork my REPL: https://replit.com/@tnvmadhav/Notion-Gumroad-Sync

> 🍴 *Forking* means making a copy of someone else’s public repository

3. After forking into your workspace, share the Gumroad and Notion API secret keys with the Python Script
    1. Click on `Secrets` box in the Left Sidebar
    2. Add the following variables & their respective tokens that were kept aside before into the form
        1. MY_NOTION_SECRET_TOKEN
        2. MY_GUMROAD_SECRET_TOKEN

    ![A screenshot of how to save API keys inside Replit secret keys form](https://tnvmadhav.me/guides/how-to-track-gumroad-sales-in-notion-using-notion-api-and-python/img/replit_hu9201d76ab9f53992db2547dfd89b61e9_6919146_1280x0_resize_q75_bgffffff_box_3.jpg)
4. Run the script from your browser!

   ![A screenshot of the Run button on Replit](https://tnvmadhav.me/guides/how-to-track-gumroad-sales-in-notion-using-notion-api-and-python/img/run_hu04d595c4b387d1bd297b3999f85ab985_4470878_1280x0_resize_q75_bgffffff_box_3.jpg)

That’s it! 

If all went well, you should see your Gumroad Product information automatically update every 30 seconds. 

> 🔑 You can keep the python script running if you like to keep up with live sales and revenue updates but Replit might charge money to keep your script running forever.

Thanks for reading.

If you liked this guide, you may also like a similar guide I wrote on [Tracking Habits in Notion](https://tnvmadhav.me/blog/daily-task-automator/) using Python API.


👋 [-- @TnvMadhav](https://tnvmadhav.me/contact)


## Reference

[^1]: [Gumroad -- Go from zero to $1](https://gumroad.com)

[^2]: [Notion -- Your wiki, docs, & projects. Together](https://notion.so)

[^3]: [HootSuite -- Save time and get REAL results on social media](https://www.hootsuite.com)

[^4]: [Buffer -- Grow your audience on social and beyond](https://buffer.com)