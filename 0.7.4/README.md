conan.io C++ Docker images
==========================

This repository contains the source for building C++ applications
using conan.io as a reproducible Docker image using
[source-to-image](https://github.com/openshift/source-to-image).
Users can choose between RHEL and CentOS based builder images.
The resulting image can be run using [Docker](http://docker.io).


Usage
---------------------
To build a simple [conan-sample-app](https://github.com/bachp/sti-conan/tree/master/0.10/test/test-app) application
using standalone [STI](https://github.com/openshift/source-to-image) and then run the
resulting image with [Docker](http://docker.io) execute:

*  **For RHEL based image**
    ```
    $ s2i build https://github.com/bachp/sti-conan.git --context-dir=0.7.4/test/test-app/ openshift/conan-074-rhel7 conan-sample-app
    $ docker run -p 8080:8080 conan-sample-app
    ```

*  **For CentOS based image**
    ```
    $ s2i build https://github.com/bachp/sti-conan.git --context-dir=0.7.4/test/test-app/ openshift/conan-074-centos7 conan-sample-app
    $ docker run -p 8080:8080 conan-sample-app
    ```

**Accessing the application:**
```
$ curl 127.0.0.1:8080
```


Repository organization
------------------------
* **`<conan-version>`**

    * **Dockerfile**

        CentOS based Dockerfile.

    * **Dockerfile.rhel7**

        RHEL based Dockerfile. In order to perform build or test actions on this
        Dockerfile you need to run the action on a properly subscribed RHEL machine.

    * **`s2i/bin/`**

        This folder contains scripts that are run by [STI](https://github.com/openshift/source-to-image):

        *   **assemble**

            Used to install the sources into the location where the application
            will be run and prepare the application for deployment (eg. installing
            modules using npm, etc.)

        *   **run**

            This script is responsible for running the application, by using the
            application web server.

        *   **usage***

            This script prints the usage of this image.

    * **`contrib/`**

        This folder contains a file with commonly used modules.

    * **`test/`**

        This folder contains the [S2I](https://github.com/openshift/source-to-image)
        test framework with simple Poco C++ HTTP time server.

        * **`test-app/`**

            A simple conan.io enabled Poco C++ HTTP time server used for testing purposes by the [S2I](https://github.com/openshift/source-to-image) test framework.

        * **run**

            This script runs the [S2I](https://github.com/openshift/source-to-image) test framework.
