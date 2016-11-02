from conans import ConanFile
import os
from conans.tools import download, unzip, replace_in_file
from conans import CMake, ConfigureEnvironment


class MysqlConnectorConan(ConanFile):
    name = "mysql-connector-cpp"
    version = "2.0.3"
    ZIP_FOLDER_NAME = "mysql-connector-cpp-%s" % version
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    # exports = 
    url="http://github.com/lasote/conan-mysql-connector-cpp"
    license="GPL: https://github.com/mysql/mysql-connector-cpp/blob/2.0/COPYING.txt"
    requires = "Boost/1.60.0@lasote/stable"
    
    def source(self):
        zip_name = "mysql-connector"
        download("https://github.com/lasote/mysql-connector-cpp/archive/%s.zip" % self.version, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        """ Define your project building. You decide the way of building it
            to reuse it later in any other project.
        """

        cmake = CMake(self.settings)
        
        conan_magic_lines = '''project(mysql_connector_cpp)
    CMAKE_MINIMUM_REQUIRED(VERSION 2.8.11)
    include(../conanbuildinfo.cmake)
    CONAN_BASIC_SETUP()
    '''
        replace_in_file("%s/CMakeLists.txt" % self.ZIP_FOLDER_NAME, "CMAKE_MINIMUM_REQUIRED(VERSION 2.8.11)", conan_magic_lines)        
        # replace_in_file("%s/cdk/CMakeLists.txt" % self.ZIP_FOLDER_NAME, "INCLUDE(protobuf)", "")
        if not os.path.exists("%s/_build" % self.ZIP_FOLDER_NAME):
            self.run("mkdir %s/_build" % self.ZIP_FOLDER_NAME)
        
        cd_build = "cd %s/_build" % self.ZIP_FOLDER_NAME
        with_boost = "-DWITH_BOOST=%s" % self.deps_cpp_info["Boost"].lib_paths[0]
        shared = "-DBUILD_STATIC=ON"  if not self.options.shared else "-DBUILD_STATIC=OFF"
        self.run('%s && cmake .. %s %s %s -DCMAKE_POSITION_INDEPENDENT_CODE=ON' % (cd_build, cmake.command_line, with_boost, shared))
        self.run("%s && cmake --build . %s" % (cd_build, cmake.build_config))

    def package(self):
        self.copy("*.h", "include", "%s/include" % (self.ZIP_FOLDER_NAME), keep_path=True)
        
        if not self.options.shared:
            self.copy(pattern="*.a", dst="lib", src="%s/_build/lib" % (self.ZIP_FOLDER_NAME), keep_path=False)
        else:
            self.copy(pattern="*.dylib", dst="lib", keep_path=False)
            self.copy(pattern="*.so*", dst="lib", src=self.ZIP_FOLDER_NAME, keep_path=False)
            self.copy(pattern="*.dll", dst="bin", src="_build", keep_path=False)
       
        self.copy(pattern="*.lib", dst="lib", src="%s/_build/lib" % (self.ZIP_FOLDER_NAME), keep_path=False)
        
    def package_info(self):
        if self.options.shared:
            self.cpp_info.libs = ['mysqlcppconn2']
        else:
            self.cpp_info.libs = ["mysqlcppconn2-static"]
            
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
