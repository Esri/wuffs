from conans import ConanFile


class SkiaConan(ConanFile):
    name = "wuffs"
    version = ""
    url = "https://github.com/Esri/wuffs"
    license = "https://github.com/Esri/wuffs/blob/main/LICENSE"
    description = "Wrangling Untrusted File Formats Safely."

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/wuffs/"

        # headers
        self.copy("wuffs-v0.3.c", src=base + "release/c", dst=relative + "release/c")

        # libraries
        output = "output/" + str(self.settings.platform_architecture_target) + "/staticlib"
        self.copy("*" + self.name + "*", src=base + "../../" + output, dst=output)
