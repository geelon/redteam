import subprocess
import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options
import hashlib
import pickle

define("port", default=8080, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, {
                "path": "mnist"
                })
        ]
        tornado.web.Application.__init__(self, handlers)
        
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome! Note that prediction generation takes 30+ seconds.")
        self.render("upload_form.html")

#id_to_prediction_dict = {}

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        id = str(self.get_argument('ID'))
        with open("output/id.pickle", 'wb') as f:
            pickle.dump(id , f)
        output = subprocess.call("./script.sh", shell=True)
        with open("output/output.pkl", 'rb') as f:
            prediction = str(pickle.load(f))
        self.write("Predicting based on image " + str(id) + " to be " + prediction + " .<br> <br>")
        self.write('<img src="/static/%s.png" />' % (str(id)))

        # if 'input_file' in self.request.files:
        #     input_file = self.request.files['input_file'][0]
        #     original_fname = input_file['filename']
        #     extension = os.path.splitext(original_fname)[1]
        #     fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
            
        #     parts_of_filename = original_fname.split(".")
        #     final_filename = parts_of_filename[0]+"_output."+parts_of_filename[1]
            
        #     output_file = open("output/" + final_filename, 'wb')
        #     output_file.write(input_file['body'])
        #     self.write("File " + final_filename + " is uploaded. ")

        #     encoded_filename = original_fname.encode('utf-8')
        #     id_for_file = str(int(hashlib.sha1(encoded_filename).hexdigest(), 16) % (10 ** 8))
        #     id_to_prediction_dict[id_for_file] = "prediction_"+ id_for_file

        #     self.write("Your ID: " + id_for_file)
        # else:
        #     id = self.get_argument('ID')
        #     self.write("Prediction: " + id_to_prediction_dict[id])

        self.render("upload_form.html")
        
def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == "__main__":
    main()
