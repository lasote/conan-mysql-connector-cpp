from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="mysql-connector-cpp:shared", pure_c=True)
    accepted_builds = []
    for build in builder.builds:
        if not build[0]["arch"] == "x86": # Link problems with cdk lib, not investigated, try if feedback is received
            accepted_builds.append([build[0], build[1]])
        if build[0]["compiler"] == "gcc" and float(build[0]["compiler.version"]) > 5:
            build[0]["compiler.libcxx"] = "libstdc++11"
    
    builder.builds = accepted_builds
    builder.run()
