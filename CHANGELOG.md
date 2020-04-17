commit 05ca5ffe1ca6e9e0fe41feed1b08558b8b4a8972
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Apr 17 10:11:16 2020 -0400

    Updated changelog

commit 8eb1017a83f2dc5e3e9a5ef7ebdb811f626e6006
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Apr 16 01:08:09 2020 -0400

    Fixing issue with Python 3.6

commit eeadc9989409eae50103ebc264d32901c1ba6a16
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Apr 8 16:59:41 2020 -0400

    Added CentOS 8 support
    
    CentOS 8 is now supported and tested.
    
    Closes #46

commit ade53eda99d4833f18260464c6eb618786b01b74
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 25 08:24:01 2020 -0400

    Removed facter from Alpine build
    
    Closes #51

commit f222016972a3af647b54ee5ee37fc62e5d126846
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 15 21:16:42 2020 -0500

    Fixed incorrect Debian id format

commit b15a20da4bd7d4008169a1486fef8177e6b5e60c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 15 01:01:15 2020 -0500

    First commit to resolve issues #51 and #52

commit 31a224b18cacb17c734030ef8a7acfa233ef7033
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 25 01:36:45 2020 -0400

    Added logger rotation
    
    Needed to get log rotation enabled to minimize the log file size.
    
    Resolves #70

commit 6d7dd92bba6e70359e1bbc51516ec6ed6557b12f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 23 13:15:02 2020 -0400

    Initial commit of documentation

commit 598b7124d462d564ae9c5b24e785d71d91614971
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 22 11:21:00 2020 -0400

    Python 3.6 removed from testing - Not supported

commit 02ddbf898b604ef49d0cebcffdfb18b69b696ff2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 22 11:14:21 2020 -0400

    Fixed linting issues

commit cd476f2a2c2dce2de5649992ec6e33d0190e5e4d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 22 11:08:30 2020 -0400

    More cleanup and optimizations
    
    - Template validations have been moved out of build module and into
      template as it should be.
    - Changed from subprocess Popen to subprocess run
    - Cleaned up a bit more formatting, etc.

commit 5cbc9a6213b70146fb67129bcbc0ec747447e1e2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 22 02:32:39 2020 -0400

    Fixed linting issues

commit fdd970d12d5ce6412cf4bb835b3d1eecd9a202a1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 22 02:24:25 2020 -0400

    Oh my! So, so many changes.
    
    - Cleaned up many if-then trees to use decision maps instead
    - Cleaned up functions using self in favor of kwargs
    - Added a bit more logging
    - Added more comments to clarify things
    - Probably more that I have forgotten
    - This will be a huge refactoring to clean up code and add more
      efficient logic, etc.

commit f998d27b23d280cd7792967c45b10ed8cfffe671
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 22 02:23:51 2020 -0400

    Renamed generate_templates module to templates
    
    Now has generate as function

commit 4b2306af479229a90c7b531065a412098a96d070
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 21 17:52:00 2020 -0400

    Fixing linting issues.
    
    After updating linting checks from template, the flood gates opened.

commit b28329826496a396a54d380707ab99032e8ea999
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 21 17:26:43 2020 -0400

    Switch from if-then tree to action map
    
    This is a cleaner structure for going forward

commit 1b7e7eb86967ccdc6422753dddd73f07fa30109b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 21 17:25:46 2020 -0400

    Standardized CLI args from Cookiecutter template

commit 5569a65faa0c861130ed1df0b28b09dd66531656
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 21 17:24:46 2020 -0400

    Random cleanup, etc.
    
    Cleaned up code structure a bit. Need to do more cleanup soon.

commit 792ee42591eb4af609ab1bc4dc96cc90a874833e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 21 17:21:58 2020 -0400

    Added new logging functionality
    
    This new functionality comes from the Cookiecutter template
    It replaces teh old logging

commit 13d7b1c3a6f87505a532e55109355141fc2ec44f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 21 17:18:05 2020 -0400

    New files, etc. from updated Cookiecutter template

commit 3eb07dadb0e745e1ff13d93ac1ddcc9719b07b2c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 01:38:11 2020 -0500

    Fixing GitHub Actions and Travis CI tests

commit aa1f12611881b1cf2343b469ca7b747ef8e11bd2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 01:20:16 2020 -0500

    Fixing additional Flake8 linting issues

