import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_all_sizes, get_all_styles, get_all_types, get_all_orders
from views import get_single_type, get_single_metal, get_single_size, get_single_style
from views import create_order, get_single_order, delete_order, update_metal

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        """this function splits the url
        """
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    def do_GET(self):
        """Handles GET requests to the server
        """

        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)

            else:
                response = get_all_metals()

        if resource == "sizes":
            if id is not None:
                response = get_single_size(id)

            else:
                response = get_all_sizes()

        if resource == "types":
            if id is not None:
                response = get_single_type(id)

            else:
                response = get_all_types()

        if resource == "styles":
            if id is not None:
                response = get_single_style(id)

            else:
                response = get_all_styles()

        if resource == "orders":
            if id is not None:
                response = get_single_order(id)

            else:
                response = get_all_orders()
        if response is not None:
            self._set_headers(200)
        else:
            self._set_headers(404)
            response = {
                "message": f'{"That metal is not currently in stock for jewelry." if resource == "metals" else ""} {"That style is not currently in stock for jewelry." if resource == "styles" else ""} {"That size is not currently in stock for jewelry." if resource == "sizes" else ""}'
                }

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """this is the post function
        """
        
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_order = None
        # Add a new order to the list. Don't worry about
        # the orange squiggle, you'll define the create_order
        # function next.
        if resource == "orders":
            if "metal_id" in post_body and "size_id" in post_body and "style_id" in post_body and "type_id" in post_body:
                self._set_headers(201)
                new_order = create_order(post_body)
            else:
                self._set_headers(400)
                new_order = {
                    "message": f'{"metal_id is required" if "metal_id" not in post_body else ""} {"size_id is required" if "size_id" not in post_body else ""} {"style_id is required" if "style_id" not in post_body else ""} {"type_id is required" if "type_id" not in post_body else ""}'
                }

        self.wfile.write(json.dumps(new_order).encode())

    # def do_PUT(self):
    #     """This is the PUT function
    #     """
    #     self._set_headers(405)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Delete a single order from the list
    #     if resource == "orders":
    #         message = {
    #                 "message": f'{"Modifying requires contacting the company directly"}'
    #             }

    #     # Encode the new order and send in response
    #     self.wfile.write(json.dumps(message).encode())

    def do_PUT(self):
        """This method updates an existing dictionary"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "metals":
            success = update_metal(id, post_body)
        # rest of the elif's

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        """this function will delete items
        """
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single order from the list
        if resource == "orders":
            delete_order(id)

        # Encode the new order and send in response
            self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()



# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
