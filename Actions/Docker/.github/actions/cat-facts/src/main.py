# Make an HTTP GET request to the cat-fact API
# The official API has changed
from requests import get

# This is just a string!!!
cat_url = "https://icanhazdadjoke.com/"
r = get(cat_url, headers={
    "Accept": "text/plain",
    "User-Agent": "Writing Docker action GitHub Learning Lab course. "
})

# Print the individual randomly returned cat-fact
print(r.text)

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=fact::{r.text}")
