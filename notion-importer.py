#!/usr/bin/env python3
import json
import sys
from notion_client import Client
import requests
#

# Get the Notion API token and database ID from environment variables or pass them as arguments
NOTION_TOKEN = "secret_fGBwHt2ShJfeg5J7HJTT1EYGMF1VdQPenEhIDMgdCGw"
DATABASE_ID = "ff340fa6906a4f7dae8e9539bf4c07a0"

# Initialize Notion client
notion = Client(auth=NOTION_TOKEN)

# Read input data
data = sys.stdin.read()

# Validate input
if not data.strip():
    print("Error: No input data received.")
    sys.exit(1)

try:
    property_data = json.loads(data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    sys.exit(1)

# Ensure Photos is properly handled
photos = property_data.get("Photos", [])

# Prepare Notion properties
properties = {
    "Address": {
        "title": [{"text": {"content": property_data.get("Address", "N/A")}}]
    },
    "Price": {
        "number": float(property_data.get("Price", "N/A").replace("$", "").replace(",", "")) if property_data.get("Price") else None
    },
    "Beds": {
        "number": int(property_data.get("Beds", "0")) if property_data.get("Beds").isdigit() else None
    },
    "Baths": {
        "number": int(property_data.get("Baths", "0")) if property_data.get("Baths").isdigit() else None
    },
    "Sqft": {
        "number": int(property_data.get("Sqft", "0").replace(",", "")) if property_data.get("Sqft").replace(",", "").isdigit() else None
    },
    "Special Features": {
        "multi_select": [{"name": feature} for feature in property_data.get("Special Features", [])]
    },
    "Description": {
        "rich_text": [{"text": {"content": property_data.get("Description", "N/A")}}]
    },
    "Listing Agent": {
        "rich_text": [{"text": {"content": property_data.get("Listing Agent", "N/A")}}]
    },
    "Contact Phone": {
        "phone_number": property_data.get("Contact Phone", "N/A")
    },
    "Realtor": {
        "rich_text": [{"text": {"content": property_data.get("Realtor", "N/A")}}]
    },
    "MLS Number": {
        "rich_text": [{"text": {"content": property_data.get("MLS Number", "N/A")}}]
    },
    "Source": {
        "rich_text": [{"text": {"content": property_data.get("Source", "N/A")}}]
    },
    "Web Page URL": {
        "url": property_data.get("Web Page URL", "")
    }
}

# Create the page first
try:
    page = notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties=properties
    )
    print("Page created successfully!")
except Exception as e:
    print(f"Error creating page: {e}")
    sys.exit(1)

# Attach photos as files to the created page
page_id = page["id"]

for photo_url in photos:
    try:
        # Fetch the image to ensure it's accessible
        response = requests.get(photo_url)
        response.raise_for_status()

        # Upload the image to Notion
        notion.blocks.children.append(
            page_id,
            children=[
                {
                    "object": "block",
                    "type": "image",
                    "image": {
                        "type": "external",
                        "external": {"url": photo_url}
                    }
                }
            ]
        )
        print(f"Successfully uploaded photo: {photo_url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch photo from URL: {photo_url} - {e}")
    except Exception as e:
        print(f"Failed to upload photo: {photo_url} - {e}")

print("All data, including photos, sent to Notion successfully!")
