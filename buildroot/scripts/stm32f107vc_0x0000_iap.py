import os

Import("env")

# Relocate firmware from 0x08000000 to 0x08007000
custom_ld_script = os.path.abspath("buildroot/ldscripts/stm32f107vc_0x0000_iap.ld")

for i, flag in enumerate(env["LINKFLAGS"]):
    if "-Wl,-T" in flag:
        env["LINKFLAGS"][i] = "-Wl,-T" + custom_ld_script
    elif flag == "-T":
        env["LINKFLAGS"][i + 1] = custom_ld_script
