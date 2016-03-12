conan.io C++ Docker images
==========================

This repository contains the source for building C++ applications
using conan.io as a reproducible Docker image using
[source-to-image](https://github.com/openshift/source-to-image).
Users can choose between RHEL and CentOS based builder images.
The resulting image can be run using [Docker](http://docker.io).

For more information about using these images with OpenShift, please see the
official [OpenShift Documentation](https://docs.openshift.org/latest/using_images/s2i_images/conan.html).


Versions
---------------
conan.io versions currently provided are:
* conan-0.7.4

RHEL versions currently supported are:
* RHEL7

CentOS versions currently supported are:
* CentOS7


Installation
---------------
To build a conan.io C++ image, choose either the CentOS or RHEL based image:
*  **RHEL based image**

    To build a RHEL based conen-0.6 image, you need to run the build on a properly
    subscribed RHEL machine.

    ```
    $ git clone https://github.com/bachp/sti-conan.git
    $ cd sti-conant
    $ make build TARGET=rhel7 VERSION=0.7.4
    ```

*  **CentOS based image**

    This image is available on DockerHub. To download it run:

    ```
    $ docker pull openshift/conan-074-centos7
    ```

    To build a conan.io image from scratch run:

    ```
    $ git clone https://github.com/bachp/sti-conan.git
    $ cd sti-conan
    $ make build VERSION=0.7.4
    ```

**Notice: By omitting the `VERSION` parameter, the build/test action will be performed
on all provided versions of conan.io . Since we are currently providing only version `0.7.4`,
you can omit this parameter.**


Usage
---------------------------------

For information about usage of Dockerfile for conan.io 0.7.4,
see [usage documentation](0.7.4/README.md).


Test
---------------------
This repository also provides a [S2I](https://github.com/openshift/source-to-image) test framework,
which launches tests to check functionality of a simple C++ application built on top of the sti-conan image.

Users can choose between testing a C++ test application based on a RHEL or CentOS image.

*  **RHEL based image**

    To test a RHEL7 based Conan 0.7.4 image, you need to run the test on a properly
    subscribed RHEL machine.

    ```
    $ cd sti-conan
    $ make test TARGET=rhel7 VERSION=0.7.4
    ```

*  **CentOS based image**

    ```
    $ cd sti-conan
    $ make test VERSION=0.7.4
    ```

**Notice: By omitting the `VERSION` parameter, the build/test action will be performed
on all provided versions of conan.io. Since we are currently providing only version `0.7.4`
you can omit this parameter.**


Repository organization
------------------------
* **`<conan-version>`**

    Dockerfile and scripts to build container images from.

* **`hack/`**

    Folder containing scripts which are responsible for the build and test actions performed by the `Makefile`.


Image name structure
------------------------
##### Structure: openshift/1-2-3

1. Platform name (lowercase) - conan
2. Platform version(without dots) - 074
3. Base builder image - centos7/rhel7

Examples: `openshift/conan-074-centos7`, `openshift/conan-074-rhel7`
