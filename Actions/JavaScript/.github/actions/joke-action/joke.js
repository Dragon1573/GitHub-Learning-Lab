const request = require("request-promise");

const options = {
    method: "GET",
    uri: "https://icanhazdadjoke.com/",
    headers: {
        // Instead of using JSON, I'll get plain text here.
        Accept: "text/plain",
        "User-Agent": "Writing JavaScript action GitHub Learning Lab course." +
            "  Visit lab.github.com or to contact us."
    },
};

async function getJoke() {
    const joke_response = await request(options);
    return joke_response;
}

module.exports = getJoke;
