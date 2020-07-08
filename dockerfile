FROM centos:7
RUN yum -y install nginx
RUM echo "this is the test" >  /usr/share/nginx/html/index.html
EXPOSE 80/tcp
CMD ["nginx", "-g daemon off;"]
