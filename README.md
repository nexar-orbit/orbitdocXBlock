orbitdocXBlock
===============

### Description ###

This XBlock provides an easy way to embed documents(.doc, .ppt, etc) into a course and allows to download them.
- Download button available to download the document


### Install / Update the XBlock ###

    # Move to the folder where you want to download the XBlock
    cd /edx/app/edxapp
    # Download the XBlock
    sudo -u edxapp git clone https://github.com/nexar-orbit/orbitdocXBlock.git
    # Install the XBlock
    sudo -u edxapp /edx/bin/pip.edxapp install orbitdocXBlock/
    # Upgrade the XBlock if it is already installed, using --upgrade
    sudo -u edxapp /edx/bin/pip.edxapp install orbitdocXBlock/ --upgrade
    # Remove the installation files
    sudo rm -r orbitdocXBlock

### Reboot if something isn't right ###

    sudo /edx/bin/supervisorctl restart all

### Activate the XBlock in your course ###
Go to `Settings -> Advanced Settings` and set `advanced_modules` to `["orbitdoc"]`.

### Use the XBlock in a unit ###
Select `Advanced -> Orbit Document` in your unit.
