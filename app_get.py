from http.server import HTTPServer,BaseHTTPRequestHandler

class Servidor (BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"servidor backend funcionando")


    def do_POST(self):

        tamanho = int(self.headers['Content-Length'])

        dado = self.rfile.read(tamanho)

        print("Dados recebidos:", dado.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST RECEBIDO")


HTTPServer(("0.0.0.0", 8000), Servidor).serve_forever()





