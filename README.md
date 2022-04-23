DevOps RPM Build
==================

This repository stores the RPM specifications used by DevOps to build software or libraries installed on server owned by DevOps.

Guideline
------------------
It is important to maintain the standard of our packages. You are advised to follow this guideline whenever possible.

1. Follow [Guidelines for Naming Fedora Packages](https://fedoraproject.org/wiki/Packaging:Naming) for package naming.
1. Follow [Guidelines for Versioning Fedora Packages](https://fedoraproject.org/wiki/Packaging:Versioning) for package versioning.
1. Unless you really mean it, don’t list directories in your %files section in your spec files.
1. Handle circular dependencies.
1. Sign your package.
1. Test uninstall.
1. Use common file location, ownership and permission.
1. Choose symlink over 'alternatives'. Do not use 'alternatives' unless it is system application or services.
1. Manage version symlink with CM tool.
1. [Avoid the Snakes and Dragons Along the Way](https://puppet.com/blog/software-packaging-best-practices).  Let’s talk about the snakes and dragons and glass, and snakes covered in glass that you need to avoid along the way.
    * **Sprawl.** It’s really easy when you’re doing automation work to try to handle all edge cases and all your workflows. Then one day you try to do a software release and you don’t recognize the workflow anymore. You try to run the right rake task, and you get it wrong. Or you look at the list of 30 rake tasks, and you can’t pick it out. That’s a sign of sprawl. We were definitely guilty of this at Puppet Labs, and it’s something to avoid. If the automation has become more of a hindrance than a help, then you’ve gone too far — you should probably take a step back and cut a few things out.
    * **Variation** in workflows. When building automation, try to be opinionated and a little bit flexible at the same time. You may think Debian and RPM need different workflows, but when you hammer down at them, you find they really can be the same workflow. You really should try to get those workflows to be similar now — it’s easier than it will be later.
    * **Historically preserved cruft.** When reading those maintainers' guides, make sure you are reading the ones that are up to date. If you are out there reading the Debian package maintainers’ guide from 1997, and you aren’t packaging for Woody, you’ll be in a world of pain when you try to follow it. You may have had this experience when trying to find Ruby docs for anything but 1.8.7.
    * **Shipping without testing.** This is really dangerous. Packaging is really powerful, and if you do it wrong, you can totally trash someone’s system by mistake. For example, OS X and Solaris have a nice feature: If your packaging path has a symlink in it, and your package thinks it should be a directory, no problem — the package manager will make that symlink a new directory. Whatever the symlink pointed at before is still there — don’t worry. But if that symlink says “var” or “etc,” that system might not be around anymore. Don’t do that.
    * **Over-abstraction.** In our workflows, to build a gem, we dynamically build it out of packaged metadata we have available. On the fly we build a gemspec, and then we build a gem from that. It sounds great, but there’s a potential problem. Say you are a developer, and you want to add a simple thing like a gem dependency to a package like Puppet. How do you do it? It might take a seasoned developer five or 10 minutes to figure out where that goes. That’s a problem, because the idea of the abstraction and automation is to make the development easier, not to slow it down. So we definitely went too far in that example. If you find developers needing maps and guidance to update simple things in packaging, you might want to take a look at those and see if you can simplify that workflow.

Useful commands
------------------
1. Normal build

        rpmbuild -bb --define "_build_version <version>" --define "_release_no <release no>" <spec file>
    Example:

        rpmbuild -bb --define "_build_version 1.0" --define "_release_no 1" something.spec

2. Sign RPM

        rpmsign --addsign <rpm>

3. Rebuild Yum repository data.

        createrepo --update <repo directory>
    Example:

        createrepo --update /var/www/html/yum-repos/centos/7.3.1611/devops/x86_64

