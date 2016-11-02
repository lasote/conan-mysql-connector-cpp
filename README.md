[![Build Status](https://travis-ci.org/lasote/conan-mysql-connector-cpp.svg)](https://travis-ci.org/lasote/conan-mysql-connector-cpp)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/lasote/conan-mysql-connector-cpp)](https://ci.appveyor.com/project/lasote/conan-mysql-connector-cpp)


# conan-mysql-connector-cpp

[![badge](https://img.shields.io/badge/conan.io-mysql-connector-cpp%2F2.0.3-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/mysql-connector-cpp/2.0.3/lasote/stable)

[Conan.io](https://conan.io) package for mysql-connector-cpp library. Thanks to Tim Lebedkov for the MinGW integration help! :)

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/mysql-connector-cpp/2.0.3/lasote/stable).

## Build packages

    $ pip install conan_package_tools
    $ python build.py
    
## Upload packages to server

    $ conan upload mysql-connector-cpp/2.0.3@lasote/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install mysql-connector-cpp/2.0.3@lasote/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    mysql-connector-cpp/2.0.3@lasote/stable

    [options]
    mysql-connector-cpp:shared=true # false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