commit 68d4b03149c9daa906512a4932844cc55779ae6e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 01:17:32 2020 -0500

    Fixing Flake8 linting issues

commit 58ddae01faa8e8dd14b8d03026149615880311e4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 01:12:15 2020 -0500

    Added changelog to track changes

commit 0594c8c09ed934638a76edca561e96e34a42a511
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 01:11:02 2020 -0500

    Added new files which are part of cookiecutter template
    
    - Various files such as code of conduct, contributing guide,
    contributors, license, etc.
    - Closes #65

commit fe4b849e5438b541d2f0d2c9cb573b77315174ea
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 01:09:06 2020 -0500

    Added GitLab CI config

commit 9814dfa150244abec004b1e538e285d5f0ca8f74
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 01:05:28 2020 -0500

    Added Travis CI config

commit a6bcdd95e78f15d64401d5632dc2869b83ba63fd
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 00:56:19 2020 -0500

    Renamed and updated GitHub actions CI testing

commit a1af1f83c6fdfe34d9f1c6247a3eaba2b2569a62
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 00:55:37 2020 -0500

    Updated repo info based on cookiecutter template

commit d7b77936962b609648afbd0f109aeeae66af9053
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 00:49:15 2020 -0500

    Updated gitignore with standard list from cookiecutter template

commit 1d987b3b24f158c06cec06d429d5e655bc4cf9e1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 00:48:50 2020 -0500

    Updated description of module

commit 526c1431b99a7ec5b4fb6e5ff7f9df68f9aa6026
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 00:47:56 2020 -0500

    Changed import of args to cli after renaming

commit e56cca07ae10595ece059d458b2657d2f61e8117
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 00:47:26 2020 -0500

    Updated Python requirements to latest versions

commit 080ff15fa7cf7dde073422d9ad509c129e50a2cd
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 00:44:23 2020 -0500

    Updated pylintrc config

commit ed3ed0762b13dbe8b549daf9504448d346e559d4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 3 00:43:19 2020 -0500

    Renamed args.py to cli.py

commit 4660fc4ab11d7c07c3060d4a4fd0f1a03b82401d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 15 21:11:37 2020 -0500

    Fixed pylint issue for line too long
    
    - disabling this for now

commit 118e99143556f51a838c03efef4bb71769de00cf
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 15 21:04:23 2020 -0500

    First commit of splitting out template constructs
    
    - Splitting these out into build specs will make things more clear I
    believe. With #4 still being a good option, this will at least put more
    clarity in the meantime.
    - Closes #58

commit 1b799041a6b26f65c4d6df328999745d43e66d62
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 15 21:40:00 2020 -0500

    Updated Python requirements to latest
    
    - Closes #61

commit a5fae59043dc4330ebb8e832fae9f2cf606e4c09
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 15 21:31:13 2020 -0500

    Updated Debian and Ubuntu ISO info
    
    - Closes #59

commit 853adfd96c94f5e4b0a0e9a73cc7953c7c41b83a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 15 00:45:28 2020 -0500

    Updated CentOS 7 ISO location
    
    - Resolves #56

commit d393e436d7f68e18aacdff2c0e7452d1f960b71e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 15 00:07:25 2020 -0500

    Resolves issue #54
    
    - We have added the logic required in order to determine whether or not
    the ovftool post processor is added to generate a VMware image. This was
    getting added before regardless if the vmware-iso builder was defined or
    not.

