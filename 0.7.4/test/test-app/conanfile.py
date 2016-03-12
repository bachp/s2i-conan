from conans import ConanFile, CMake

class HTTPTimeServerConan(ConanFile):
    name = "HTTPTimeServer"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    requires = "Poco/1.6.1@lasote/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake . %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)
