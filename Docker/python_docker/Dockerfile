FROM centos:6
MAINTAINER eyu's fanne

ADD CentOS-Base.repo /etc/yum.repos.d/
ADD pypage.txt /data/
COPY Python-2.7.9 /data/Python-2.7.9/
COPY setuptools-18.0.1 /data/setuptools-18.0.1/
COPY pip-7.1.0 /data/pip-7.1.0/

RUN yum clean all && yum makecache
RUN yum install -y python-devel python-pip gcc-c++ make cmake zlib-devel zlib openssl-devel

WORKDIR /data/Python-2.7.9/
RUN ./configure --prefix=/usr/local/python2.7.9 && make && make install
RUN mv /usr/bin/python /usr/bin/python_bak
RUN ln -s /usr/local/python2.7.9/bin/python2.7 /usr/bin/python
RUN sed -i '1s/\/usr\/bin\/python/\/usr\/bin\/python2.6/g' /usr/bin/yum

WORKDIR /data/setuptools-18.0.1
RUN python setup.py install
RUN ln -s /usr/local/python2.7.9/bin/easy_install /usr/bin/easy_install

WORKDIR /data/pip-7.1.0/
RUN python setup.py install
RUN ln -s /usr/local/python2.7.9/bin/pip /usr/bin/pip
RUN pip install ipython
RUN ln -s /usr/local/python2.7.9/bin/ipython /usr/bin/ipython

WORKDIR /data/
RUN pip install -r pypage.txt

WORKDIR /

CMD ["/bin/bash"]

