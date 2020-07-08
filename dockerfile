
FROM mahisakapal/dir:myimge
RUN yum -y install nginx
RUN echo "this is the test" >  /usr/share/nginx/html/index.html
EXPOSE 80/tcp
CMD ["nginx", "-g daemon off;"]
