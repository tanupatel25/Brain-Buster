# trivial dockerfile to create Programming Language environment

FROM gcc

RUN echo "alias run-app='gcc -Wall -g -gdwarf-4 spreadsheet.c && ./a.out'" >> /etc/bash.bashrc
RUN git config --global user.email "tanu@concordia.edu"
RUN git config --global user.name "Tanu"

RUN apt-get update && apt-get install -y \
    bash-completion   \
    cmake             \
    valgrind          \
    nano              \
    scons             \
    clojure           \
    leiningen         \
    erlang            \
    rebar             \  
    
    && rm -rf /var/lib/apt/lists/*