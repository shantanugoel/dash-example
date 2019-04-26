FROM shantanugoel/ubuntu-py2-py3

RUN apt install -y sudo && \
    useradd -ms /bin/bash user && \
    echo "user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user && \
    chmod 0440 /etc/sudoers.d/user

USER user

WORKDIR /home/user

CMD ["/bin/bash"]