commit 491320ce3572c6683e0dc8b3567e338903e62ea9
Author: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Date:   Tue Dec 3 00:25:03 2019 +0000

    Bump typed-ast from 1.3.1 to 1.3.2
    
    Bumps [typed-ast](https://github.com/python/typed_ast) from 1.3.1 to 1.3.2.
    - [Release notes](https://github.com/python/typed_ast/releases)
    - [Changelog](https://github.com/python/typed_ast/blob/master/release_process.md)
    - [Commits](https://github.com/python/typed_ast/compare/1.3.1...1.3.2)
    
    Signed-off-by: dependabot[bot] <support@github.com>

commit 275e70b2c24a9b0757add2a4382524178d091a9e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 18 00:02:46 2019 -0400

    Added CLI arg to override password in distros.yml
    
    - Based on the fact that you might want to override the default password
    defined in distros.yml. You can now use the -p/--password flag to
    override the default password.
    - closes #49

commit 9d4faaa1fae8ca27ad40de89bd56b55615a6827e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Sep 19 15:50:48 2019 -0400

    Fixed issue with VMware Fusion builder
    
    - Needed to add vmware-vmx to list of valid vmware-iso builder defs.
    - Resolves #20

commit 520b3a9be408d93624f2880603127a7693f23ee1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Sep 19 10:18:06 2019 -0400

    Removed previously used test Virtualbox tools
    
    - We had to use test Virtualbox guest additions for building correctly
    on CentOS/Fedora. This is now not required.
    - Closes #43

commit 47ba05d3948b0a5ec36f6ccfaf5606656559e2eb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 23:21:22 2019 -0400

    - Closes #27

commit feb0948f187bebf93d80f8e6d6b44d5c9d5b696d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 22:23:58 2019 -0400

    Testing vars for worklow steps

commit a23ef1a6bf6fc6593c923411ce02b66f987b82bf
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 17:46:05 2019 -0400

    Fixed Fedora 28/29 ISO info
    
    - Resolves #34

commit 70132346cf1736617ff5822758ab779b38b792c0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 17:43:47 2019 -0400

    Fixed Debian 10 ISO info
    
    - Resolves #33

commit dbbfe6002dac163d6068ae4ef1a33863f4452521
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 17:22:07 2019 -0400

    Closes #32

commit b2571c8553472cc0dde1b7ae0424b10a6d68a52d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 17:15:10 2019 -0400

    Added step to generate Packer templates only

commit e777445f2fb88a58c40119623d65bf859741f7f8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 17:12:14 2019 -0400

    Added installation of Packer

commit 71c7c467fec32c3126af26e5256c97a90404b512
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 17:05:46 2019 -0400

    Fixed pylint issues

commit 3bc4f83b99658a4326d160cb1552ee6f8d04d0ce
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 16:21:29 2019 -0400

    Fix pylint execution

commit c71233784c864e5570d16f3141f0f0db7d384d83
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Sep 18 16:15:27 2019 -0400

    Update main.yml

commit baaf84ea3747b6f18a995b771fff3640dc76f5c1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Sep 17 23:40:16 2019 -0400

    Resolves #30

commit 1bfdda464c876b72e94262e5870459c3ae5e6d6c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Aug 7 00:19:30 2019 -0400

    Closes #28
    
    - Added distro, version as part of bootstrap config in order to separate
    out the applicable builds when generating configs. This will allow us to
    build specific versions if needed after generating configs.

commit c994bf8b98a3839d9eeaf6de6492c00684df7703
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jul 12 16:52:02 2019 -0400

    Cleaned up module imports
    
    I wanted to have a clean consistent method of importing modules.
    
    Importing from this module name rather than using . imports.
    
    Closes #25

commit 17d4f27079381b3a078af081609bcf49c34f17ab
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jul 12 15:53:50 2019 -0400

    First commit of basic logging
    
    Closes #3

commit 04924c501caede3a06db67eaa23b00f6c2437f5b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jul 11 19:03:44 2019 -0400

    Resolves #21

commit 780bccd4748ebc073d486bd87ee1d7f2776ca3f5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 8 22:56:06 2019 -0400

    Added workaround for Ubuntu libssl issue
    
    Resolves #18

commit c1f4fe874f2ff88c53f6ebc516925f14fa6d9e79
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 8 22:52:01 2019 -0400

    Added Debian 10 (Buster)
    
    Resolves #16

commit 714d6c5d8497ca816feddb3b5470c19ffc61f443
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jun 27 01:45:11 2019 -0400

    Added Alpine 3.10 distro
    
    Closes #14

commit b69c96dc1854f5a1cf91008e208d29c9c752d119
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jun 19 07:23:32 2019 -0400

    This resolves #7 to fix incorrect versions displayed.

commit 75005a88ee307b23993dbb572be827520e031965
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jun 19 01:16:24 2019 -0400

    Added check to ensure outputdir exists if defined

commit 127eadcc5bcdad980adf88879719c87675bfff49
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jun 19 01:15:24 2019 -0400

    Added comments

commit 3dca0eedb8c68ca6d285903bb92a894b2e4b766f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jun 19 01:15:06 2019 -0400

    Added initial usage info for generating templates

commit d695ce45e299a19e28b6121818d72f3bcf28ab25
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jun 18 23:31:26 2019 -0400

    Added functionality to generate templates only
    
    This will allow us to generate the template based on distros defined,
    validate the template, and then save as distro-version.json for each
    template.
    
    Resolves #6

commit 651dd6c9aaa1800d3e72c3fd649060dfdf8a3395
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jun 18 23:31:26 2019 -0400

    Added functionality to generate templates only
    
    This will allow us to generate the template based on distros defined,
    validate the template, and then save as distro-version.json for each
    template.

commit 90a6927b6d65b94e84510de8ae187fef1f2cff9e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Jun 8 01:35:18 2019 -0400

    Resolves #8
    
    Added the additional installation instructions to successfully install
    vagrant-libvirt plugin on macOS. This needs to be tested a few more
    times.

commit 2e98a24edadda9a0e1aebdf04e32eff527824987
Author: bunchc <bunchc@gmail.com>
Date:   Wed Jun 5 23:47:07 2019 -0500

    Rework build logic
    
    This adds some checking to the build logic to match defined builders
    to those installed on the system. It also adds the ability to run
    user specified builders.

commit 367799c443c5ff01bd23682873515c43d51ca86c
Author: bunchc <bunchc@gmail.com>
Date:   Tue Jun 4 19:34:07 2019 -0500

    Not all systems ship with cpu-checker /  kvm-ok
    
    Add some additional logic should the system not have `kvm-ok` or `cpu-checker` installed.
    
    This fix attempts a naive check of `/proc/cpuinfo` for some of the flags needed for nested virt.

commit 7b059a3601d3738f8ed345bdf85bdf4723d13f2b
Author: bunchc <bunchc@gmail.com>
Date:   Tue Jun 4 17:13:45 2019 -0500

    Check for hardware acceleration when using KVM on linux

commit 8c9fe4c4d4d29ac7e8dfd1d3f2c09ff18687f639
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed May 1 23:50:52 2019 -0400

    Updated scripts based on Fedora 30

commit 39bcf94591b45eb91c6b8aa6e7a615e98f492efe
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed May 1 23:50:38 2019 -0400

    Added Fedora 30

commit 0fff29c1432e3bf5b8d4ea90824e339499e362bb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Apr 30 00:28:04 2019 -0400

    Updated Debian 9 to 9.9.0

commit 42b16538842193adc6e34ab5b31264c49bda3110
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Apr 19 11:08:59 2019 -0400

    Added Ubuntu 19.04

commit 8ad954cd0e87f7c0ebffe19f1a16dc3a65ef81a4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Apr 13 00:16:56 2019 -0400

    Added check for platform running QEMU to define accelerator

commit 27df0fb8e3ce181744f8c7b3d3a6c0b35aa9f818
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Apr 3 08:41:43 2019 -0400

    Cleaned up help info

commit 1b1033d2f7720953a0192b9b903506eb4fdd024e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Apr 1 23:40:17 2019 -0400

    Added check for QEMU when both vBox/QEMU are defined as builders

commit d8e93ccd1b88bfeb66869f189ce18cbc454d8375
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Apr 1 23:39:44 2019 -0400

    Added boot_wait for 30s per distro to account for timing

commit 35132e379b79079dc0be03d2a258cd01575fb3fa
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 31 23:59:25 2019 -0400

    Updated example help for cli args

commit 3964dc16624d70ba1ed8a2489bc100112c2722d8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 31 23:58:14 2019 -0400

    Cleaned up formatting

commit c1cb43be290aa11c7adb9840ce63a114a9e0499c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 31 23:58:02 2019 -0400

    Added ability to define number of days since last build

commit 63e69d65a7b10895d71359a5bdc65648619da91e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 31 10:18:29 2019 -0400

    Fixed issue with builders not being defined

commit 708e9d0603cbc97c05b5128c5dc91d2960c4a202
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 31 10:13:33 2019 -0400

    Added logic to only build if older than 30 days

commit 9bf86eb7245c788dc8c57eaa52e6da23770097bd
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 30 23:43:36 2019 -0400

    Added custom build manifest

commit 6547cd2fbc7c89741dba9a49c533ba44bd0ecd13
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 30 10:14:04 2019 -0400

    Changed vagrant login shell to bash

commit 26c9e5e0651f254e636cd00f8ee17e0d79e7bcb2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 30 09:14:32 2019 -0400

    Fixing vagrant setup

commit 4b2767a5274c54baad9d0971afe7767b0595c270
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 30 08:53:25 2019 -0400

    Fixed updating vagrant password

commit 724e005ff0fc057b41a1b09b572819a01d28a7a0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 30 01:38:50 2019 -0400

    Fixing permission denied

commit e735642a6e92b6ac3622c4b19171a904d4acb1a4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 23:37:58 2019 -0400

    Changed vagrant output to only exclude qemu when freenas

commit a00d4fb4fe3affcb5f1fa3e85b1fad4a7a635cc2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 23:10:01 2019 -0400

    Added initial Vagrant support

commit 779bdad0aabfe45760a27f0d81e9f077b0e17781
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 19:37:38 2019 -0400

    Trying to fix FreeNAS build

commit b844004f8e9f827cb14c5eb055e770ab589102a3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 18:59:44 2019 -0400

    Added longer wait for freenas

commit d7f47779c1feeec244f2c51a3672c61a1fa1a788
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 18:28:14 2019 -0400

    Added missing shutdown command for FreeNAS

commit d44b0adae3700ce1ff55330c1b8736aff5095149
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 18:26:53 2019 -0400

    Fixed typo for adding ssh info

commit 88d94580f9fbd1de2521f7e0bb7444e3c9446041
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 18:24:40 2019 -0400

    Fixed bootstrap_cfg for FreeNAS

commit 553d9bb9b141b9ee279967e2cb82ea60cb87073f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 18:21:35 2019 -0400

    Fixing FreeNAS

commit 1ba521e08db0f8175b6f6d5bde97e095454b5f6e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 18:19:18 2019 -0400

    Added FreeNAS

commit 75498d2bfb08b54aa53104e3fc597c08caffabaf
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 13:42:25 2019 -0400

    Changed arguments to allow list-distros to execute w/out add'l arguments

commit 64dc857fdd313b4eabce8d8f8cf23bd1e409dbb3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 13:38:10 2019 -0400

    Cleaned up code, added docstrings, etc.

commit a71141f1a6019d190f841f9746f7b9db0850f2eb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 11:00:09 2019 -0400

    Fixed disk_dev for Alpine

commit 219792c3154c48596583db4ce173381c0c041c98
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 10:06:03 2019 -0400

    Added Alpine support

commit 43ddb6992af9f45aebe09ceea6352831d1ab4cf2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 01:04:26 2019 -0400

    Added ability to list distros and only build a specific distro

commit 1e3c6a24e3f447f896d1fa961da6f73ab9f4a913
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 01:03:27 2019 -0400

    Updated help info

commit c1b59c94c0e19377274d4f36989e646ece047e65
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 00:39:38 2019 -0400

    Added Fedora

commit c5122859f451df82f468d02efefe4bd44a3fe6f3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 00:39:23 2019 -0400

    Cleaned up

commit 330a9023b93667cd105549b157e6ace7d203c2dc
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 00:30:06 2019 -0400

    Updated example

commit 66ab538f30d30a2dee2259e4376ea7ee6ddfe1d1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 00:29:49 2019 -0400

    Split out execution to __main__.py

commit 618903a07e8eef33aae56ffae3c01760c77a0e0d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 00:29:24 2019 -0400

    Changed file to default to distros.yml and not required

commit 51474031d58a013141b744f94acd7e14ba2f8c90
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 29 00:28:56 2019 -0400

    Added usage info

commit 379c6875efc578582b514867b48b934fe6c01c3e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Mar 28 22:11:00 2019 -0400

    Cleaned up code

commit 0b941c35dcc2b631bd22219872ad736913bac0ba
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Mar 28 16:57:48 2019 -0400

    Removed vscode directory

commit 71a017c4884121bd12d1da3b1a57732a8852273a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Mar 28 00:24:08 2019 -0400

    Cleaned up code for a better flow

commit 63b3735725a5feed3c56c9a91c0b92c003d738a8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 27 00:34:17 2019 -0400

    Added README

commit c70872cfc9f46286afc0b14e71aa14953777c190
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 27 00:30:52 2019 -0400

    first commit
