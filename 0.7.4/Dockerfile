FROM openshift/base-centos7

# This image provides a conani.io environment you can use to run your C++
# applications.

MAINTAINER Pascal Bach <pascal.bach@nextrem.ch>

EXPOSE 8080

ENV CONAN_VERSION=0.7.4

LABEL io.k8s.description="Platform for building and running conan.io enabled C++ applications" \
      io.k8s.display-name="conan.io 0.7.4" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,conan.io"

RUN yum install -y centos-release-scl && \
    INSTALL_PKGS="python-pip cmake make gcc gcc-c++ kernel-devel" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y && \
    pip install "conan==$CONAN_VERSION" && \
    conan


# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH
COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# Each language image can have 'contrib' a directory with extra files needed to
# run and build the applications.
#COPY ./contrib/ /opt/app-root

# Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:0 /opt/app-root
USER 1001

# Set the default CMD to print the usage of the language image
CMD $STI_SCRIPTS_PATH/usage
