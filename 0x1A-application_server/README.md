0x1A. Application server
DevOps
SysAdmin

Resources
Read or watch:

Application server vs web server
How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
Running Gunicorn
Be careful with the way Flask manages slash in route - strict_slashes
Upstart documentation

Here are some key differences between a web server and an application server:

Web Server12:
It is designed to serve HTTP content2.
It is mostly designed to serve static content such as HTML, CSS, JavaScript, and images13.
It encompasses a web container only1.
It consumes or utilizes less resources1.
It arranges the run environment for web applications1.
It supports multithreading1.
It uses HTML and HTTP protocols1.
It supports processes that are not resource-intensive1.
It does not support transactions and connection pooling1.
Its capacity of fault tolerance is low compared to application servers1.
Examples of web servers are Apache HTTP Server, Nginx1.
Application Server12:
It can also serve HTTP content but is not limited to just HTTP2.
It hosts web applications that deliver dynamic content by accessing and processing databases and web services3.
It encompasses both a web container and an EJB container1.
It utilizes more resources1.
It arranges the run environment for enterprise applications1.
It does not support multithreading1.
It uses GUI as well as HTTP and RPC/RMI protocols1.
It supports resource-intensive processes1.
It supports transactions and connection pooling1.
It has high fault tolerance1.
Examples of application servers are JBoss, Glassfish1.
In summary, a web server is well suited for serving static content and an application server is better suited for serving dynamic content2. Most of the production environments have a web server acting as a reverse proxy to an application server
