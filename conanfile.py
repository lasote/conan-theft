from conans import ConanFile, ConfigureEnvironment
import os
from conans.tools import download
from conans.tools import unzip, replace_in_file
from conans import CMake
from shutil import copyfile


class LibpngConan(ConanFile):
    name = "theft"
    version = "0.2.0"
    ZIP_FOLDER_NAME = "%s-%s" % (name, version)
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    url="http://github.com/lasote/conan-theft"
    license="https://github.com/silentbicycle/theft/blob/v0.2.0/LICENSE"
    exports=["CMakeLists.txt"]
    
    def config(self):
        self.settings.os.remove("Windows")
       
    def source(self):
        zip_name = "v%s.zip" % self.version
        download("https://github.com/silentbicycle/theft/archive/%s" % zip_name, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        """ Define your project building. You decide the way of building it
            to reuse it later in any other project.
        """
        env = ConfigureEnvironment(self.deps_cpp_info, self.settings)

        if self.settings.os == "Linux" or self.settings.os == "Macos":            
            self.run("cd %s && %s make" % (self.ZIP_FOLDER_NAME, env.command_line))
#        Windows not compile!!!!
#         else:
#             copyfile("CMakeLists.txt", "%s/CMakeLists.txt" % self.ZIP_FOLDER_NAME)
#             cmake = CMake(self.settings)
#             self.run("cd %s && mkdir _build" % self.ZIP_FOLDER_NAME)
#             cd_build = "cd %s/_build" % self.ZIP_FOLDER_NAME
#             self.run('%s && cmake .. %s' % (cd_build, cmake.command_line))
#             self.run("%s && cmake --build . %s" % (cd_build, cmake.build_config))
                
    def package(self):
        """ Define your conan structure: headers, libs, bins and data. After building your
            project, this method is called to create a defined structure:
        """
        # Copying headers
        self.copy("*.h", "include", "%s" % (self.ZIP_FOLDER_NAME), keep_path=False)

        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=self.ZIP_FOLDER_NAME, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["theft"]
