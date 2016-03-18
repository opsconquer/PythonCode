有时我们需要一个建立RPC服务简单而快速的方法。我们需要的只是让程序B去调用程序A(可能在另一个机器上)的方法。

我们不用了解关于这个的任何技术，但是我们只是需要这么个简单的东西，我们可以使用一个叫做 XML-RPC 的协议(对应的Python库实现 SimpleXMLRPCServer )来处理这种事。

这里是一个简单粗糙的文件阅读服务器:

from SimpleXMLRPCServer import SimpleXMLRPCServer

def file_reader(file_name):
    with open(file_name, 'r') as f:
        return f.read()

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_introspection_functions()

server.register_function(file_reader)

server.serve_forever()

响应它的客户端:

import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://localhost:8000/')
proxy.file_reader('/tmp/secret.txt')
现在我们就有了一个远程的文件阅读器，除了一点代码，没有外部依赖。(当然，不安全，所以只在”家”用这个吧)
