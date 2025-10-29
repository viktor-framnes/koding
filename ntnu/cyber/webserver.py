from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import quote, unquote
import json
import socket


def extract_json_string(string):
    start = string.find("{")
    stop = string.rfind("}")
    return string[start : stop + 1]


def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


def dictionary_to_string(dictionary):
    return json.dumps(dictionary)


def json_string_to_dictionary(json_string):
    return json.loads(json_string)


def encode_string_into_url(string):
    return quote(string)


def decode_url_back_to_string(url_encoded_string):
    return unquote(url_encoded_string)


def string_to_unicode_bytes(string):
    return string.encode("utf-8")


class RequestHandler(BaseHTTPRequestHandler):
    def store_data(self, name, data):
        if not hasattr(self.server, "data"):
            self.server.data = {}
        self.server.data[name] = data

    def load_data(self, name):
        if hasattr(self.server, "data"):
            if name in self.server.data:
                return self.server.data[name]
        return None

    def do_GET(self):
        # Phase 1: What has been requested?
        print("-------- Incoming GET request --------")
        print("  Request data: {}".format(self.requestline))

        # Phase 2: Which data do we want to send back?
        response = "Hei hei"

        # Phase 3: Let's send back the data!
        response_in_bytes = string_to_unicode_bytes(response)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response_in_bytes)

    def do_POST(self):
        """HTTP POST request as it comes from the sensor device application,
        for instance to send the current temerature."""

        print("-------- Incoming POST request --------")
        print("  Request data: {}".format(self.requestline))

        decoded_request = decode_url_back_to_string(self.requestline)
        print("  Decoded data: {}".format(decoded_request))

        json_string = extract_json_string(decoded_request)
        print("  Extracted JSON string: {}".format(json_string))

        dictionary = json_string_to_dictionary(json_string)
        print(dictionary)

        # We extract the temperature...
        temperature = dictionary["temperature"]
        print(f"Temperature {temperature} received in do_POST()")
        # ...and store it
        self.store_data("temperature", temperature)

        # Phase 2: Which data do we want to send back?
        response = "ok"

        # Phase 3: Let's send back the data!
        response_in_bytes = string_to_unicode_bytes(response)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response_in_bytes)

port = 8023
httpd = HTTPServer(
    ("", port),
    RequestHandler,
)
print("")
print(" ******** TTM4175 Web Server  ******** ")
print(
    "    The server will be reachable via  http://{}:{}/".format(get_ip_address(), port)
)
print("    Terminate the server via Ctrl-C.")
print(" ************************************* ")
print("")
httpd.serve_forever()